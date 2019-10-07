import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
import Preprocesing as prepro
import cv2
import time
import network.main2 as network

picture_width = 960
picture_height = 700
rectangles = []
output_font_family = "Times New Roman"
output_font_size = 23


def create_main_image(image, root):
    canvas = tkinter.Canvas(root, width=picture_width, height=picture_height,
                            scrollregion=(1, 0, image.width(), image.height()), bg='white')
    canvas.grid(row=1, column=0)

    scroll_x = tkinter.Scrollbar(root, orient="horizontal", command=canvas.xview)
    scroll_x.grid(row=2, column=0, sticky="ew")

    scroll_y = tkinter.Scrollbar(root, orient="vertical", command=canvas.yview)
    scroll_y.grid(row=1, column=1, sticky="ns")

    canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
    image_on_canvas = canvas.create_image(0, 0, image=image, anchor=tkinter.NW)

    return canvas, image_on_canvas


def create_read_label(root):
    read_label = tkinter.Label(root, text="Read image: ")
    read_label.grid(row=0, column=0)
    return read_label


def create_text(root):
    text = tkinter.Text(root, height=20, width=25, font=(output_font_family, output_font_size))
    text.tag_configure("center", justify='center')
    text.tag_add("center", 1.0, "end")
    text.grid(row=1, column=2)
    return text


def create_selected_text(root):
    text = tkinter.Text(root, height=5, width=25, font=(output_font_family, output_font_size))
    text.tag_configure("center", justify='center')
    text.tag_add("center", 1.0, "end")
    text.grid(row=2, column=2)
    return text


def create_search_button(root, canvas, image_on_canvas, text, text2):
    searching_button = tkinter.Button(root, text="Search image")
    searching_button.grid(row=1, column=3)
    searching_button.bind('<Button-1>',
                          lambda event, can=canvas, img=image_on_canvas, ro=root, tx=text, tx2=text2:
                          search_button_event(can, img, ro, tx, tx2))
    return searching_button


def search_button_event(canvas, image_on_canvas, root, text, text2):
    path = askopenfilename()
    create_rectangles(canvas, image_on_canvas, root, text, path, text2)


def create_rectangles(canvas, image_on_canvas, root, text, path, text2):
    start_time = time.time()
    image = img_to_photo_image(path)
    canvas.itemconfig(image_on_canvas, image=image)

    (im_bw, ratio) = create_binary_image(path)

    words = prepro.crop_text_line(im_bw)
    for word in words:
        word.vectorize_chars()

    prepro.save_vectorized_chars(words)

    content = []
    for word in words:
        word.values = network.function2(word.chars)
        content.append(word.values)

    create_rectangle_cords(root, canvas, words, ratio, text)

    text2.delete('1.0', END)
    text2.insert(INSERT, content)


    print("Elapsed: " + str(time.time() - start_time))

    canvas.itemconfig(image=image)


def img_to_photo_image(path):
    original_image = Image.open(path)
    return ImageTk.PhotoImage(original_image)


def create_binary_image(path):
    grey_scale_image = create_grey_scale_image(path)
    grey_scale_image.save('grey_scale_2.png')

    img = cv2.imread('grey_scale_2.png')
    img, ratio = prepro.normalize_font_size(img)
    cv2.imwrite('normalized.png', img)

    im_bw = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)[1]
    cv2.imwrite('binary_image2.png', im_bw)
    return im_bw, ratio


def create_grey_scale_image(path):
    grey_scale_image = Image.open(path).convert('LA')
    return grey_scale_image


def on_click_event(text, value):
    text.delete('1.0', END)
    text.insert(INSERT, value)


def create_rectangle_cords(root, canvas, words, ratio, text):
    rectangles.clear()
    for word in words:
        x1 = int(word.x1 / ratio) - 2
        x2 = int(word.x2 / ratio) + 2
        y1 = int(word.y1 / ratio) - 2
        y2 = int(word.y2 / ratio) + 2

        create_rectangle(x1, y1, x2, y2, root, canvas, word, text, fill='green', alpha=.2)


# Changing to binary picture
def create_image(path):
    original_image = Image.open(path)
    resized_image = original_image.resize((picture_width, picture_height), Image.ANTIALIAS)
    read_image = ImageTk.PhotoImage(resized_image)
    return read_image


def create_read_button(root):
    button = tkinter.Button(root, text="Read from image")
    button.grid(columnspan=2)


def create_rectangle(x1, y1, x2, y2, root, canvas, word, text, **kwargs):
    if 'alpha' in kwargs:
        alpha = int(kwargs.pop('alpha') * 255)
        fill = kwargs.pop('fill')
        fill = root.winfo_rgb(fill) + (alpha,)
        image = Image.new('RGBA', (x2 - x1, y2 - y1), fill)
        rectangles.append(ImageTk.PhotoImage(image))
        idd = canvas.create_image(x1, y1, image=rectangles[-1], anchor='nw')
        canvas.tag_bind(idd, '<ButtonPress-1>',
                        lambda event, tx=text, va=word.values: on_click_event(tx, va))
    idd = canvas.create_rectangle(x1, y1, x2, y2, **kwargs)
    canvas.tag_bind(idd, '<ButtonPress-1>',
                    lambda event, tx=text, va=word.values: on_click_event(tx, va))
