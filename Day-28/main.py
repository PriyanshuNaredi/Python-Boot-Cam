import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = "00:00")
    title_text.config(text="Timer")
    check_marks.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    REPS += 1
    
    work = WORK_MIN *60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    
    if REPS % 8 == 0:
        title_text.config(text="Break",fg=RED)
        count_down(long_break)
    elif REPS % 2 == 0:
        title_text.config(text="Break",fg=PINK)
        count_down(short_break)
    else:
        title_text.config(text="Work",fg=GREEN)
        count_down(work)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    min = math.floor(count/60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(tagOrId=timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(REPS/2)):
            mark = "✅"
        check_marks.config(text=mark)
            


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_text = Label(text="Timer", font=(FONT_NAME, 38, "bold"),
                   fg=GREEN, bg=YELLOW, highlightthickness=0)
title_text.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Day-28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


start_button = Button(text="Start",command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset",command=reset, highlightthickness=0)
reset_button.grid(row=2, column=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW,
                    font=(FONT_NAME, 15, "bold"))
check_marks.grid(row=2, column=1)
check_marks.config(pady=18)


window.mainloop()
