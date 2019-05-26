import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
import cv2

picture_width = 960
picture_height = 700
rectangles = []


# def search_button_event(event):
#     actual_path = askopenfilename()
#     img = resize_image(actual_path)
#     View.create_main_image(picture_width, picture_height, img)
#     # createLeftImage(actual_path)
#     print('dupa')
#     print('dupa')
#     # createGreyScaleImage(path)
#     # createRightImage('greyscale.png')


# Changing to binary picture
# def createLeftImage(path):
#     originalImage = Image.open(path)
#     resizedImage = originalImage.resize((picture_width, picture_height), Image.ANTIALIAS)
#     readImage = ImageTk.PhotoImage(resizedImage)
#
#     # main_image.image_on_canvas(image=readImage)
#     main_image.create_image(0, 0, image=image, anchor=tkinter.NW)
#
#
# def createGreyScaleImage(path):
#     greyScaleImage = Image.open(path).convert('LA')
#     convertedImage2 = ImageTk.PhotoImage(greyScaleImage)
#     rightImage.configure(image=convertedImage2)
#     rightImage.image = convertedImage2
#     return greyScaleImage
#
#
# def createRightImage(path):
#     img = cv2.imread(path)
#     im_bw = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)[1]
#     cv2.imwrite('binary_image.png', im_bw)
#
#     binaryImage = Image.open('binary_image.png')
#     rezisedImage = binaryImage.resize((picture_width, picture_height), Image.ANTIALIAS)
#     binaryImage = ImageTk.PhotoImage(rezisedImage)
#     rightImage.configure(image=binaryImage)
#     rightImage.image = binaryImage
#
#
# def searchButtonEvent(event):
#     path = askopenfilename()
#     createLeftImage(path)
#     createGreyScaleImage(path)
#     createRightImage('greyscale.png')


# Creating rectangles
# def disappearRectangle(event):
#     rectangle.grid_forget()
#
#
# def createRectangle(event):
#     rectangle.grid(row=1, column=0)


def create_searching_button(root, canvas, image_on_canvas):
    searching_button = tkinter.Button(root, text="Search image")
    searching_button.grid(columnspan=1)
    searching_button.bind('<Button-1>', lambda event, can=canvas, img=image_on_canvas: search_button_event(can, img))
    return searching_button


def search_button_event(canvas, image_on_canvas):
    path = askopenfilename()
    image = resize_image(path)

    canvas.itemconfig(image_on_canvas, image=image)
    canvas.itemconfig(image=image)

    # canvas.itemconfig(image_on_canvas, image=image)
    # print(image.height())
    # print(image.width())

    # image_canvas = create_main_image(picture_width, picture_height, image)

    # path = askopenfilename()
    # create_image(path)
    # print('search_button_event')
    # createGreyScaleImage(path)
    # createRightImage('greyscale.png')


# Changing to binary picture
def create_image(path):
    original_image = Image.open(path)
    resized_image = original_image.resize((picture_width, picture_height), Image.ANTIALIAS)
    read_image = ImageTk.PhotoImage(resized_image)
    return read_image


def create_text(root):
    text = tkinter.Text(root, height=43, width=30)
    text.grid(row=1, column=1)
    return text


def create_read_button(root):
    button = tkinter.Button(root, text="Read from image")
    button.grid(columnspan=2)


def create_read_label(root):
    read_label = tkinter.Label(root, text="Read image: ")
    read_label.grid(row=0, column=0)
    return read_label


def create_main_image(image, root):
    canvas = tkinter.Canvas(width=picture_width, height=picture_height, bg='black')
    canvas.grid(row=1, column=0)

    image_on_canvas = canvas.create_image(0, 0, image=image, anchor=tkinter.NW)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # FIXME : Implement method
    canvas.bind('<Enter>', create_rectangles)
    canvas.bind("<Leave>", disappear_rectangles)

    # rectangles.append()
    obj1_id = canvas.create_rectangle(230, 10, 290, 60, outline="#f11", fill="#1f1", width=2)
    canvas.tag_bind(obj1_id, '<ButtonPress-1>', rectangle_on_click_event1)
    # canvas.tag_bind(obj1_id, '<Enter>', lambda event, can=canvas, rect_id=obj1_id: rectangle_appear(can, rect_id))
    # canvas.tag_bind(obj1_id, '<Leave>', lambda event, can=canvas, rect_id=obj1_id: rectangle_disappear(can, rect_id))
    create_rectangle(10, 10, 2000, 1000, root, canvas, fill='green', alpha=.2)

    obj2_id = canvas.create_rectangle(400, 200, 290, 60, outline="#f11", fill="#1f1", width=2)
    canvas.tag_bind(obj2_id, '<ButtonPress-1>', rectangle_on_click_event2)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    return canvas, image_on_canvas


def create_rectangle(x1, y1, x2, y2, root, canvas, **kwargs):
    if 'alpha' in kwargs:
        alpha = int(kwargs.pop('alpha') * 255)
        fill = kwargs.pop('fill')
        fill = root.winfo_rgb(fill) + (alpha,)
        image = Image.new('RGBA', (x2 - x1, y2 - y1), fill)
        rectangles.append(ImageTk.PhotoImage(image))
        canvas.create_image(x1, y1, image=rectangles[-1], anchor='nw')
    canvas.create_rectangle(x1, y1, x2, y2, **kwargs)


# EVENTS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# TODO: To implement
def rectangle_on_click_event1(event):
    print('FIRST SHAPE')


def rectangle_disappear(canvas, id):
    print('FIRST SHAPE')


def rectangle_appear(canvas, id):
    print('FIRST SHAPE')


def rectangle_on_click_event2(event):
    print('SECOND SHAPE')


# TODO: To implement
def create_rectangles(event):
    print("on")


def disappear_rectangles(event):
    print("off")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def resize_image(path):
    original_image = Image.open(path)
    resized_image = original_image.resize((picture_width, picture_height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized_image)
