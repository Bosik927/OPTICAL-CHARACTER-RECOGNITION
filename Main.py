from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
import cv2

def disappearRectangle(event):
    #rectangle.grid_forget()
    print("Off")

def createRectangle(event):
    #rectangle.grid()
    print("On")

def mapToBinaryImage(path):
    img = cv2.imread(path)
    im_bw = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)[1]
    print(im_bw)
    cv2.imwrite('binary_image.png', im_bw)

    binaryImage = ImageTk.PhotoImage(Image.open('binary_image.png'))
    leftBottomImage.configure(image=binaryImage)
    leftBottomImage.image = binaryImage

def searchButtonEvent(event):
    path = askopenfilename()
    readImage = ImageTk.PhotoImage(Image.open(path))
    leftImage.configure(image=readImage)
    leftImage.image = readImage

    convertedImage = Image.open(path).convert('LA')
    convertedImage.save('greyscale.png')

    convertedImage2 = ImageTk.PhotoImage(convertedImage)
    rightImage.configure(image=convertedImage2)
    rightImage.image = convertedImage2

    mapToBinaryImage('greyscale.png')


root = Tk()
img = ImageTk.PhotoImage(Image.open("download.png"))

createRect = Button(root, text="Create rectangles: ")
createRect.grid(row =0, column=0)
createRect.bind("<Button-1>", createRectangle)
createRect.bind("<Button-3>", disappearRectangle)

rectangle = Label(root, text = "Hover over image!")
rectangle.grid(row =1, column=0)

leftImage = Label(root, image = img)
leftImage.grid(row =1, column=0)
leftImage.bind('<FocusIn>', createRectangle)
# leftImage.bind("<FocusOut>", disappearRectangle)

button = Button(root,text ="Read sentese")
button.grid(columnspan=2)

rightLabel = Label(root, text="Read sentence:")
rightLabel.grid(row =0, column=1)

rightImage = Label(root, image = img)
rightImage.grid(row =1, column=1)

leftBottomImage = Label(root, image = img)
leftBottomImage.grid(row =2, column=0)

rightBottomImage = Label(root, image = img)
rightBottomImage.grid(row =2, column=1)

searchingButton = Button(root,text ="Search file")
searchingButton.grid(columnspan=2)
searchingButton.bind('<Button-1>', searchButtonEvent)

root.mainloop()