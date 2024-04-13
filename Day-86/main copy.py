import os
import sys
from wonderwords import RandomSentence
from tkinter import *
from tkinter import messagebox
import time

list = []

s = RandomSentence()
string_text=''
for i in range(10):
    string_text += str(s.bare_bone_with_adjective()).replace('.','').lower()
    
list += string_text.split(' ')
 

root = Tk()
label = None

user_text = ''

current_char = ''
i = 0
j = len(string_text) - 2
k = 0

words_typed = 0

def key_pressed(event):
    global label, user_text, i, j, k, words_typed   
    
    current_word.config(text='Current word is \n' + list[k])
    
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

# canvas = Canvas(height=526, width=800)
#                 # bg=BACKGROUND_COLOR, highlightthickness=0)
# front_img = PhotoImage(file="Day-86\card_back.png")
# canvas_image = canvas.create_image(400, 263, image=front_img)
# card_title = canvas.create_text(
#     400, 150, text="\n\n\n\n\n"+string_text, width=400, font=("Ariel", 20),
#     justify='left')

# canvas.pack(padx=100,pady=20)



text_label = Label(root,text=string_text,wraplength=600, justify="center",padx=50,pady=50,bg='lightyellow',font=("Arial", 20, "italic"), borderwidth=2, relief="solid")
text_label.pack()

current_word = Label(root,text="1st Word",wraplength=600, justify="center",padx=50,pady=50,font=('white',20))
# current_word.pack()

canvas = Canvas(height=200, width=200)
                # bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="Day-86\card_back.png")
canvas_image = canvas.create_image(50, 50, image=front_img)
card_title = canvas.create_text(
    400, 150, text="1st Word", width=100, font=("Ariel", 20),
    justify='left')
canvas.pack()

user_text_label = Label(root,text="string_text",wraplength=600, justify="center",padx=50,pady=50,bg='lightgrey')
user_text_label.pack()


root.bind('<Key>',key_pressed)
root.bind('<BackSpace>',delete_user_text)



def a_callback_function():
    global words_typed
    print("a_callback_function was called.")
    messagebox.showinfo("Time Countdown", "Time's up \n Words Per minute: " + str(words_typed))
    print(words_typed)
    restart_program()
    
root.after(10000,a_callback_function) # after 10 secs

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

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