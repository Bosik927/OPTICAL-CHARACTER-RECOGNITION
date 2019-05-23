import cv2
import os
import numpy
import glob


class Word:
    chars = []
    def __init__(self, x1,x2,y1,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def getCoordsStr(self):
        return str(self.x1) + " " + str(self.x2) + " " + str(self.y1) + " " + str(self.y2)


# Funkcja Marcina
def un_skew_text(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    coords = numpy.column_stack(numpy.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


def findFontSize(blankLineList):
    coords = findText(blankLineList)
    lenList = len(coords)
    lenBlackBlock = []
    for coord in range(0, lenList, 2):
        lenBlackBlock.append(coords[coord+1]-coords[coord])
    return numpy.median(lenBlackBlock)

# Zamienia białe pixele na 0 a czarne na 1
def pixelToBinary(pixel):
    if pixel == 0:
        return True
    else:
        return False


# Drukuje binarną wersję obrazu, aktualnie nieużywane
def printBinaryImage(binaryImage):
    heigth, width, _ = binaryImage.shape
    for x in range(heigth):
        print("")
        for y in range(width):
            pixVal = binaryImage[x, y][1]
            pixVal = pixelToBinary(pixVal)
            print(pixVal, end="")


# Znajduje współrzędne czarnych bloków, mam nadzieję że będzie działać
def findText(docLines):
    coordinates = []
    listLen = len(docLines)

    if docLines[0] is False:  # True oznacza pustą linię
        coordinates.append(1)
    for lineNum in range(listLen - 1):
        if docLines[lineNum] is False and docLines[lineNum + 1] is True or docLines[lineNum] is True and docLines[
            lineNum + 1] is False:
            coordinates.append(lineNum + 1)
    if docLines[listLen - 1] is False:
        coordinates.append(listLen)
    return coordinates


# Znajduje białe linie
def findBlankLines(img):
    heigth, width, _ = img.shape
    lineList = []
    for x in range(heigth):
        blankLine = True
        for y in range(width):
            pixVal = img[x, y][1]
            pixVal = pixelToBinary(pixVal)
            if pixVal == True: blankLine = False
        lineList.append(blankLine)
    return lineList


# Wycina linie tekstu, trzeba utworzyć folder cropped, żeby w nim zapisywało
def cropTextLine(binaryImage):
    heigth, width, _ = binaryImage.shape
    lineListHorizontal = findBlankLines(binaryImage)
    crpNum = 1
    wordList = []
    linesCoord = findText(lineListHorizontal)
    estimatedSpaceSize=findFontSize(lineListHorizontal)/4
    print(estimatedSpaceSize)
    for x in range(0, len(linesCoord), 2):
        croppedImgHor = binaryImage[linesCoord[x]:linesCoord[x + 1], 0:width]
        lineListVertical = findBlankLines(numpy.rot90(croppedImgHor, k=3))
        charCoord = findText(lineListVertical)
        rows, cols, _ = croppedImgHor.shape
        x1 = charCoord[0]
        crpChars = []
        for y in range(0, len(charCoord), 2):
            croppedImgVer = croppedImgHor[0:rows, charCoord[y]:charCoord[y + 1]]
            if(y == len(charCoord)-2):
                crpChars.append((croppedImgVer))
            if(y>0):
                if((charCoord[y] - charCoord[y-1])>4 or y == len(charCoord)-2):
                    word = Word(x1,charCoord[y-1],linesCoord[x],linesCoord[x + 1])
                    word.chars=crpChars
                    wordList.append(word)
                    x1=charCoord[y]
                    crpChars = []
            crpChars.append((croppedImgVer))
    return wordList


def saveCroppedCharacters(wordList):
    crpNum = 1
    files = glob.glob('cropped/*.png')
    for f in files:
        os.remove(f)

    for word in wordList:
        for char in word.chars:
            fileName = str(crpNum) + " " + word.getCoordsStr() + '.png'
            crpNum += 1
            cv2.imwrite(os.path.join('cropped', fileName), char)

# Funkcja Stasia, podstawowa obsługa programu
# def mapToBinaryImage(path):
#     img = cv2.imread(path)
#     im_bw = un_skew_text(img)  # prostrowanie skanu
#     im_bw = cv2.threshold(im_bw, 128, 255, cv2.THRESH_BINARY)[1]
#
#     cv2.imwrite('binary_image.png', im_bw)
#
#     binaryImage = ImageTk.PhotoImage(Image.open('binary_image.png'))
#     leftBottomImage.configure(image=binaryImage)
#     leftBottomImage.image = binaryImage
#
#     wordList = cropTextLine(im_bw)
#     #for word in wordList:
#         #word.printCoords()
#     saveCroppedCharacters(wordList)
