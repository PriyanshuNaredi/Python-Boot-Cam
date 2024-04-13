import os
import sys
from wonderwords import RandomSentence
from tkinter import *
from tkinter import messagebox
import time

# Global Variable

list = []

s = RandomSentence()
string_text = ''
for i in range(10):
    string_text += str(s.bare_bone_with_adjective()).replace('.', '').lower()

list += string_text.split(' ')


root = Tk()
label = None

user_text = ''

current_char = ''
i = 0
j = len(string_text) - 2
k = 0

words_typed = 0

def greet():
    messagebox.showinfo(
        "Info", "How to play \n Start Typing, will only get a minute \n Time starts After this Alert" )

# Functions
def key_pressed(event):
    global label, user_text, i, j, k, words_typed
    if event.char == string_text[i]:
        user_list = user_text.split(" ")
        temp = words_typed
        words_typed = len(set(user_list).intersection(list))
        user_text += event.char
        if i < j:
            i += 1
            user_text_label.config(text=user_text)
            user_text_label.pack()
        if words_typed > temp:
            k += 1
        else:
            pass
    else:
        pass


def delete_user_text(event):
    global user_text, i, string_text
    if user_text[-1] != string_text[i-1]:
        user_text = user_text[:-1]
        user_text_label.config(text=user_text)
        user_text_label.pack()


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def a_callback_function():
    global words_typed
    print("a_callback_function was called.")
    messagebox.showwarning(
        "Time Countdown", "Time's up \n Words Per minute: " + str(words_typed))
    print(words_typed)
    restart_program()

# UI
# messagebox.showinfo(
#         "Info", "How to play \n Start Typing, will only get a minute \n Time starts After this Alert" )
text_label = Label(root, text=string_text, wraplength=600, justify="center", padx=50,
                   pady=50, bg='lightyellow', font=("Arial", 20, "italic"), borderwidth=2, relief="solid")
text_label.pack()

current_word = Label(root, text="Current Word", wraplength=600,
                     justify="center", padx=50, pady=50, font=('white', 20))
current_word.pack()

user_text_label = Label(root, text="string_text", wraplength=600,
                        justify="center", padx=50, pady=50, bg='lightgrey')
user_text_label.pack()



root.bind('<Key>', key_pressed)
root.bind('<BackSpace>', delete_user_text)


root.after(10000, a_callback_function)  # after 10 secs


root.mainloop()


# def key_pressed(event):
#     if hasattr(key_pressed,'label'):
#         key_pressed.label.destroy()
#     label=Label(root,text='Key pressed - '+event.char)
#     label.text = label
#     label.pack()


# text_scroll = Scrollbar(root)
# text_scroll.pack(side=RIGHT, fill=Y)

# text = Text(root, wrap='word', yscrollcommand=text_scroll.set, bg="lightgray", padx=10, pady=10)
# text.insert('1.0', string_text)
# text.pack(expand=True, fill=BOTH)

# text_scroll.config(command=text.yview)

# if label is not None:
#     label.config(text='Key pressed - ' + event.char)

# else:
#     label = Label(root, text='Key pressed - ' + event.char)
#     label.pack()
# user_text_label.config(text=user_text)
# user_text_label.pack()
# from wonderwords import RandomSentence
# from tkinter import *
# from tkinter import messagebox
# import time

# list = []

# s = RandomSentence()
# string_text=''
# for i in range(10):
#     string_text += str(s.bare_bone_with_adjective()).replace('.',' ').lower()


# root = Tk()
# label = None

# user_text = ''

# current_char = ''
# i = 0
# j = len(string_text) - 2

# timer_start = 0
# end_timer = 60

# words_typed = 0

# def key_pressed(event):
#     global label, user_text,current_char, i, j, timer_start, end_timer, words_typed
#     if timer_start <= end_timer:
#         timer_start += 1
#         if event.char == string_text[i]:
#             if event.char == '':
#                 words_typed += 1
#             user_text += event.char
#             if i < j:
#                 i += 1
#                 user_text_label.config(text=user_text)
#                 user_text_label.pack()
#             else:
#                 pass
#         else:
#             pass
#     else:
#         messagebox.showinfo("Time Countdown", "Time's up " + str(words_typed))
#         print(words_typed)


# def delete_user_text(event):
#     global user_text
#     user_text = user_text[:-1]
#     user_text_label.config(text=user_text)
#     user_text_label.pack()


# text_label = Label(root,text=string_text,wraplength=600, justify="center",padx=50,pady=50,bg='lightgrey')
# text_label.pack()

# user_text_label = Label(root,text="string_text",wraplength=600, justify="center",padx=50,pady=50,bg='lightgrey')
# user_text_label.pack()
# root.bind('<Key>',key_pressed)
# root.bind('<BackSpace>',delete_user_text)

# def a_callback_function():
#     print("a_callback_function was called.")

# # my_button = Button(root, text="Start")
# # my_button.after(100_0, a_callback_function)
# # my_button.pack()


# root.mainloop()


# # def key_pressed(event):
# #     if hasattr(key_pressed,'label'):
# #         key_pressed.label.destroy()
# #     label=Label(root,text='Key pressed - '+event.char)
# #     label.text = label
# #     label.pack()


# # text_scroll = Scrollbar(root)
# # text_scroll.pack(side=RIGHT, fill=Y)

# # text = Text(root, wrap='word', yscrollcommand=text_scroll.set, bg="lightgray", padx=10, pady=10)
# # text.insert('1.0', string_text)
# # text.pack(expand=True, fill=BOTH)

# # text_scroll.config(command=text.yview)


#     # if label is not None:
#     #     label.config(text='Key pressed - ' + event.char)

#     # else:
#     #     label = Label(root, text='Key pressed - ' + event.char)
#     #     label.pack()
#     # user_text_label.config(text=user_text)
#     # user_text_label.pack()
