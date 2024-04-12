# ------Working
import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
import sys

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if filepath:
        display_image(filepath)

def display_image(filepath):
    global displayed_image
    displayed_image = Image.open(filepath)
    displayed_image.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
    img = ImageTk.PhotoImage(displayed_image)
    
    # Clear any previous image displayed
    if hasattr(display_image, 'label'):
        display_image.label.destroy()
    if hasattr(display_image, 'frame'):
        display_image.frame.destroy()
    if hasattr(display_image, 'save_button'):
        display_image.save_button.destroy()
    if hasattr(display_image, 'restart_button'):
        display_image.restart_button.destroy()
    
    label = tk.Label(root, image=img)
    label.image = img  # Keep a reference to the image object to prevent garbage collection
    label.pack()
    
    # Store the label reference to remove it when a new image is uploaded
    display_image.label = label
    
    # Add frame with options
    frame = tk.Frame(root)
    frame.pack(pady=10)
    
    option1_button = tk.Button(frame, text="Option 1", command=lambda: option_selected("Option 1", filepath))
    option1_button.pack(side=tk.LEFT, padx=5)
    
    option2_button = tk.Button(frame, text="Option 2", command=lambda: option_selected("Option 2", filepath))
    option2_button.pack(side=tk.LEFT, padx=5)
    
    # Store the frame reference to remove it when a new image is uploaded
    display_image.frame = frame

def option_selected(option, filepath):
    if option == "Option 1":
        text = simpledialog.askstring("Enter Text", "Enter some text:")
        if text:
            display_image_with_text(filepath, text)
    elif option == "Option 2":
        upload_second_image(filepath)

def display_image_with_text(filepath, text):
    global displayed_image
    draw = ImageDraw.Draw(displayed_image)
    font = ImageFont.load_default()  # You can choose any font you have on your system
    
    # Position to place the text
    position = (0, 0)
    
    # Drawing text on the image
    draw.text(position, text, fill="white", font=font)
    
    # Convert image to PhotoImage format
    img = ImageTk.PhotoImage(displayed_image)
    
    # Clear any previous image displayed
    if hasattr(display_image_with_text, 'label'):
        display_image_with_text.label.destroy()
    
    label = tk.Label(root, image=img)
    label.image = img  # Keep a reference to the image object to prevent garbage collection
    label.pack()
    
    # Store the label reference to remove it when a new image with text is displayed
    display_image_with_text.label = label
    
    # Add save and restart buttons
    add_save_and_restart_buttons()

def upload_second_image(first_filepath):
    second_filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if second_filepath:
        paste_second_image(first_filepath, second_filepath)

def paste_second_image(first_filepath, second_filepath):
    global displayed_image
    first_img = Image.open(first_filepath)
    second_img = Image.open(second_filepath)
    
    # Resize the second image to fit within the dimensions of the first image
    second_img.thumbnail(first_img.size)
    
    # Check if the second image has an alpha channel (transparency)
    if 'A' in second_img.getbands():
        # If the second image has transparency, paste it with transparency mask
        first_img.paste(second_img, (0, 0), second_img)
    else:
        # If the second image does not have transparency, convert it to RGBA mode
        second_img = second_img.convert('RGBA')
        first_img.paste(second_img, (0, 0), second_img)
    
    displayed_image = first_img
    
    # Convert image to PhotoImage format
    img = ImageTk.PhotoImage(displayed_image)
    
    # Clear any previous image displayed
    if hasattr(display_pasted_image, 'label'):
        display_pasted_image.label.destroy()
    
    label = tk.Label(root, image=img)
    label.image = img  # Keep a reference to the image object to prevent garbage collection
    label.pack()
    
    # Store the label reference to remove it when a new image is displayed
    display_pasted_image.label = label
    
    # Add save and restart buttons
    add_save_and_restart_buttons()

def add_save_and_restart_buttons():
    # Add save button
    save_button = tk.Button(root, text="Save Image", command=save_image)
    save_button.pack(pady=5)
    
    # Store the save button reference to remove it when a new image is displayed
    display_image_with_text.save_button = save_button
    
    # Add restart button
    restart_button = tk.Button(root, text="Restart", command=restart_program)
    restart_button.pack(pady=5)
    
    # Store the restart button reference to remove it when a new image is displayed
    display_image_with_text.restart_button = restart_button

def save_image():
    global displayed_image
    if displayed_image:
        save_filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if save_filepath:
            displayed_image.save(save_filepath)
            messagebox.showinfo("Image Saved", f"The image has been saved as {save_filepath}")

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

root = tk.Tk()
root.title("Image Uploader")

upload_button = tk.Button(root, text="Upload Image", command=open_file)
upload_button.pack(pady=20)

root.mainloop()


# from tkinter import *
# from tkinter import filedialog, messagebox
# from tkinter.filedialog import askopenfile
# from PIL import Image, ImageTk, ImageFont, ImageDraw

# # Creating a new window and configurations
# window = Tk()
# window.title("Watermark")
# window.minsize(width=500, height=500)

# img_path = ""
# watermark_path = ""

# def upload_img():
#     global img_path, img
#     fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
#     path = filedialog.askopenfilename(filetypes=fileTypes)
#     img_path = str(path)
#     img = Image.open(path)
#     img.thumbnail((300, 300))  # Resize the image to fit the label
#     img = ImageTk.PhotoImage(img)
#     imgLabel = Label(window, image=img)
#     canvas.itemconfig(canvas_image, image=img)
    

    
# def upload_watermark_img():
#     global watermark_path
#     fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
#     path = filedialog.askopenfilename(filetypes=fileTypes)
#     watermark_path = str(path)
    
# welcome_text = Label(window, text='Add Student Data with Photo', width=30, font=('times', 18, 'bold'))
# welcome_text.pack()

