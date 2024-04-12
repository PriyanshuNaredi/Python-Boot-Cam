from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from PIL import Image, ImageFont, ImageDraw


#Creating a new window and configurations
window = Tk()
window.title("Watermark")
window.minsize(width=500, height=500)


def upload_img():
    global img
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = filedialog.askopenfilename(filetypes=fileTypes)
    img = ImageTk.PhotoImage(file=path)
    imgLabel = Label(image=img)
    # imgLabel.grid(row=3,column=1)
    imgLabel.pack()
    
    
welcome_text = Label(text='Add Student Data with Photo',width=30,font=(('times', 18, 'bold')))  
# welcome_text.grid(row=1,column=1)
welcome_text.pack


upload_img_button = Button(text="Upload image", command=upload_img)
# upload_img_button.grid(row=2,column=1)
upload_img_button.pack()


def upload_watermark_img():
    global watermark_img
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = filedialog.askopenfilename(filetypes=fileTypes)
    watermark_img = ImageTk.PhotoImage(file=path)
    imgLabel = Label(image=watermark_img)
    # imgLabel.grid(row=3,column=1)
    imgLabel.pack()

#Radiobutton
def add_img_watermark():
    upload_wimg_button = Button(text="Upload image", command=upload_watermark_img)
# upload_img_button.grid(row=2,column=1)
    upload_wimg_button.pack()
    # width,height = img.size
    transparent = Image.new('RGBA', (0,0,0,0))
    transparent.paste(img,(0,0))
    transparent.paste(watermark_img, (0,0))
    transparent.show()
    
def add_text_watermark():
    entry = Entry(width=30)
    entry.insert(END, string="Priyanshu Naredi")
    print(entry.get())
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 4)
    draw.text((0,0),text=entry.get(),font=font)
    entry.pack()


#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Text As Watermark", value=1, variable=radio_state, command=add_text_watermark)
radiobutton2 = Radiobutton(text="Image As Watermark", value=2, variable=radio_state, command=add_img_watermark)
radiobutton1.pack()
radiobutton2.pack()


# img = Image.open("Day-85/base.jpg")
# test = ImageTk.PhotoImage(image=img)
# label = Label(image=test)
# label.image = test
# label.place(x=250,y=250)

# img = ImageTk.PhotoImage(file='Day-85/base.jpg')
# imgLabel = Label(image=img)
# imgLabel.pack()





window.mainloop()