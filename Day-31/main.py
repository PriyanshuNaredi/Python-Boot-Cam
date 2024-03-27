from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# csv file
try:
    data = pandas.read_csv("Day-31/data/words_to_learn.csv")
except FileNotFoundError:
    org_data = pandas.read_csv("Day-31/data/french_words.csv")
    to_learn = org_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# functions


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("Day-31/data/words_to_learn.csv", index=False)
    next_card()


# Tkinter

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800,
                bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="Day-31\images\card_front.png")
back_img = PhotoImage(file="Day-31\images\card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(
    400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


wrong_img = PhotoImage(file="Day-31/images/wrong.png")
wrong_button = Button(text="right", image=wrong_img, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="Day-31/images/right.png")
right_button = Button(text="right", image=right_img, command=is_known)
right_button.grid(row=1, column=1)


next_card()

window.mainloop()
