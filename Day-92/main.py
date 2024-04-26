from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief

NUMBER_OF_COLORS = 15
TITLE_FONT = "Arial"
TITLE_COLOR = "#EFEFEF"
WORD_FONT = "Times New Roman"
WORD_COLOR = "#EEEEEE"
BACKGROUND_COLOR = "#222832"
BTN_BACKGROUND_COLOR = "#2F3847"


def get_img_colors():
    img_file = filedialog.askopenfilename(
        initialdir="/",
        title="Select IMG",
        filetypes=(('Image Files', "*.jpg;*.jpeg;*.png"), ("All Files", "*.*"))
    )
    img = Image.open(img_file, 'r').convert('RGB')
    color_thief = ColorThief(img_file)
    global displayed_image

    # build a color palette
    palette = color_thief.get_palette(color_count=12)
    for i in palette:
        hex_color = '#%02x%02x%02x' % (i)
        colors_text.insert(END,hex_color+"\n")
 


def copy_to_clipboard():
    root.clipboard_append(colors_text.get("1.0", END))


def clear_text():
    colors_text.delete("1.0", END)

root = Tk()
root.title('Image to Color List')
root.config(padx=25, pady=25, bg=BACKGROUND_COLOR)
title_label = Label(text="Image to Color List", font=(
    TITLE_FONT, 32, "bold"), fg=TITLE_COLOR, bg=BACKGROUND_COLOR)
open_btn = Button(text="Select Image", font=(WORD_FONT, 20), width=25, fg=WORD_COLOR, bg=BTN_BACKGROUND_COLOR,
                  command=get_img_colors)
copy_btn = Button(text="Copy Text", font=(WORD_FONT, 20), width=25, fg=WORD_COLOR, bg=BTN_BACKGROUND_COLOR,
                  command=copy_to_clipboard)
clear_btn = Button(text="Clear Text", font=(WORD_FONT, 20), width=25, fg=WORD_COLOR, bg=BTN_BACKGROUND_COLOR,
                   command=clear_text)
colors_text = Text(root, width=35, height=16, font=(TITLE_FONT, 14))
title_label.grid(column=0, row=0, pady=20)
colors_text.grid(column=0, row=2)
open_btn.grid(column=0, row=3, pady=10)
copy_btn.grid(column=0, row=4)
clear_btn.grid(column=0, row=5, pady=10)
root.mainloop()
