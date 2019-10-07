from tkinter import *
from tkinter.filedialog import askopenfilename

import FullScreenApp as App
import ViewInitializer as View

root = Tk()
App.FullScreenApp(root)

path = askopenfilename()
image = View.img_to_photo_image(path)

(canvas, image_on_canvas) = View.create_main_image(image, root)
read_label = View.create_read_label(root)
text = View.create_text(root)
selected_text = View.create_selected_text(root)
searching_button = View.create_search_button(root, canvas, image_on_canvas, selected_text, text)

root.mainloop()
