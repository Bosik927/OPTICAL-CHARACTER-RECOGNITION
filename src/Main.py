from tkinter import *
from tkinter.filedialog import askopenfilename

import FullScreenApp as App
import ViewInitializer as View

root = Tk()
App.FullScreenApp(root)

path = askopenfilename()
image = View.resize_image(path)

(canvas, image_on_canvas) = View.create_main_image(image, root)
read_label = View.create_read_label(root)
read_button = View.create_read_button(root)
text = View.create_text(root)
searching_button = View.create_searching_button(root, canvas, image_on_canvas)

root.mainloop()
