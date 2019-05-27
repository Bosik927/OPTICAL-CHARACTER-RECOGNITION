import glob
import os
import cv2
import numpy


# TODO: Delete unnecessary comments
class Word:
    chars = []

    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def get_coordinate(self):
        return str(self.x1) + " " + str(self.x2) + " " + str(self.y1) + " " + str(self.y2)

    def vectorize_chars(self):
        chars = []
        for char in self.chars:
            width, height = char.shape[:2]
            char_coordinates = find_text(find_blink_lines(char))
            char = char[char_coordinates[0]:char_coordinates[1], 0:width]

            width, height = char.shape[:2]
            x1_offset = int((32 - width) / 2)
            x2_offset = 32 - width - x1_offset
            y1_offset = int((32 - height) / 2)
            y2_offset = 32 - height - y1_offset

            padded_char = cv2.copyMakeBorder(char, x1_offset, x2_offset, y1_offset, y2_offset, cv2.BORDER_CONSTANT,
                                          value=(255, 255, 255))

            chars.append(create_binary_vector(padded_char))
        self.chars = chars


def create_binary_vector(img):
    height, width = img.shape[:2]
    binary_vector = []

    for x in range(height):
        for y in range(width):
            pixel = img[x, y]
            if pixel[0] == 255:
                binary_vector.append(0)
            else:
                binary_vector.append(1)
    return binary_vector

# Funkcja Marcina
def un_skew_text(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    coordinates = numpy.column_stack(numpy.where(thresh > 0))
    angle = cv2.minAreaRect(coordinates)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


def find_font_size(blank_line_list):
    coordinates = find_text(blank_line_list)
    list_length = len(coordinates)
    len_black_block = []
    for coord in range(0, list_length, 2):
        len_black_block.append(coordinates[coord + 1] - coordinates[coord])
    return numpy.median(len_black_block)


def normalize_font_size(img):
    img_bin = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)[1]
    estimated_font_size = find_font_size(find_blink_lines(img_bin))
    ratio = 1 / (estimated_font_size / 30)
    return cv2.resize(img, None, fx=ratio, fy=ratio), ratio


# Zamienia białe pixele na 0 a czarne na 1
def map_pixel_to_binary(pixel):
    if pixel == 0:
        return True
    else:
        return False


# Drukuje binarną wersję obrazu, aktualnie nieużywane
def print_binary_image(binary_image):
    height, width, _ = binary_image.shape
    for x in range(height):
        print("")
        for y in range(width):
            pix_val = binary_image[x, y][1]
            pix_val = map_pixel_to_binary(pix_val)
            print(pix_val, end="")


# Znajduje współrzędne czarnych bloków, mam nadzieję że będzie działać
def find_text(doc_lines):
    coordinates = []
    list_length = len(doc_lines)

    if doc_lines[0] is False:  # True oznacza pustą linię
        coordinates.append(1)
    for line_number in range(list_length - 1):
        if doc_lines[line_number] is False and doc_lines[line_number + 1] is True \
                or doc_lines[line_number] is True and doc_lines[line_number + 1] is False:
            coordinates.append(line_number + 1)
    if doc_lines[list_length - 1] is False:
        coordinates.append(list_length)
    return coordinates


# TODO: Add function with return false or true value and append to list
# Znajduje białe linie
def find_blink_lines(img):
    height, width, _ = img.shape
    line_list = []
    for x in range(height):
        blankLine = True
        for y in range(width):
            pix_val = img[x, y][1]
            pix_val = map_pixel_to_binary(pix_val)
            if pix_val == True:
                blankLine = False
        line_list.append(blankLine)
    return line_list


# Wycina znaki, zapisuje je w obiekcie klasy Word
def crop_text_line(binaryImage):
    heigth, width, _ = binaryImage.shape
    lineListHorizontal = find_blink_lines(binaryImage)
    crpNum = 1
    wordList = []
    linesCoord = find_text(lineListHorizontal)
    estimatedSpaceSize = 6
    for x in range(0, len(linesCoord), 2):
        croppedImgHor = binaryImage[linesCoord[x]:linesCoord[x + 1], 0:width]
        lineListVertical = find_blink_lines(numpy.rot90(croppedImgHor, k=3))
        charCoord = find_text(lineListVertical)
        rows, cols, _ = croppedImgHor.shape
        x1 = charCoord[0]
        crpChars = []
        for y in range(0, len(charCoord), 2):
            croppedImgVer = croppedImgHor[0:rows, charCoord[y]:charCoord[y + 1]]
            x2 = charCoord[y - 1]
            if (y == len(charCoord) - 2):
                crpChars.append((croppedImgVer))
                x2 = charCoord[y + 1]
            if (y > 0):
                if ((charCoord[y] - charCoord[y - 1]) > estimatedSpaceSize or y == len(charCoord) - 2):
                    word = Word(x1, x2, linesCoord[x], linesCoord[x + 1])
                    word.chars = crpChars
                    wordList.append(word)
                    x1 = charCoord[y]
                    crpChars = []
            crpChars.append((croppedImgVer))
    return wordList

# Zapisuje znaki, trzeba utworzyć folder cropped, żeby w nim zapisywało
def saveCroppedCharacters(wordList):
    crpNum = 1
    files = glob.glob('cropped/*.png')
    for f in files:
        os.remove(f)

    for word in wordList:
        for char in word.chars:
            fileName = str(crpNum) + " " + word.get_coordinate() + '.png'
            crpNum += 1
            cv2.imwrite(os.path.join('cropped', fileName), char)


def save_vectorized_chars(word_list):
    f = open("vectors.txt", "w+")
    for word in word_list:
        for vector in word.chars:
            vector_string = ''.join(map(str, vector))
            f.write(str(vector_string) + '\n')
    f.close()