import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
import Preprocesing as pre
import cv2
import time

picture_width = 960
picture_height = 700
rectangles = []


def create_searching_button(root, canvas, image_on_canvas):
    searching_button = tkinter.Button(root, text="Search image")
    searching_button.grid(columnspan=1)
    searching_button.bind('<Button-1>',
                          lambda event, can=canvas, img=image_on_canvas, ro=root: search_button_event(can, img, ro))
    return searching_button


# TODO: Optimiześ
def search_button_event(canvas, image_on_canvas, root):
    path = askopenfilename()
    start_time = time.time()
    image = resize_image(path)
    canvas.itemconfig(image_on_canvas, image=image)
    canvas.itemconfig(image_on_canvas, image=image)

    (grey_scale_image, gui_grey_scale_image) = create_grey_scale_image(path)
    grey_scale_image.save('grey_scale_2.png')

    img = cv2.imread('grey_scale_2.png')
    img, ratio = pre.normalize_font_size(img)
    cv2.imwrite('normalized.png', img)

    im_bw = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)[1]
    cv2.imwrite('binary_image2.png', im_bw)

    words = pre.crop_text_line(im_bw)
    for word in words:
        word.vectorize_chars()
    pre.save_vectorized_chars(words)

    pre.save_vectorized_chars(words)

    create_rectangles2(root, canvas, words, ratio)
    print("Elapsed: " + str(time.time()-start_time))
    canvas.itemconfig(image=image)



def create_rectangles2(root, canvas, words, ratio):
    rectangles.clear()
    for word in words:
        x1 = int(word.x1 / ratio) - 2
        x2 = int(word.x2 / ratio) + 2
        y1 = int(word.y1 / ratio) - 2
        y2 = int(word.y2 / ratio) + 2
        rectangles.append(
            create_rectangle(x1, y1, x2, y2, root, canvas, fill='green', alpha=.2))


def create_grey_scale_image(path):
    grey_scale_image = Image.open(path).convert('LA')
    gui_grey_scale_image = ImageTk.PhotoImage(grey_scale_image)
    return grey_scale_image, gui_grey_scale_image


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

    # TODO: Delete
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # FIXME : Implement method, adding rectangles
    canvas.bind('<Enter>', create_rectangles)
    canvas.bind("<Leave>", disappear_rectangles)

    # rectangles.append()z

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


# TODO: Delete
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


# TODO: Delete
def create_rectangles(event):
    print("on")


def disappear_rectangles(event):
    print("off")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def resize_image(path):
    original_image = Image.open(path)
    # resized_image = original_image.resize((picture_width, picture_height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(original_image)
