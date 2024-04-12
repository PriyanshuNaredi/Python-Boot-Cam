from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk, ImageFont, ImageDraw

# Creating a new window and configurations
window = Tk()
window.title("Watermark")
window.minsize(width=500, height=500)

img_path = ""
watermark_path = ""

def upload_img():
    global img_path, img
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = filedialog.askopenfilename(filetypes=fileTypes)
    img_path = str(path)
    img = Image.open(path)
    img.thumbnail((300, 300))  # Resize the image to fit the label
    img = ImageTk.PhotoImage(img)
    imgLabel = Label(window, image=img)
    imgLabel.pack()
    
def upload_watermark_img():
    global watermark_path
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = filedialog.askopenfilename(filetypes=fileTypes)
    watermark_path = str(path)
    
welcome_text = Label(window, text='Add Student Data with Photo', width=30, font=('times', 18, 'bold'))
welcome_text.pack()

upload_img_button = Button(window, text="Upload image", command=upload_img)
upload_img_button.pack()

upload_watermark_button = Button(window, text="Upload image", command=upload_watermark_img)
upload_watermark_button.pack()



def add_img_watermark():
    global image,img
    if not img_path or not watermark_path:
        print("Please upload an image and a watermark image first.")
        return
    img = Image.open(img_path)
    watermark_img = Image.open(watermark_path)
    img.paste(watermark_img,(0,0))
    img.show()
    image = ImageTk.PhotoImage(img)
    imgLabel = Label(image=image)
    imgLabel.pack()

def add_text_watermark():
    global image
    if not img_path:
        print("Please upload an image first.")
        return
    entry = Entry(window, width=30)
    entry.insert(END, string="Priyanshu Naredi")
    watermark_text = entry.get()
    image = Image.open(img_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 20)
    draw.text((10, 10), text=watermark_text, font=font)  # Position the text watermark on the image
    image.thumbnail((300, 300))  # Resize the image to fit the label
    img = ImageTk.PhotoImage(image)
    imgLabel = Label(window, image=img)
    imgLabel.pack()

# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(window, text="Text As Watermark", value=1, variable=radio_state, command=add_text_watermark)
radiobutton2 = Radiobutton(window, text="Image As Watermark", value=2, variable=radio_state, command=add_img_watermark)
radiobutton1.pack()
radiobutton2.pack()

window.mainloop()
# from tkinter import *
# from tkinter import filedialog
# from tkinter.filedialog import askopenfile
# from PIL import Image, ImageTk
# from PIL import Image, ImageFont, ImageDraw

# img = ''

# img_path =''

# #Creating a new window and configurations
# window = Tk()
# window.title("Watermark")
# window.minsize(width=500, height=500)


# def upload_img():
#     global img_path,img
#     fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
#     path = filedialog.askopenfilename(filetypes=fileTypes)
#     img_path = str(path)
#     img = ImageTk.PhotoImage(file=path)
#     imgLabel = Label(image=img)
#     # imgLabel.grid(row=3,column=1)
#     imgLabel.pack()
    
    
# welcome_text = Label(text='Add Student Data with Photo',width=30,font=(('times', 18, 'bold')))  
# # welcome_text.grid(row=1,column=1)
# welcome_text.pack()


# upload_img_button = Button(text="Upload image", command=upload_img)
# # upload_img_button.grid(row=2,column=1)
# upload_img_button.pack()

# # img = ImageTk.PhotoImage(file=img_path)
# # img_label = Label(image=img).pack()


# def upload_watermark_img():
#     global watermark_path
#     fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
#     path = filedialog.askopenfilename(filetypes=fileTypes)
#     watermark_path = str(path)
#     watermark_img = ImageTk.PhotoImage(file=path)
#     imgLabel = Label(image=watermark_img)
#     # imgLabel.grid(row=3,column=1)
#     imgLabel.pack()

# #Radiobutton
# def add_img_watermark():
#     upload_wimg_button = Button(text="Upload image", command=upload_watermark_img)
# # upload_img_button.grid(row=2,column=1)
#     upload_wimg_button.pack()
    
    
    

    
# def add_text_watermark():
#     entry = Entry(width=30)
#     entry.insert(END, string="Priyanshu Naredi")
#     print(entry.get())
#     image = Image.open(img_path)
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.truetype("arial.ttf", 10)
#     draw.text((0,0),text=entry.get(),font=font)
#     image.show()
#     image.save('D:\Python\Day-85\images\w1.jpg')
#     entry.pack()


# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Text As Watermark", value=1, variable=radio_state, command=add_text_watermark)
# radiobutton2 = Radiobutton(text="Image As Watermark", value=2, variable=radio_state, command=add_img_watermark)
# radiobutton1.pack()
# radiobutton2.pack()


# # img = Image.open("Day-85/base.jpg")
# # test = ImageTk.PhotoImage(image=img)
# # label = Label(image=test)
# # label.image = test
# # label.place(x=250,y=250)

# # img = ImageTk.PhotoImage(file='Day-85/base.jpg')
# # imgLabel = Label(image=img)
# # imgLabel.pack()





# window.mainloop()