# upload_img_button = Button(window, text="Upload image", command=upload_img)
# upload_img_button.pack()

# canvas = Canvas(height=526, width=800)
# front_img = PhotoImage(file="Day-85\images\card_front.png")
# canvas_image = canvas.create_image(400, 263, image=front_img)

# canvas.pack()

# # upload_watermark_button = Button(window, text="Upload image", command=upload_watermark_img)
# # upload_watermark_button.pack()



# def add_img_watermark():
#     global image,watermark_img
#     # if not img_path or not watermark_path:
#     #     print("Please upload an image and a watermark image first.")
#     #     return
#     messagebox.askquestion("t")
#     # newWindow = Toplevel(window)
#     # newWindow.title("")
#     # upload_watermark_button = Button(newWindow, text="Upload image", command=upload_watermark_img)
#     # upload_watermark_button.pack()

#     # watermark_img = Image.open(watermark_path)
#     # watermark_img.show()
#     # watermark_img = PhotoImage(watermark_img)
#     # imgLabel = Label(newWindow,image=watermark_img)
#     # imgLabel.pack()
    
    
#     # newWindow.mainloop()
    
    
#     # img = Image.open(img_path)
#     # watermark_img = Image.open(watermark_path)
#     # img.paste(watermark_img,(0,0))
#     # img.show()
#     # image = ImageTk.PhotoImage(img)
#     # imgLabel = Label(image=image)
#     # imgLabel.pack()

# def add_text_watermark():
#     global image
#     if not img_path:
#         print("Please upload an image first.")
#         return
#     entry = Entry(window, width=30)
#     entry.insert(END, string="Priyanshu Naredi")
#     watermark_text = entry.get()
#     image = Image.open(img_path)
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.truetype("arial.ttf", 20)
#     draw.text((10, 10), text=watermark_text, font=font)  # Position the text watermark on the image
#     image.thumbnail((300, 300))  # Resize the image to fit the label
#     img = ImageTk.PhotoImage(image)
#     imgLabel = Label(window, image=img)
#     imgLabel.pack()

# # Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(window, text="Text As Watermark", value=1, variable=radio_state, command=add_text_watermark)
# radiobutton2 = Radiobutton(window, text="Image As Watermark", value=2, variable=radio_state, command=add_img_watermark)
# radiobutton1.pack()
# radiobutton2.pack()

# # if radiobutton2:
# #     upload_watermark_button = Button(window, text="Upload image", command=upload_watermark_img)
# #     upload_watermark_button.pack()

# window.mainloop()


# # from tkinter import *
# # from tkinter import filedialog
# # from tkinter.filedialog import askopenfile
# # from PIL import Image, ImageTk
# # from PIL import Image, ImageFont, ImageDraw

# # #Creating a new window and configurations
# # if __name__ == "__main__":
# #     window = Tk()
# #     window.title("Watermark")
# #     window.minsize(width=500, height=500)


# # def upload_img():
# #     global img_path,img
# #     fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
# #     path = filedialog.askopenfilename(filetypes=fileTypes)
# #     img_path = str(path)
# #     img = ImageTk.PhotoImage(file=path)
# #     imgLabel = Label(image=img)
# #     # imgLabel.grid(row=3,column=1)
# #     imgLabel.pack()

   
    
# # welcome_text = Label(text='Add Student Data with Photo',width=30,font=(('times', 18, 'bold')))  
# # # welcome_text.grid(row=1,column=1)
# # welcome_text.pack()


# # upload_img_button = Button(text="Upload image", command=upload_img)
# # # upload_img_button.grid(row=2,column=1)
# # upload_img_button.pack()

# # # img = ImageTk.PhotoImage(file=img_path)
# # # img_label = Label(image=img).pack()


# # def upload_watermark_img():
# #     global watermark_path,watermark_img
# #     fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
# #     path = filedialog.askopenfilename(filetypes=fileTypes)
# #     watermark_path = str(path)
# #     watermark_img = ImageTk.PhotoImage(file=path)
# #     imgLabel = Label(image=watermark_img)
# #     # imgLabel.grid(row=3,column=1)
# #     imgLabel.pack()

# # #Radiobutton
# # def add_img_watermark():
# #     upload_wimg_button = Button(text="Upload image", command=upload_watermark_img)
# # # upload_img_button.grid(row=2,column=1)
# #     upload_wimg_button.pack()
# #     print(watermark_path)

    
    
    

    
# # def add_text_watermark():
# #     entry = Entry(width=30)
# #     entry.insert(END, string="Priyanshu Naredi")
# #     print(entry.get())
# #     image = Image.open(img_path)
# #     draw = ImageDraw.Draw(image)
# #     font = ImageFont.truetype("arial.ttf", 10)
# #     draw.text((0,0),text=entry.get(),font=font)
# #     image.show()
# #     image.save('D:\Python\Day-85\images\w1.jpg')
# #     entry.pack()


# # #Variable to hold on to which radio button value is checked.
# # radio_state = IntVar()
# # radiobutton1 = Radiobutton(text="Text As Watermark", value=1, variable=radio_state, command=add_text_watermark)
# # radiobutton2 = Radiobutton(text="Image As Watermark", value=2, variable=radio_state, command=add_img_watermark)
# # radiobutton1.pack()
# # radiobutton2.pack()


# # # img = Image.open("Day-85/base.jpg")
# # # test = ImageTk.PhotoImage(image=img)
# # # label = Label(image=test)
# # # label.image = test
# # # label.place(x=250,y=250)

# # # img = ImageTk.PhotoImage(file='Day-85/base.jpg')
# # # imgLabel = Label(image=img)
# # # imgLabel.pack()





# # window.mainloop()