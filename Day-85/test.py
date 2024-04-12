# import tkinter as tk
# from tkinter import filedialog, messagebox, simpledialog, colorchooser
# from PIL import Image, ImageTk, ImageDraw, ImageFont
# import sys
# import os

# def open_file():
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if filepath:
#         display_image(filepath)

# def display_image(filepath):
#     global displayed_image
#     displayed_image = Image.open(filepath)
#     displayed_image.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
#     if hasattr(display_image, 'frame'):
#         display_image.frame.destroy()
#     if hasattr(display_image, 'save_button'):
#         display_image.save_button.destroy()
#     if hasattr(display_image, 'restart_button'):
#         display_image.restart_button.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is uploaded
#     display_image.label = label
    
#     # Add frame with options
#     frame = tk.Frame(root)
#     frame.pack(pady=10)
    
#     option1_button = tk.Button(frame, text="Add Watermark", command=lambda: option_selected("Add Watermark", filepath))
#     option1_button.pack(side=tk.LEFT, padx=5)
    
#     option2_button = tk.Button(frame, text="Add Image Watermark", command=lambda: option_selected("Add Image Watermark", filepath))
#     option2_button.pack(side=tk.LEFT, padx=5)
    
#     # Store the frame reference to remove it when a new image is uploaded
#     display_image.frame = frame

# def option_selected(option, filepath):
#     if option == "Add Watermark":
#         watermark_dialog(filepath)
#     elif option == "Add Image Watermark":
#         upload_second_image(filepath)
    
#     # Destroy the upload button and frame with options
#     upload_button.destroy()
#     if hasattr(display_image, 'frame'):
#         display_image.frame.destroy()

# def watermark_dialog(filepath):
#     global watermark_text, font_size_var, font_color
    
#     dialog = tk.Toplevel(root)
#     dialog.title("Watermark Options")
    
#     # Text input
#     text_label = tk.Label(dialog, text="Enter Text:")
#     text_label.grid(row=0, column=0, padx=5, pady=5)
    
#     watermark_text_entry = tk.Entry(dialog)
#     watermark_text_entry.grid(row=0, column=1, padx=5, pady=5)
    
#     # Font size entry
#     font_size_label = tk.Label(dialog, text="Font Size:")
#     font_size_label.grid(row=1, column=0, padx=5, pady=5)
    
#     font_size_var = tk.StringVar(dialog, value="12")  # Default font size
#     font_size_entry = tk.Entry(dialog, textvariable=font_size_var, width=10)
#     font_size_entry.grid(row=1, column=1, padx=5, pady=5)
    
#     # Font color selection
#     font_color_label = tk.Label(dialog, text="Font Color:")
#     font_color_label.grid(row=2, column=0, padx=5, pady=5)
    
#     font_color_button = tk.Button(dialog, text="Select Color", command=lambda: select_font_color(dialog))
#     font_color_button.grid(row=2, column=1, padx=5, pady=5)
    
#     # Apply button
#     apply_button = tk.Button(dialog, text="Apply", command=lambda: apply_watermark(filepath, watermark_text_entry.get(), font_size_var.get(), dialog))
#     apply_button.grid(row=3, column=0, columnspan=2, pady=10)
    
#     # Cancel button
#     cancel_button = tk.Button(dialog, text="Cancel", command=dialog.destroy)
#     cancel_button.grid(row=4, column=0, columnspan=2, pady=10)

# def select_font_color(dialog):
#     global font_color
#     color = colorchooser.askcolor(title="Select Font Color")
#     if color:
#         font_color = color[1]  # Extract the hex color value
#         dialog.lift()  # Bring the dialog window to the front after color selection

# def apply_watermark(filepath, text, font_size, dialog):
#     font_size = int(font_size)
#     if not hasattr(select_font_color, 'font_color'):
#         messagebox.showerror("Error", "Please select a font color.")
#         return
    
#     font_color = select_font_color.font_color
    
#     # Open the image
#     image = Image.open(filepath)
    
#     # Draw watermark text on the image
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.truetype("arial.ttf", font_size)  # You can specify any font you like
#     draw.text((10, 10), text, fill=font_color, font=font)
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
    
#     # Display the image with the watermark
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image with text is displayed
#     display_image.label = label
    
#     # Add save and restart buttons
#     add_save_and_restart_buttons()
    
#     # Close the dialog window
#     dialog.destroy()

# def upload_second_image(first_filepath):
#     second_filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if second_filepath:
#         paste_second_image(first_filepath, second_filepath)

# def paste_second_image(first_filepath, second_filepath):
#     global displayed_image
#     first_img = Image.open(first_filepath)
#     second_img = Image.open(second_filepath)
    
#     # Resize the second image to fit within the dimensions of the first image
#     second_img.thumbnail(first_img.size)
    
#     # Check if the second image has an alpha channel (transparency)
#     if 'A' in second_img.getbands():
#         # If the second image has transparency, paste it with transparency mask
#         first_img.paste(second_img, (0, 0), second_img)
#     else:
#         # If the second image does not have transparency, convert it to RGBA mode
#         second_img = second_img.convert('RGBA')
#         first_img.paste(second_img, (0, 0), second_img)
    
#     displayed_image = first_img
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is displayed
#     display_image.label = label
    
#     # Add save and restart buttons
#     add_save_and_restart_buttons()

# def add_save_and_restart_buttons():
#     # Add save button
#     save_button = tk.Button(root, text="Save Image", command=save_image)
#     save_button.pack(pady=5)
    
#     # Store the save button reference to remove it when a new image is displayed
#     display_image.save_button = save_button
    
#     # Add restart button
#     restart_button = tk.Button(root, text="Restart", command=restart_program)
#     restart_button.pack(pady=5)
    
#     # Store the restart button reference to remove it when a new image is displayed
#     display_image.restart_button = restart_button

# def save_image():
#     global displayed_image
#     if displayed_image:
#         save_filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
#         if save_filepath:
#             displayed_image.save(save_filepath)
#             messagebox.showinfo("Image Saved", f"The image has been saved as {save_filepath}")

# def restart_program():
#     python = sys.executable
#     os.execl(python, python, *sys.argv)

# root = tk.Tk()
# root.title("Image Uploader")

# upload_button = tk.Button(root, text="Upload Image", command=open_file)
# upload_button.pack(pady=20)

# root.mainloop()

# ---------
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, colorchooser
from PIL import Image, ImageTk, ImageDraw, ImageFont
import sys
import os

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
    
    option1_button = tk.Button(frame, text="Add Watermark", command=lambda: option_selected("Add Watermark", filepath))
    option1_button.pack(side=tk.LEFT, padx=5)
    
    option2_button = tk.Button(frame, text="Add Image Watermark", command=lambda: option_selected("Add Image Watermark", filepath))
    option2_button.pack(side=tk.LEFT, padx=5)
    
    # Store the frame reference to remove it when a new image is uploaded
    display_image.frame = frame

def option_selected(option, filepath):
    if option == "Add Watermark":
        watermark_dialog(filepath)
    elif option == "Add Image Watermark":
        upload_second_image(filepath)
    
    # Destroy the upload button and frame with options
    upload_button.destroy()
    if hasattr(display_image, 'frame'):
        display_image.frame.destroy()

def watermark_dialog(filepath):
    global watermark_text, font_size_var, font_color
    
    dialog = tk.Toplevel(root)
    dialog.title("Watermark Options")
    
    # Text input
    text_label = tk.Label(dialog, text="Enter Text:")
    text_label.grid(row=0, column=0, padx=5, pady=5)
    
    watermark_text_entry = tk.Entry(dialog)
    watermark_text_entry.grid(row=0, column=1, padx=5, pady=5)
    
    # Font size entry
    font_size_label = tk.Label(dialog, text="Font Size:")
    font_size_label.grid(row=1, column=0, padx=5, pady=5)
    
    font_size_var = tk.StringVar(dialog, value="12")  # Default font size
    font_size_entry = tk.Entry(dialog, textvariable=font_size_var, width=10)
    font_size_entry.grid(row=1, column=1, padx=5, pady=5)
    
    # Font color selection
    font_color_label = tk.Label(dialog, text="Font Color:")
    font_color_label.grid(row=2, column=0, padx=5, pady=5)
    
    font_color_button = tk.Button(dialog, text="Select Color", command=lambda: select_font_color(dialog))
    font_color_button.grid(row=2, column=1, padx=5, pady=5)

    
    # Apply button
    apply_button = tk.Button(dialog, text="Apply", command=lambda: apply_watermark(filepath, watermark_text_entry.get(), font_size_var.get(), font_color, dialog))
    apply_button.grid(row=3, column=0, columnspan=2, pady=10)
    
    # Cancel button
    cancel_button = tk.Button(dialog, text="Cancel", command=dialog.destroy)
    cancel_button.grid(row=4, column=0, columnspan=2, pady=10)

def select_font_color(dialog):
    global font_color
    color = colorchooser.askcolor(title="Select Font Color")
    if color:
        font_color = color[1]  # Extract the hex color value
        dialog.lift()  # Bring the dialog window to the front after color selection

def apply_watermark(filepath, text, font_size, color, dialog):
    font_size = int(font_size)
    
    # Open the image
    image = Image.open(filepath)
    
    try:
        # Draw watermark text on the image
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", font_size)  # You can specify any font you like
        draw.text((10, 10), text, fill=color, font=font)
    except NameError:
        messagebox.showerror("Error", "Please select a font color.")
        return
    
    # Convert image to PhotoImage format
    img = ImageTk.PhotoImage(image)
    
    # Clear any previous image displayed
    if hasattr(display_image, 'label'):
        display_image.label.destroy()
    
    # Display the image with the watermark
    label = tk.Label(root, image=img)
    label.image = img  # Keep a reference to the image object to prevent garbage collection
    label.pack()
    
    # Store the label reference to remove it when a new image with text is displayed
    display_image.label = label
    
    # Add save and restart buttons
    add_save_and_restart_buttons()
    
    # Close the dialog window
    dialog.destroy()

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
    if hasattr(display_image, 'label'):
        display_image.label.destroy()
    
    label = tk.Label(root, image=img)
    label.image = img  # Keep a reference to the image object to prevent garbage collection
    label.pack()
    
    # Store the label reference to remove it when a new image is displayed
    display_image.label = label
    
    # Add save and restart buttons
    add_save_and_restart_buttons()

def add_save_and_restart_buttons():
    # Add save button
    save_button = tk.Button(root, text="Save Image", command=save_image)
    save_button.pack(pady=5)
    
    # Store the save button reference to remove it when a new image is displayed
    display_image.save_button = save_button
    
    # Add restart button
    restart_button = tk.Button(root, text="Restart", command=restart_program)
    restart_button.pack(pady=5)
    
    # Store the restart button reference to remove it when a new image is displayed
    display_image.restart_button = restart_button

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
#------------
# import tkinter as tk
# from tkinter import filedialog, messagebox, simpledialog, colorchooser
# from PIL import Image, ImageTk, ImageDraw, ImageFont
# import sys
# import os

# def open_file():
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if filepath:
#         display_image(filepath)

# def display_image(filepath):
#     global displayed_image
#     displayed_image = Image.open(filepath)
#     displayed_image.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
#     if hasattr(display_image, 'frame'):
#         display_image.frame.destroy()
#     if hasattr(display_image, 'save_button'):
#         display_image.save_button.destroy()
#     if hasattr(display_image, 'restart_button'):
#         display_image.restart_button.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is uploaded
#     display_image.label = label
    
#     # Add frame with options
#     frame = tk.Frame(root)
#     frame.pack(pady=10)
    
#     option1_button = tk.Button(frame, text="Add Watermark", command=lambda: option_selected("Add Watermark", filepath))
#     option1_button.pack(side=tk.LEFT, padx=5)
    
#     option2_button = tk.Button(frame, text="Add Image Watermark", command=lambda: option_selected("Add Image Watermark", filepath))
#     option2_button.pack(side=tk.LEFT, padx=5)
    
#     # Store the frame reference to remove it when a new image is uploaded
#     display_image.frame = frame

# def option_selected(option, filepath):
#     if option == "Add Watermark":
#         watermark_dialog(filepath)
#     elif option == "Add Image Watermark":
#         upload_second_image(filepath)
    
#     # Destroy the upload button and frame with options
#     upload_button.destroy()
#     if hasattr(display_image, 'frame'):
#         display_image.frame.destroy()

# def watermark_dialog(filepath):
#     global watermark_text, font_size_var, font_color
    
#     dialog = tk.Toplevel(root)
#     dialog.title("Watermark Options")
    
#     # Text input
#     text_label = tk.Label(dialog, text="Enter Text:")
#     text_label.grid(row=0, column=0, padx=5, pady=5)
    
#     watermark_text_entry = tk.Entry(dialog)
#     watermark_text_entry.grid(row=0, column=1, padx=5, pady=5)
    
#     # Font size entry
#     font_size_label = tk.Label(dialog, text="Font Size:")
#     font_size_label.grid(row=1, column=0, padx=5, pady=5)
    
#     font_size_var = tk.StringVar(dialog, value="12")  # Default font size
#     font_size_entry = tk.Entry(dialog, textvariable=font_size_var, width=10)
#     font_size_entry.grid(row=1, column=1, padx=5, pady=5)
    
#     # Font color selection
#     font_color_label = tk.Label(dialog, text="Font Color:")
#     font_color_label.grid(row=2, column=0, padx=5, pady=5)
    
#     font_color_button = tk.Button(dialog, text="Select Color", command=lambda: select_font_color(dialog))
#     font_color_button.grid(row=2, column=1, padx=5, pady=5)
    
#     # Apply button
#     apply_button = tk.Button(dialog, text="Apply", command=lambda: apply_watermark(filepath, watermark_text_entry.get(), font_size_var.get(), font_color, dialog))
#     apply_button.grid(row=3, column=0, columnspan=2, pady=10)
    
#     # Cancel button
#     cancel_button = tk.Button(dialog, text="Cancel", command=dialog.destroy)
#     cancel_button.grid(row=4, column=0, columnspan=2, pady=10)

# def select_font_color(dialog):
#     global font_color
#     color = colorchooser.askcolor(title="Select Font Color")
#     if color:
#         font_color = color[1]  # Extract the hex color value
#         dialog.lift()  # Bring the dialog window to the front after color selection

# def apply_watermark(filepath, text, font_size, color, dialog):
#     font_size = int(font_size)
    
#     # Open the image
#     image = Image.open(filepath)
    
#     # Draw watermark text on the image
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.truetype("arial.ttf", font_size)  # You can specify any font you like
#     draw.text((10, 10), text, fill=color, font=font)
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
    
#     # Display the image with the watermark
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image with text is displayed
#     display_image.label = label
    
#     # Add save and restart buttons
#     add_save_and_restart_buttons()
    
#     # Close the dialog window
#     dialog.destroy()

# def upload_second_image(first_filepath):
#     second_filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if second_filepath:
#         paste_second_image(first_filepath, second_filepath)

# def paste_second_image(first_filepath, second_filepath):
#     global displayed_image
#     first_img = Image.open(first_filepath)
#     second_img = Image.open(second_filepath)
    
#     # Resize the second image to fit within the dimensions of the first image
#     second_img.thumbnail(first_img.size)
    
#     # Check if the second image has an alpha channel (transparency)
#     if 'A' in second_img.getbands():
#         # If the second image has transparency, paste it with transparency mask
#         first_img.paste(second_img, (0, 0), second_img)
#     else:
#         # If the second image does not have transparency, convert it to RGBA mode
#         second_img = second_img.convert('RGBA')
#         first_img.paste(second_img, (0, 0), second_img)
    
#     displayed_image = first_img
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is displayed
#     display_image.label = label
    
#     # Add save and restart buttons
#     add_save_and_restart_buttons()

# def add_save_and_restart_buttons():
#     # Add save button
#     save_button = tk.Button(root, text="Save Image", command=save_image)
#     save_button.pack(pady=5)
    
#     # Store the save button reference to remove it when a new image is displayed
#     display_image.save_button = save_button
    
#     # Add restart button
#     restart_button = tk.Button(root, text="Restart", command=restart_program)
#     restart_button.pack(pady=5)
    
#     # Store the restart button reference to remove it when a new image is displayed
#     display_image.restart_button = restart_button

# def save_image():
#     global displayed_image
#     if displayed_image:
#         save_filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
#         if save_filepath:
#             displayed_image.save(save_filepath)
#             messagebox.showinfo("Image Saved", f"The image has been saved as {save_filepath}")

# def restart_program():
#     python = sys.executable
#     os.execl(python, python, *sys.argv)

# root = tk.Tk()
# root.title("Image Uploader")

# upload_button = tk.Button(root, text="Upload Image", command=open_file)
# upload_button.pack(pady=20)

# root.mainloop()



# ----almost
# import tkinter as tk
# from tkinter import filedialog, messagebox, simpledialog, colorchooser
# from PIL import Image, ImageTk, ImageDraw, ImageFont
# import sys
# import os

# def open_file():
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if filepath:
#         display_image(filepath)

# def display_image(filepath):
#     global displayed_image
#     displayed_image = Image.open(filepath)
#     displayed_image.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
#     if hasattr(display_image, 'frame'):
#         display_image.frame.destroy()
#     if hasattr(display_image, 'save_button'):
#         display_image.save_button.destroy()
#     if hasattr(display_image, 'restart_button'):
#         display_image.restart_button.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is uploaded
#     display_image.label = label
    
#     # Add frame with options
#     frame = tk.Frame(root)
#     frame.pack(pady=10)
    
#     option1_button = tk.Button(frame, text="Add Watermark", command=lambda: option_selected("Add Watermark", filepath))
#     option1_button.pack(side=tk.LEFT, padx=5)
    
#     option2_button = tk.Button(frame, text="Add Image Watermark", command=lambda: option_selected("Add Image Watermark", filepath))
#     option2_button.pack(side=tk.LEFT, padx=5)
    
#     # Store the frame reference to remove it when a new image is uploaded
#     display_image.frame = frame

# def option_selected(option, filepath):
#     if option == "Add Watermark":
#         watermark_dialog(filepath)
#     elif option == "Add Image Watermark":
#         upload_second_image(filepath)

# def watermark_dialog(filepath):
#     global watermark_text, font_size_var, font_color
    
#     dialog = tk.Toplevel(root)
#     dialog.title("Watermark Options")
    
#     # Text input
#     text_label = tk.Label(dialog, text="Enter Text:")
#     text_label.grid(row=0, column=0, padx=5, pady=5)
    
#     watermark_text_entry = tk.Entry(dialog)
#     watermark_text_entry.grid(row=0, column=1, padx=5, pady=5)
    
#     # Font size entry
#     font_size_label = tk.Label(dialog, text="Font Size:")
#     font_size_label.grid(row=1, column=0, padx=5, pady=5)
    
#     font_size_var = tk.StringVar(dialog, value="12")  # Default font size
#     font_size_entry = tk.Entry(dialog, textvariable=font_size_var, width=10)
#     font_size_entry.grid(row=1, column=1, padx=5, pady=5)
    
#     # Font color selection
#     font_color_label = tk.Label(dialog, text="Font Color:")
#     font_color_label.grid(row=2, column=0, padx=5, pady=5)
    
#     font_color_button = tk.Button(dialog, text="Select Color", command=lambda: select_font_color(dialog))
#     font_color_button.grid(row=2, column=1, padx=5, pady=5)
    
#     # Apply button
#     apply_button = tk.Button(dialog, text="Apply", command=lambda: apply_watermark(filepath, watermark_text_entry.get(), font_size_var.get(), font_color, dialog))
#     apply_button.grid(row=3, column=0, columnspan=2, pady=10)
    
#     # Cancel button
#     cancel_button = tk.Button(dialog, text="Cancel", command=dialog.destroy)
#     cancel_button.grid(row=4, column=0, columnspan=2, pady=10)

# def select_font_color(dialog):
#     global font_color
#     color = colorchooser.askcolor(title="Select Font Color")
#     if color:
#         font_color = color[1]  # Extract the hex color value
#         dialog.lift()  # Bring the dialog window to the front after color selection

# def apply_watermark(filepath, text, font_size, color, dialog):
#     font_size = int(font_size)
    
#     # Open the image
#     image = Image.open(filepath)
    
#     # Draw watermark text on the image
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.truetype("arial.ttf", font_size)  # You can specify any font you like
#     draw.text((10, 10), text, fill=color, font=font)
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
    
#     # Display the image with the watermark
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image with text is displayed
#     display_image.label = label
    
#     # Add save and restart buttons
#     add_save_and_restart_buttons()
    
#     # Close the dialog window
#     dialog.destroy()

# def upload_second_image(first_filepath):
#     second_filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if second_filepath:
#         paste_second_image(first_filepath, second_filepath)

# def paste_second_image(first_filepath, second_filepath):
#     global displayed_image
#     first_img = Image.open(first_filepath)
#     second_img = Image.open(second_filepath)
    
#     # Resize the second image to fit within the dimensions of the first image
#     second_img.thumbnail(first_img.size)
    
#     # Check if the second image has an alpha channel (transparency)
#     if 'A' in second_img.getbands():
#         # If the second image has transparency, paste it with transparency mask
#         first_img.paste(second_img, (0, 0), second_img)
#     else:
#         # If the second image does not have transparency, convert it to RGBA mode
#         second_img = second_img.convert('RGBA')
#         first_img.paste(second_img, (0, 0), second_img)
    
#     displayed_image = first_img
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is displayed
#     display_image.label = label
    
#     # Add save and restart buttons
#     add_save_and_restart_buttons()

# def add_save_and_restart_buttons():
#     # Add save button
#     save_button = tk.Button(root, text="Save Image", command=save_image)
#     save_button.pack(pady=5)
    
#     # Store the save button reference to remove it when a new image is displayed
#     display_image.save_button = save_button
    
#     # Add restart button
#     restart_button = tk.Button(root, text="Restart", command=restart_program)
#     restart_button.pack(pady=5)
    
#     # Store the restart button reference to remove it when a new image is displayed
#     display_image.restart_button = restart_button

# def save_image():
#     global displayed_image
#     if displayed_image:
#         save_filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
#         if save_filepath:
#             displayed_image.save(save_filepath)
#             messagebox.showinfo("Image Saved", f"The image has been saved as {save_filepath}")

# def restart_program():
#     python = sys.executable
#     os.execl(python, python, *sys.argv)

# root = tk.Tk()
# root.title("Image Uploader")

# upload_button = tk.Button(root, text="Upload Image", command=open_file)
# upload_button.pack(pady=20)

# root.mainloop()

#---------
# import tkinter as tk
# from tkinter import filedialog, messagebox, simpledialog, colorchooser
# from PIL import Image, ImageTk, ImageDraw, ImageFont
# import sys
# import os

# def open_file():
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if filepath:
#         display_image(filepath)

# def display_image(filepath):
#     global displayed_image
#     displayed_image = Image.open(filepath)
#     displayed_image.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
#     if hasattr(display_image, 'frame'):
#         display_image.frame.destroy()
#     if hasattr(display_image, 'save_button'):
#         display_image.save_button.destroy()
#     if hasattr(display_image, 'restart_button'):
#         display_image.restart_button.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is uploaded
#     display_image.label = label
    
#     # Add frame with options
#     frame = tk.Frame(root)
#     frame.pack(pady=10)
    
#     option1_button = tk.Button(frame, text="Add Watermark", command=lambda: option_selected("Add Watermark", filepath))
#     option1_button.pack(side=tk.LEFT, padx=5)
    
#     option2_button = tk.Button(frame, text="Add Image Watermark", command=lambda: option_selected("Add Image Watermark", filepath))
#     option2_button.pack(side=tk.LEFT, padx=5)
    
#     # Store the frame reference to remove it when a new image is uploaded
#     display_image.frame = frame

# def option_selected(option, filepath):
#     if option == "Add Watermark":
#         watermark_dialog(filepath)
#     elif option == "Add Image Watermark":
#         upload_second_image(filepath)

# def watermark_dialog(filepath):
#     global watermark_text, font_size_var, font_color
    
#     dialog = tk.Toplevel(root)
#     dialog.title("Watermark Options")
    
#     # Text input
#     text_label = tk.Label(dialog, text="Enter Text:")
#     text_label.grid(row=0, column=0, padx=5, pady=5)
    
#     watermark_text_entry = tk.Entry(dialog)
#     watermark_text_entry.grid(row=0, column=1, padx=5, pady=5)
    
#     # Font size entry
#     font_size_label = tk.Label(dialog, text="Font Size:")
#     font_size_label.grid(row=1, column=0, padx=5, pady=5)
    
#     font_size_var = tk.StringVar(dialog, value="12")  # Default font size
#     font_size_entry = tk.Entry(dialog, textvariable=font_size_var, width=10)
#     font_size_entry.grid(row=1, column=1, padx=5, pady=5)
    
#     # Font color selection
#     font_color_label = tk.Label(dialog, text="Font Color:")
#     font_color_label.grid(row=2, column=0, padx=5, pady=5)
    
#     font_color_button = tk.Button(dialog, text="Select Color", command=lambda: select_font_color(dialog))
#     font_color_button.grid(row=2, column=1, padx=5, pady=5)
    
#     # Apply button
#     apply_button = tk.Button(dialog, text="Apply", command=lambda: apply_watermark(filepath, watermark_text_entry.get(), font_size_var.get(), font_color))
#     apply_button.grid(row=3, column=0, columnspan=2, pady=10)
    
#     # Cancel button
#     cancel_button = tk.Button(dialog, text="Cancel", command=dialog.destroy)
#     cancel_button.grid(row=4, column=0, columnspan=2, pady=10)

# def select_font_color(dialog):
#     global font_color
#     color = colorchooser.askcolor(title="Select Font Color")
#     if color:
#         font_color = color[1]  # Extract the hex color value
#         dialog.lift()  # Bring the dialog window to the front after color selection

# def apply_watermark(filepath, text, font_size, color):
#     font_size = int(font_size)
    
#     # Open the image
#     image = Image.open(filepath)
    
#     # Draw watermark text on the image
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.truetype("arial.ttf", font_size)  # You can specify any font you like
#     draw.text((10, 10), text, fill=color, font=font)
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
    
#     # Display the image with the watermark
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image with text is displayed
#     display_image.label = label
    
#     # Add save and restart buttons
#     add_save_and_restart_buttons()

# def upload_second_image(first_filepath):
#     second_filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if second_filepath:
#         paste_second_image(first_filepath, second_filepath)

# def paste_second_image(first_filepath, second_filepath):
#     global displayed_image
#     first_img = Image.open(first_filepath)
#     second_img = Image.open(second_filepath)
    
#     # Resize the second image to fit within the dimensions of the first image
#     second_img.thumbnail(first_img.size)
    
#     # Check if the second image has an alpha channel (transparency)
#     if 'A' in second_img.getbands():
#         # If the second image has transparency, paste it with transparency mask
#         first_img.paste(second_img, (0, 0), second_img)
#     else:
#         # If the second image does not have transparency, convert it to RGBA mode
#         second_img = second_img.convert('RGBA')
#         first_img.paste(second_img, (0, 0), second_img)
    
#     displayed_image = first_img
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is displayed
#     display_image.label = label
    
#     # Add save and restart buttons
#     add_save_and_restart_buttons()

# def add_save_and_restart_buttons():
#     # Add save button
#     save_button = tk.Button(root, text="Save Image", command=save_image)
#     save_button.pack(pady=5)
    
#     # Store the save button reference to remove it when a new image is displayed
#     display_image.save_button = save_button
    
#     # Add restart button
#     restart_button = tk.Button(root, text="Restart", command=restart_program)
#     restart_button.pack(pady=5)
    
#     # Store the restart button reference to remove it when a new image is displayed
#     display_image.restart_button = restart_button

# def save_image():
#     global displayed_image
#     if displayed_image:
#         save_filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
#         if save_filepath:
#             displayed_image.save(save_filepath)
#             messagebox.showinfo("Image Saved", f"The image has been saved as {save_filepath}")

# def restart_program():
#     python = sys.executable
#     os.execl(python, python, *sys.argv)

# root = tk.Tk()
# root.title("Image Uploader")

# upload_button = tk.Button(root, text="Upload Image", command=open_file)
# upload_button.pack(pady=20)

# root.mainloop()


# ---Working---
# import tkinter as tk
# from tkinter import filedialog, messagebox, simpledialog, colorchooser
# from PIL import Image, ImageTk, ImageDraw, ImageFont
# import sys
# import os

# def open_file():
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if filepath:
#         display_image(filepath)

# def display_image(filepath):
#     global displayed_image
#     displayed_image = Image.open(filepath)
#     displayed_image.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
#     if hasattr(display_image, 'frame'):
#         display_image.frame.destroy()
#     if hasattr(display_image, 'save_button'):
#         display_image.save_button.destroy()
#     if hasattr(display_image, 'restart_button'):
#         display_image.restart_button.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is uploaded
#     display_image.label = label
    
#     # Add frame with options
#     frame = tk.Frame(root)
#     frame.pack(pady=10)
    
#     option1_button = tk.Button(frame, text="Add Text Watermark", command=lambda: option_selected("Add Text Watermark", filepath))
#     option1_button.pack(side=tk.LEFT, padx=5)
    
#     option2_button = tk.Button(frame, text="Add Image Watermark", command=lambda: option_selected("Add Image Watermark", filepath))
#     option2_button.pack(side=tk.LEFT, padx=5)
    
#     # Store the frame reference to remove it when a new image is uploaded
#     display_image.frame = frame

# def option_selected(option, filepath):
#     if option == "Add Text Watermark":
#         text_watermark_dialog(filepath)
#     elif option == "Add Image Watermark":
#         upload_second_image(filepath)

# def text_watermark_dialog(filepath):
#     global watermark_text, font_size_var, font_color
    
#     watermark_text = simpledialog.askstring("Enter Text", "Enter text for watermark:")
#     if watermark_text:
#         font_size_var = tk.StringVar(root, value="12")  # Default font size
#         font_color = "white"  # Default font color
        
#         # Create dialog window for additional options
#         dialog = tk.Toplevel(root)
#         dialog.title("Text Watermark Options")
        
#         # Font size entry
#         font_size_label = tk.Label(dialog, text="Font Size:")
#         font_size_label.grid(row=0, column=0, padx=5, pady=5)
        
#         font_size_entry = tk.Entry(dialog, textvariable=font_size_var, width=10)
#         font_size_entry.grid(row=0, column=1, padx=5, pady=5)
        
#         # Font color selection
#         font_color_label = tk.Label(dialog, text="Font Color:")
#         font_color_label.grid(row=1, column=0, padx=5, pady=5)
        
#         font_color_button = tk.Button(dialog, text="Select Color", command=select_font_color)
#         font_color_button.grid(row=1, column=1, padx=5, pady=5)
        
#         # Apply button
#         apply_button = tk.Button(dialog, text="Apply", command=lambda: apply_text_watermark(filepath))
#         apply_button.grid(row=2, column=0, columnspan=2, pady=10)
        
#         # Cancel button
#         cancel_button = tk.Button(dialog, text="Cancel", command=dialog.destroy)
#         cancel_button.grid(row=3, column=0, columnspan=2, pady=10)

# def select_font_color():
#     global font_color
#     color = colorchooser.askcolor(title="Select Font Color")
#     if color:
#         font_color = color[1]  # Extract the hex color value

# def apply_text_watermark(filepath):
#     global watermark_text, font_size_var, font_color
    
#     font_size = int(font_size_var.get())
    
#     # Open the image
#     image = Image.open(filepath)
    
#     # Draw watermark text on the image
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.truetype("arial.ttf", font_size)  # You can specify any font you like
#     draw.text((10, 10), watermark_text, fill=font_color, font=font)
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
    
#     # Display the image with the watermark
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image with text is displayed
#     display_image.label = label
    
#     # Add save and restart buttons
#     add_save_and_restart_buttons()

# def upload_second_image(first_filepath):
#     second_filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if second_filepath:
#         paste_second_image(first_filepath, second_filepath)

# def paste_second_image(first_filepath, second_filepath):
#     global displayed_image
#     first_img = Image.open(first_filepath)
#     second_img = Image.open(second_filepath)
    
#     # Resize the second image to fit within the dimensions of the first image
#     second_img.thumbnail(first_img.size)
    
#     # Check if the second image has an alpha channel (transparency)
#     if 'A' in second_img.getbands():
#         # If the second image has transparency, paste it with transparency mask
#         first_img.paste(second_img, (0, 0), second_img)
#     else:
#         # If the second image does not have transparency, convert it to RGBA mode
#         second_img = second_img.convert('RGBA')
#         first_img.paste(second_img, (0, 0), second_img)
    
#     displayed_image = first_img
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is displayed
#     display_image.label = label
    
#     # Add save and restart buttons
#     add_save_and_restart_buttons()

# def add_save_and_restart_buttons():
#     # Add save button
#     save_button = tk.Button(root, text="Save Image", command=save_image)
#     save_button.pack(pady=5)
    
#     # Store the save button reference to remove it when a new image is displayed
#     display_image.save_button = save_button
    
#     # Add restart button
#     restart_button = tk.Button(root, text="Restart", command=restart_program)
#     restart_button.pack(pady=5)
    
#     # Store the restart button reference to remove it when a new image is displayed
#     display_image.restart_button = restart_button

# def save_image():
#     global displayed_image
#     if displayed_image:
#         save_filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
#         if save_filepath:
#             displayed_image.save(save_filepath)
#             messagebox.showinfo("Image Saved", f"The image has been saved as {save_filepath}")

# def restart_program():
#     python = sys.executable
#     os.execl(python, python, *sys.argv)

# root = tk.Tk()
# root.title("Image Uploader")

# upload_button = tk.Button(root, text="Upload Image", command=open_file)
# upload_button.pack(pady=20)

# root.mainloop()

# -----------
# import tkinter as tk
# from tkinter import filedialog, messagebox, simpledialog, colorchooser
# from PIL import Image, ImageTk, ImageDraw, ImageFont
# import sys
# import os

# def open_file():
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if filepath:
#         display_image(filepath)

# def display_image(filepath):
#     global displayed_image
#     displayed_image = Image.open(filepath)
#     displayed_image.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
#     if hasattr(display_image, 'frame'):
#         display_image.frame.destroy()
#     if hasattr(display_image, 'save_button'):
#         display_image.save_button.destroy()
#     if hasattr(display_image, 'restart_button'):
#         display_image.restart_button.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is uploaded
#     display_image.label = label
    
#     # Add frame with options
#     frame = tk.Frame(root)
#     frame.pack(pady=10)
    
#     option1_button = tk.Button(frame, text="Add Text Watermark", command=lambda: option_selected("Add Text Watermark", filepath))
#     option1_button.pack(side=tk.LEFT, padx=5)
    
#     option2_button = tk.Button(frame, text="Add Image Watermark", command=lambda: option_selected("Add Image Watermark", filepath))
#     option2_button.pack(side=tk.LEFT, padx=5)
    
#     # Store the frame reference to remove it when a new image is uploaded
#     display_image.frame = frame

# def option_selected(option, filepath):
#     if option == "Add Text Watermark":
#         text_watermark_dialog(filepath)
#     elif option == "Add Image Watermark":
#         upload_second_image(filepath)

# def text_watermark_dialog(filepath):
#     global watermark_text, font_size_var, font_color
    
#     watermark_text = simpledialog.askstring("Enter Text", "Enter text for watermark:")
#     if watermark_text:
#         font_size_var = tk.StringVar(root, value="12")  # Default font size
#         font_color = "white"  # Default font color
        
#         # Create dialog window for additional options
#         dialog = tk.Toplevel(root)
#         dialog.title("Text Watermark Options")
        
#         # Font size entry
#         font_size_label = tk.Label(dialog, text="Font Size:")
#         font_size_label.grid(row=0, column=0, padx=5, pady=5)
        
#         font_size_entry = tk.Entry(dialog, textvariable=font_size_var, width=10)
#         font_size_entry.grid(row=0, column=1, padx=5, pady=5)
        
#         # Font color selection
#         font_color_label = tk.Label(dialog, text="Font Color:")
#         font_color_label.grid(row=1, column=0, padx=5, pady=5)
        
#         font_color_button = tk.Button(dialog, text="Select Color", command=select_font_color)
#         font_color_button.grid(row=1, column=1, padx=5, pady=5)
        
#         # Apply button
#         apply_button = tk.Button(dialog, text="Apply", command=lambda: apply_text_watermark(filepath))
#         apply_button.grid(row=2, column=0, columnspan=2, pady=10)
        
#         # Cancel button
#         cancel_button = tk.Button(dialog, text="Cancel", command=dialog.destroy)
#         cancel_button.grid(row=3, column=0, columnspan=2, pady=10)

# def select_font_color():
#     global font_color
#     color = colorchooser.askcolor(title="Select Font Color")
#     if color:
#         font_color = color[1]  # Extract the hex color value

# def apply_text_watermark(filepath):
#     global watermark_text, font_size_var, font_color
    
#     font_size = int(font_size_var.get())
    
#     # Open the image
#     image = Image.open(filepath)
    
#     # Draw watermark text on the image
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.truetype("arial.ttf", font_size)  # You can specify any font you like
#     draw.text((10, 10), watermark_text, fill=font_color, font=font)
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image_with_text, 'label'):
#         display_image_with_text.label.destroy()
    
#     # Display the image with the watermark
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image with text is displayed
#     display_image_with_text.label = label
    
#     # Add save and restart buttons
#     add_save_and_restart_buttons()

# def upload_second_image(first_filepath):
#     second_filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if second_filepath:
#         paste_second_image(first_filepath, second_filepath)

# def paste_second_image(first_filepath, second_filepath):
#     global displayed_image
#     first_img = Image.open(first_filepath)
#     second_img = Image.open(second_filepath)
    
#     # Resize the second image to fit within the dimensions of the first image
#     second_img.thumbnail(first_img.size)
    
#     # Check if the second image has an alpha channel (transparency)
#     if 'A' in second_img.getbands():
#         # If the second image has transparency, paste it with transparency mask
#         first_img.paste(second_img, (0, 0), second_img)
#     else:
#         # If the second image does not have transparency, convert it to RGBA mode
#         second_img = second_img.convert('RGBA')
#         first_img.paste(second_img, (0, 0), second_img)
    
#     displayed_image = first_img
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_pasted_image, 'label'):
#         display_pasted_image.label.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is displayed
#     display_pasted_image.label = label
    
#     # Add save and restart buttons
#     add_save_and_restart_buttons()

# def add_save_and_restart_buttons():
#     # Add save button
#     save_button = tk.Button(root, text="Save Image", command=save_image)
#     save_button.pack(pady=5)
    
#     # Store the save button reference to remove it when a new image is displayed
#     display_image_with_text.save_button = save_button
    
#     # Add restart button
#     restart_button = tk.Button(root, text="Restart", command=restart_program)
#     restart_button.pack(pady=5)
    
#     # Store the restart button reference to remove it when a new image is displayed
#     display_image_with_text.restart_button = restart_button

# def save_image():
#     global displayed_image
#     if displayed_image:
#         save_filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
#         if save_filepath:
#             displayed_image.save(save_filepath)
#             messagebox.showinfo("Image Saved", f"The image has been saved as {save_filepath}")

# def restart_program():
#     python = sys.executable
#     os.execl(python, python, *sys.argv)

# root = tk.Tk()
# root.title("Image Uploader")

# upload_button = tk.Button(root, text="Upload Image", command=open_file)
# upload_button.pack(pady=20)

# root.mainloop()


#------------
# import tkinter as tk
# from tkinter import filedialog, messagebox, simpledialog
# from PIL import Image, ImageTk, ImageDraw, ImageFont
# import sys
# import os

# # Function to open a file dialog for image selection
# def open_file():
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if filepath:
#         display_image(filepath)

# # Function to display the image on the GUI
# def display_image(filepath):
#     global displayed_image
#     displayed_image = Image.open(filepath)
#     displayed_image.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
#     if hasattr(display_image, 'frame'):
#         display_image.frame.destroy()
#     if hasattr(display_image, 'save_button'):
#         display_image.save_button.destroy()
#     if hasattr(display_image, 'restart_button'):
#         display_image.restart_button.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is uploaded
#     display_image.label = label
    
#     # Add frame with options
#     frame = tk.Frame(root)
#     frame.pack(pady=10)
    
#     option1_button = tk.Button(frame, text="Add Text Watermark", command=lambda: option_selected("Add Text Watermark", filepath))
#     option1_button.pack(side=tk.LEFT, padx=5)
    
#     option2_button = tk.Button(frame, text="Add Image Watermark", command=lambda: option_selected("Add Image Watermark", filepath))
#     option2_button.pack(side=tk.LEFT, padx=5)
    
#     # Store the frame reference to remove it when a new image is uploaded
#     display_image.frame = frame

# # Function to handle option selection
# def option_selected(option, filepath):
#     if option == "Add Text Watermark":
#         show_text_watermark_dialog(filepath)
#     elif option == "Add Image Watermark":
#         upload_second_image(filepath)

# # Function to display a dialog for entering text watermark options
# def show_text_watermark_dialog(filepath):
#     text = simpledialog.askstring("Enter Text", "Enter some text:")
#     if text:
#         font_size = simpledialog.askinteger("Font Size", "Enter font size:", initialvalue=12)
#         if font_size:
#             font_path = filedialog.askopenfilename(title="Select Font File", filetypes=[("Font files", "*.ttf;*.otf")])
#             if font_path:
#                 display_image_with_text(filepath, text, font_path, font_size)

# # Function to display the image with text watermark
# def display_image_with_text(filepath, text, font_path, font_size):
#     global displayed_image
#     draw = ImageDraw.Draw(displayed_image)
#     try:
#         font = ImageFont.truetype(font_path, font_size)
#     except OSError as e:
#         messagebox.showerror("Font Error", f"Error loading font: {e}")
#         return
    
#     # Position to place the text
#     position = (10, 10)
    
#     # Drawing text on the image
#     draw.text(position, text, fill="white", font=font)
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image_with_text, 'label'):
#         display_image_with_text.label.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image with text is displayed
#     display_image_with_text.label = label
    
#     # Add save and restart buttons
#     add_save_and_restart_buttons()

# # Function to upload a second image for pasting as a watermark
# def upload_second_image(first_filepath):
#     second_filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if second_filepath:
#         paste_second_image(first_filepath, second_filepath)

# # Function to paste the second image as a watermark onto the first image
# def paste_second_image(first_filepath, second_filepath):
#     global displayed_image
#     first_img = Image.open(first_filepath)
#     second_img = Image.open(second_filepath)
    
#     # Resize the second image to fit within the dimensions of the first image
#     second_img.thumbnail(first_img.size)
    
#     # Check if the second image has an alpha channel (transparency)
#     if 'A' in second_img.getbands():
#         # If the second image has transparency, paste it with transparency mask
#         first_img.paste(second_img, (0, 0), second_img)
#     else:
#         # If the second image does not have transparency, convert it to RGBA mode
#         second_img = second_img.convert('RGBA')
#         first_img.paste(second_img, (0, 0), second_img)
    
#     displayed_image = first_img
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_pasted_image, 'label'):
#         display_pasted_image.label.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is displayed
#     display_pasted_image.label = label
    
#     # Add save and restart buttons
#     add_save_and_restart_buttons()

# # Function to add save and restart buttons
# def add_save_and_restart_buttons():
#     # Add save button
#     save_button = tk.Button(root, text="Save Image", command=save_image)
#     save_button.pack(pady=5)
    
#     # Store the save button reference to remove it when a new image is displayed
#     add_save_and_restart_buttons.save_button = save_button
    
#     # Add restart button
#     restart_button = tk.Button(root, text="Restart", command=restart_program)
#     restart_button.pack(pady=5)
    
#     # Store the restart button reference to remove it when a new image is displayed
#     add_save_and_restart_buttons.restart_button = restart_button

# # Function to save the displayed image
# def save_image():
#     global displayed_image
#     if displayed_image:
#         save_filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
#         if save_filepath:
#             displayed_image.save(save_filepath)
#             messagebox.showinfo("Image Saved", f"The image has been saved as {save_filepath}")

# # Function to restart the program
# def restart_program():
#     python = sys.executable
#     os.execl(python, python, *sys.argv)

# # Main Tkinter window
# root = tk.Tk()
# root.title("Image Uploader")

# # Button to upload image
# upload_button = tk.Button(root, text="Upload Image", command=open_file)
# upload_button.pack(pady=20)

# # Start the Tkinter event loop
# root.mainloop()


# Working --------------
# import tkinter as tk
# from tkinter import filedialog, messagebox, simpledialog
# from PIL import Image, ImageTk, ImageDraw, ImageFont
# import sys
# import os

# def open_file():
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if filepath:
#         display_image(filepath)

# def display_image(filepath):
#     global displayed_image
#     displayed_image = Image.open(filepath)
#     displayed_image.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
#     if hasattr(display_image, 'frame'):
#         display_image.frame.destroy()
#     if hasattr(display_image, 'save_button'):
#         display_image.save_button.destroy()
#     if hasattr(display_image, 'restart_button'):
#         display_image.restart_button.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is uploaded
#     display_image.label = label
    
#     # Add frame with options
#     frame = tk.Frame(root)
#     frame.pack(pady=10)
    
#     option1_button = tk.Button(frame, text="Add Text Watermark", command=lambda: option_selected("Add Text Watermark", filepath))
#     option1_button.pack(side=tk.LEFT, padx=5)
    
#     option2_button = tk.Button(frame, text="Add Image Watermark", command=lambda: option_selected("Add Image Watermark", filepath))
#     option2_button.pack(side=tk.LEFT, padx=5)
    
#     # Store the frame reference to remove it when a new image is uploaded
#     display_image.frame = frame

# def option_selected(option, filepath):
#     if option == "Add Text Watermark":
#         text = simpledialog.askstring("Enter Text", "Enter some text:")
#         if text:
#             display_image_with_text(filepath, text)
#     elif option == "Add Image Watermark":
#         upload_second_image(filepath)

# def display_image_with_text(filepath, text):
#     global displayed_image
#     draw = ImageDraw.Draw(displayed_image)
#     font = ImageFont.load_default()  # You can choose any font you have on your system
    
#     # Position to place the text
#     position = (10, 10)
    
#     # Drawing text on the image
#     draw.text(position, text, fill="white", font=font)
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image_with_text, 'label'):
#         display_image_with_text.label.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image with text is displayed
#     display_image_with_text.label = label
    
#     # Add save and restart buttons
#     add_save_and_restart_buttons()

# def upload_second_image(first_filepath):
#     second_filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if second_filepath:
#         paste_second_image(first_filepath, second_filepath)

# def paste_second_image(first_filepath, second_filepath):
#     global displayed_image
#     first_img = Image.open(first_filepath)
#     second_img = Image.open(second_filepath)
    
#     # Resize the second image to fit within the dimensions of the first image
#     second_img.thumbnail(first_img.size)
    
#     # Check if the second image has an alpha channel (transparency)
#     if 'A' in second_img.getbands():
#         # If the second image has transparency, paste it with transparency mask
#         first_img.paste(second_img, (0, 0), second_img)
#     else:
#         # If the second image does not have transparency, convert it to RGBA mode
#         second_img = second_img.convert('RGBA')
#         first_img.paste(second_img, (0, 0), second_img)
    
#     displayed_image = first_img
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_pasted_image, 'label'):
#         display_pasted_image.label.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is displayed
#     display_pasted_image.label = label
    
#     # Add save and restart buttons
#     add_save_and_restart_buttons()

# def add_save_and_restart_buttons():
#     # Add save button
#     save_button = tk.Button(root, text="Save Image", command=save_image)
#     save_button.pack(pady=5)
    
#     # Store the save button reference to remove it when a new image is displayed
#     display_image_with_text.save_button = save_button
    
#     # Add restart button
#     restart_button = tk.Button(root, text="Restart", command=restart_program)
#     restart_button.pack(pady=5)
    
#     # Store the restart button reference to remove it when a new image is displayed
#     display_image_with_text.restart_button = restart_button

# def save_image():
#     global displayed_image
#     if displayed_image:
#         save_filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
#         if save_filepath:
#             displayed_image.save(save_filepath)
#             messagebox.showinfo("Image Saved", f"The image has been saved as {save_filepath}")

# def restart_program():
#     python = sys.executable
#     os.execl(python, python, *sys.argv)

# root = tk.Tk()
# root.title("Image Uploader")

# upload_button = tk.Button(root, text="Upload Image", command=open_file)
# upload_button.pack(pady=20)

# root.mainloop()


# ------Working
# import os
# import tkinter as tk
# from tkinter import filedialog, messagebox, simpledialog
# from PIL import Image, ImageTk, ImageDraw, ImageFont
# import sys

# def open_file():
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if filepath:
#         display_image(filepath)

# def display_image(filepath):
#     global displayed_image
#     displayed_image = Image.open(filepath)
#     displayed_image.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
#     if hasattr(display_image, 'frame'):
#         display_image.frame.destroy()
#     if hasattr(display_image, 'save_button'):
#         display_image.save_button.destroy()
#     if hasattr(display_image, 'restart_button'):
#         display_image.restart_button.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is uploaded
#     display_image.label = label
    
#     # Add frame with options
#     frame = tk.Frame(root)
#     frame.pack(pady=10)
    
#     option1_button = tk.Button(frame, text="Option 1", command=lambda: option_selected("Option 1", filepath))
#     option1_button.pack(side=tk.LEFT, padx=5)
    
#     option2_button = tk.Button(frame, text="Option 2", command=lambda: option_selected("Option 2", filepath))
#     option2_button.pack(side=tk.LEFT, padx=5)
    
#     # Store the frame reference to remove it when a new image is uploaded
#     display_image.frame = frame

# def option_selected(option, filepath):
#     if option == "Option 1":
#         text = simpledialog.askstring("Enter Text", "Enter some text:")
#         if text:
#             display_image_with_text(filepath, text)
#     elif option == "Option 2":
#         upload_second_image(filepath)

# def display_image_with_text(filepath, text):
#     global displayed_image
#     draw = ImageDraw.Draw(displayed_image)
#     font = ImageFont.load_default()  # You can choose any font you have on your system
    
#     # Position to place the text
#     position = (0, 0)
    
#     # Drawing text on the image
#     draw.text(position, text, fill="white", font=font)
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image_with_text, 'label'):
#         display_image_with_text.label.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image with text is displayed
#     display_image_with_text.label = label
    
#     # Add save and restart buttons
#     add_save_and_restart_buttons()

# def upload_second_image(first_filepath):
#     second_filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if second_filepath:
#         paste_second_image(first_filepath, second_filepath)

# def paste_second_image(first_filepath, second_filepath):
#     global displayed_image
#     first_img = Image.open(first_filepath)
#     second_img = Image.open(second_filepath)
    
#     # Resize the second image to fit within the dimensions of the first image
#     second_img.thumbnail(first_img.size)
    
#     # Check if the second image has an alpha channel (transparency)
#     if 'A' in second_img.getbands():
#         # If the second image has transparency, paste it with transparency mask
#         first_img.paste(second_img, (0, 0), second_img)
#     else:
#         # If the second image does not have transparency, convert it to RGBA mode
#         second_img = second_img.convert('RGBA')
#         first_img.paste(second_img, (0, 0), second_img)
    
#     displayed_image = first_img
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_pasted_image, 'label'):
#         display_pasted_image.label.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is displayed
#     display_pasted_image.label = label
    
#     # Add save and restart buttons
#     add_save_and_restart_buttons()

# def add_save_and_restart_buttons():
#     # Add save button
#     save_button = tk.Button(root, text="Save Image", command=save_image)
#     save_button.pack(pady=5)
    
#     # Store the save button reference to remove it when a new image is displayed
#     display_image_with_text.save_button = save_button
    
#     # Add restart button
#     restart_button = tk.Button(root, text="Restart", command=restart_program)
#     restart_button.pack(pady=5)
    
#     # Store the restart button reference to remove it when a new image is displayed
#     display_image_with_text.restart_button = restart_button

# def save_image():
#     global displayed_image
#     if displayed_image:
#         save_filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
#         if save_filepath:
#             displayed_image.save(save_filepath)
#             messagebox.showinfo("Image Saved", f"The image has been saved as {save_filepath}")

# def restart_program():
#     python = sys.executable
#     os.execl(python, python, *sys.argv)

# root = tk.Tk()
# root.title("Image Uploader")

# upload_button = tk.Button(root, text="Upload Image", command=open_file)
# upload_button.pack(pady=20)

# root.mainloop()

#-------------
# import tkinter as tk
# from tkinter import filedialog, messagebox, simpledialog
# from PIL import Image, ImageTk, ImageDraw, ImageFont

# def open_file():
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if filepath:
#         display_image(filepath)

# def display_image(filepath):
#     global displayed_image
#     displayed_image = Image.open(filepath)
#     displayed_image.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
#     if hasattr(display_image, 'frame'):
#         display_image.frame.destroy()
#     if hasattr(display_image, 'save_button'):
#         display_image.save_button.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is uploaded
#     display_image.label = label
    
#     # Add frame with options
#     frame = tk.Frame(root)
#     frame.pack(pady=10)
    
#     option1_button = tk.Button(frame, text="Option 1", command=lambda: option_selected("Option 1", filepath))
#     option1_button.pack(side=tk.LEFT, padx=5)
    
#     option2_button = tk.Button(frame, text="Option 2", command=lambda: option_selected("Option 2", filepath))
#     option2_button.pack(side=tk.LEFT, padx=5)
    
#     # Store the frame reference to remove it when a new image is uploaded
#     display_image.frame = frame

# def option_selected(option, filepath):
#     if option == "Option 1":
#         text = simpledialog.askstring("Enter Text", "Enter some text:")
#         if text:
#             display_image_with_text(filepath, text)
#     elif option == "Option 2":
#         upload_second_image(filepath)

# def display_image_with_text(filepath, text):
#     global displayed_image
#     draw = ImageDraw.Draw(displayed_image)
#     font = ImageFont.load_default()  # You can choose any font you have on your system
    
#     # Position to place the text
#     position = (10, 10)
    
#     # Drawing text on the image
#     draw.text(position, text, fill="white", font=font)
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image_with_text, 'label'):
#         display_image_with_text.label.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image with text is displayed
#     display_image_with_text.label = label
    
#     # Add save button
#     save_button = tk.Button(root, text="Save Image", command=save_image)
#     save_button.pack(pady=10)
    
#     # Store the save button reference to remove it when a new image is displayed
#     display_image_with_text.save_button = save_button

# def upload_second_image(first_filepath):
#     second_filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if second_filepath:
#         paste_second_image(first_filepath, second_filepath)

# def paste_second_image(first_filepath, second_filepath):
#     global displayed_image
#     first_img = Image.open(first_filepath)
#     second_img = Image.open(second_filepath)
    
#     # Resize the second image to fit within the dimensions of the first image
#     second_img.thumbnail(first_img.size)
    
#     # Check if the second image has an alpha channel (transparency)
#     if 'A' in second_img.getbands():
#         # If the second image has transparency, paste it with transparency mask
#         first_img.paste(second_img, (0, 0), second_img)
#     else:
#         # If the second image does not have transparency, convert it to RGBA mode
#         second_img = second_img.convert('RGBA')
#         first_img.paste(second_img, (0, 0), second_img)
    
#     displayed_image = first_img
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(displayed_image)
    
#     # Clear any previous image displayed
#     if hasattr(display_pasted_image, 'label'):
#         display_pasted_image.label.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is displayed
#     display_pasted_image.label = label
    
#     # Add save button
#     save_button = tk.Button(root, text="Save Image", command=save_image)
#     save_button.pack(pady=10)
    
#     # Store the save button reference to remove it when a new image is displayed
#     display_pasted_image.save_button = save_button

# def save_image():
#     global displayed_image
#     if displayed_image:
#         save_filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
#         if save_filepath:
#             displayed_image.save(save_filepath)
#             messagebox.showinfo("Image Saved", f"The image has been saved as {save_filepath}")

# root = tk.Tk()
# root.title("Image Uploader")

# upload_button = tk.Button(root, text="Upload Image", command=open_file)
# upload_button.pack(pady=20)

# root.mainloop()

#---------------
# import tkinter as tk
# from tkinter import filedialog, messagebox, simpledialog
# from PIL import Image, ImageTk, ImageDraw, ImageFont

# def open_file():
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if filepath:
#         display_image(filepath)

# def display_image(filepath):
#     img = Image.open(filepath)
#     img.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
#     img = ImageTk.PhotoImage(img)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
#     if hasattr(display_image, 'frame'):
#         display_image.frame.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is uploaded
#     display_image.label = label
    
#     # Add frame with options
#     frame = tk.Frame(root)
#     frame.pack(pady=10)
    
#     option1_button = tk.Button(frame, text="Option 1", command=lambda: option_selected("Option 1", filepath))
#     option1_button.pack(side=tk.LEFT, padx=5)
    
#     option2_button = tk.Button(frame, text="Option 2", command=lambda: option_selected("Option 2", filepath))
#     option2_button.pack(side=tk.LEFT, padx=5)
    
#     # Store the frame reference to remove it when a new image is uploaded
#     display_image.frame = frame

# def option_selected(option, filepath):
#     if option == "Option 1":
#         text = simpledialog.askstring("Enter Text", "Enter some text:")
#         if text:
#             display_image_with_text(filepath, text)
#     elif option == "Option 2":
#         upload_second_image(filepath)

# def display_image_with_text(filepath, text):
#     image = Image.open(filepath)
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.load_default()  # You can choose any font you have on your system
    
#     # Position to place the text
#     position = (10, 10)
    
#     # Drawing text on the image
#     draw.text(position, text, fill="white", font=font)
    
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image_with_text, 'label'):
#         display_image_with_text.label.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image with text is displayed
#     display_image_with_text.label = label

# def upload_second_image(first_filepath):
#     second_filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if second_filepath:
#         paste_second_image(first_filepath, second_filepath)

# def paste_second_image(first_filepath, second_filepath):
#     first_img = Image.open(first_filepath)
#     second_img = Image.open(second_filepath)
    
#     # Resize the second image to fit within the dimensions of the first image
#     second_img.thumbnail(first_img.size)
    
#     # Check if the second image has an alpha channel (transparency)
#     if 'A' in second_img.getbands():
#         # If the second image has transparency, paste it with transparency mask
#         first_img.paste(second_img, (0, 0), second_img)
#     else:
#         # If the second image does not have transparency, convert it to RGBA mode
#         second_img = second_img.convert('RGBA')
#         first_img.paste(second_img, (0, 0), second_img)
    
#     # Save or display the modified image
#     display_pasted_image(first_img)

# def display_pasted_image(image):
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(image)
    
#     # Clear any previous image displayed
#     if hasattr(display_pasted_image, 'label'):
#         display_pasted_image.label.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is displayed
#     display_pasted_image.label = label

# root = tk.Tk()
# root.title("Image Uploader")

# upload_button = tk.Button(root, text="Upload Image", command=open_file)
# upload_button.pack(pady=20)

# root.mainloop()

#----------
# import tkinter as tk
# from tkinter import filedialog, messagebox, simpledialog
# from PIL import Image, ImageTk

# def open_file():
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if filepath:
#         display_image(filepath)

# def display_image(filepath):
#     img = Image.open(filepath)
#     img.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
#     img = ImageTk.PhotoImage(img)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
#     if hasattr(display_image, 'frame'):
#         display_image.frame.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is uploaded
#     display_image.label = label
    
#     # Add frame with options
#     frame = tk.Frame(root)
#     frame.pack(pady=10)
    
#     option1_button = tk.Button(frame, text="Option 1", command=lambda: option_selected("Option 1", filepath))
#     option1_button.pack(side=tk.LEFT, padx=5)
    
#     option2_button = tk.Button(frame, text="Option 2", command=lambda: option_selected("Option 2", filepath))
#     option2_button.pack(side=tk.LEFT, padx=5)
    
#     # Store the frame reference to remove it when a new image is uploaded
#     display_image.frame = frame

# def option_selected(option, filepath):
#     if option == "Option 1":
#         text = simpledialog.askstring("Enter Text", "Enter some text:")
#         if text:
#             display_image_with_text(filepath, text)
#     elif option == "Option 2":
#         upload_second_image(filepath)

# def upload_second_image(first_filepath):
#     second_filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if second_filepath:
#         paste_second_image(first_filepath, second_filepath)

# def paste_second_image(first_filepath, second_filepath):
#     first_img = Image.open(first_filepath)
#     second_img = Image.open(second_filepath)
    
#     # Resize the second image to fit within the dimensions of the first image
#     second_img.thumbnail(first_img.size)
    
#     # Check if the second image has an alpha channel (transparency)
#     if 'A' in second_img.getbands():
#         # If the second image has transparency, paste it with transparency mask
#         first_img.paste(second_img, (0, 0), second_img)
#     else:
#         # If the second image does not have transparency, convert it to RGBA mode
#         second_img = second_img.convert('RGBA')
#         first_img.paste(second_img, (0, 0), second_img)
    
#     # Save or display the modified image
#     display_pasted_image(first_img)

# def display_pasted_image(image):
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(image)
    
#     # Clear any previous image displayed
#     if hasattr(display_pasted_image, 'label'):
#         display_pasted_image.label.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is displayed
#     display_pasted_image.label = label

# root = tk.Tk()
# root.title("Image Uploader")

# upload_button = tk.Button(root, text="Upload Image", command=open_file)
# upload_button.pack(pady=20)

# root.mainloop()

#-----------
# import tkinter as tk
# from tkinter import filedialog, messagebox
# from PIL import Image, ImageTk

# def open_file():
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if filepath:
#         display_image(filepath)

# def display_image(filepath):
#     img = Image.open(filepath)
#     img.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
#     img = ImageTk.PhotoImage(img)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
#     if hasattr(display_image, 'frame'):
#         display_image.frame.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is uploaded
#     display_image.label = label
    
#     # Add frame with options
#     frame = tk.Frame(root)
#     frame.pack(pady=10)
    
#     option1_button = tk.Button(frame, text="Option 1", command=lambda: option_selected("Option 1", filepath))
#     option1_button.pack(side=tk.LEFT, padx=5)
    
#     option2_button = tk.Button(frame, text="Option 2", command=lambda: option_selected("Option 2", filepath))
#     option2_button.pack(side=tk.LEFT, padx=5)
    
#     # Store the frame reference to remove it when a new image is uploaded
#     display_image.frame = frame

# def option_selected(option, filepath):
#     if option == "Option 1":
#         text = simpledialog.askstring("Enter Text", "Enter some text:")
#         if text:
#             display_image_with_text(filepath, text)
#     elif option == "Option 2":
#         upload_second_image(filepath)

# def upload_second_image(filepath):
#     second_filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if second_filepath:
#         paste_second_image(filepath, second_filepath)

# def paste_second_image(first_filepath, second_filepath):
#     first_img = Image.open(first_filepath)
#     second_img = Image.open(second_filepath)
    
#     # Resize the second image to fit within the dimensions of the first image
#     second_img.thumbnail(first_img.size)
    
#     # Paste the second image on top of the first one
#     first_img.paste(second_img, (0, 0), second_img)
    
#     # Save or display the modified image
#     display_pasted_image(first_img)

# def display_pasted_image(image):
#     # Convert image to PhotoImage format
#     img = ImageTk.PhotoImage(image)
    
#     # Clear any previous image displayed
#     if hasattr(display_pasted_image, 'label'):
#         display_pasted_image.label.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is displayed
#     display_pasted_image.label = label

# root = tk.Tk()
# root.title("Image Uploader")

# upload_button = tk.Button(root, text="Upload Image", command=open_file)
# upload_button.pack(pady=20)

# root.mainloop()

#-----------------
# import tkinter as tk
# from tkinter import filedialog, messagebox, simpledialog
# from PIL import Image, ImageTk, ImageDraw, ImageFont

# def open_file():
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if filepath:
#         display_image(filepath)

# def display_image(filepath):
#     img = Image.open(filepath)
#     img.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
#     photo_img = ImageTk.PhotoImage(img)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
#     if hasattr(display_image, 'frame'):
#         display_image.frame.destroy()
    
#     label = tk.Label(root, image=photo_img)
#     label.image = photo_img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is uploaded
#     display_image.label = label
    
#     # Add frame with options
#     frame = tk.Frame(root)
#     frame.pack(pady=10)
    
#     option1_button = tk.Button(frame, text="Option 1", command=lambda: option_selected("Option 1", img, filepath))
#     option1_button.pack(side=tk.LEFT, padx=5)
    
#     option2_button = tk.Button(frame, text="Option 2", command=lambda: option_selected("Option 2", img, filepath))
#     option2_button.pack(side=tk.LEFT, padx=5)
    
#     # Store the frame reference to remove it when a new image is uploaded
#     display_image.frame = frame

# def option_selected(option, img, filepath):
#     if option == "Option 1":
#         text = simpledialog.askstring("Enter Text", "Enter some text:")
#         if text:
#             img_with_text = add_text_to_image(img, text, filepath)
#             display_image_with_text(img_with_text, filepath)
#     else:
#         messagebox.showinfo("Option Selected", f"You selected: {option}")

# def add_text_to_image(img, text, filepath):
#     image = Image.open(filepath)
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.load_default()  # You can choose any font you have on your system
    
#     # Position to place the text
#     position = (10, 10)
    
#     # Drawing text on the image
#     draw.text(position, text, fill="white", font=font)
    
#     return image

# def display_image_with_text(image, filepath):
#     # Convert image to PhotoImage format
#     photo_img = ImageTk.PhotoImage(image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image_with_text, 'label'):
#         display_image_with_text.label.destroy()
    
#     label = tk.Label(root, image=photo_img)
#     label.image = photo_img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image with text is displayed
#     display_image_with_text.label = label
    
#     # Ask user whether to save the modified image
#     save_image_prompt(filepath, image)

# def save_image_prompt(filepath, image):
#     response = messagebox.askyesno("Save Image", "Do you want to save the modified image?")
#     if response:
#         save_image(filepath, image)

# def save_image(filepath, image):
#     save_filepath = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
#     if save_filepath:
#         image.save(save_filepath)
#         messagebox.showinfo("Image Saved", f"The modified image has been saved as {save_filepath}")

# root = tk.Tk()
# root.title("Image Uploader")

# upload_button = tk.Button(root, text="Upload Image", command=open_file)
# upload_button.pack(pady=20)

# root.mainloop()

#---------------
# import tkinter as tk
# from tkinter import filedialog, messagebox, simpledialog
# from PIL import Image, ImageTk, ImageDraw, ImageFont

# def open_file():
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if filepath:
#         display_image(filepath)

# def display_image(filepath):
#     img = Image.open(filepath)
#     img.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
#     photo_img = ImageTk.PhotoImage(img)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
#     if hasattr(display_image, 'frame'):
#         display_image.frame.destroy()
    
#     label = tk.Label(root, image=photo_img)
#     label.image = photo_img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is uploaded
#     display_image.label = label
    
#     # Add frame with options
#     frame = tk.Frame(root)
#     frame.pack(pady=10)
    
#     option1_button = tk.Button(frame, text="Option 1", command=lambda: option_selected("Option 1", img, filepath))
#     option1_button.pack(side=tk.LEFT, padx=5)
    
#     option2_button = tk.Button(frame, text="Option 2", command=lambda: option_selected("Option 2", img, filepath))
#     option2_button.pack(side=tk.LEFT, padx=5)
    
#     # Store the frame reference to remove it when a new image is uploaded
#     display_image.frame = frame

# def option_selected(option, img, filepath):
#     if option == "Option 1":
#         text = simpledialog.askstring("Enter Text", "Enter some text:")
#         if text:
#             img_with_text = add_text_to_image(img, text, filepath)
#             display_image_with_text(img_with_text)
#     else:
#         messagebox.showinfo("Option Selected", f"You selected: {option}")

# def add_text_to_image(img, text, filepath):
#     image = Image.open(filepath)
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.load_default()  # You can choose any font you have on your system
    
#     # Position to place the text
#     position = (10, 10)
    
#     # Drawing text on the image
#     draw.text(position, text, fill="white", font=font)
    
#     return image

# def display_image_with_text(image):
#     # Convert image to PhotoImage format
#     photo_img = ImageTk.PhotoImage(image)
    
#     # Clear any previous image displayed
#     if hasattr(display_image_with_text, 'label'):
#         display_image_with_text.label.destroy()
    
#     label = tk.Label(root, image=photo_img)
#     label.image = photo_img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image with text is displayed
#     display_image_with_text.label = label

# root = tk.Tk()
# root.title("Image Uploader")

# upload_button = tk.Button(root, text="Upload Image", command=open_file)
# upload_button.pack(pady=20)

# root.mainloop()



#-------------
# import tkinter as tk
# from tkinter import filedialog, messagebox, simpledialog
# from PIL import Image, ImageTk

# def open_file():
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if filepath:
#         display_image(filepath)

# def display_image(filepath):
#     img = Image.open(filepath)
#     img.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
#     img = ImageTk.PhotoImage(img)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
#     if hasattr(display_image, 'frame'):
#         display_image.frame.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is uploaded
#     display_image.label = label
    
#     # Add frame with options
#     frame = tk.Frame(root)
#     frame.pack(pady=10)
    
#     option1_button = tk.Button(frame, text="Option 1", command=lambda: option_selected("Option 1"))
#     option1_button.pack(side=tk.LEFT, padx=5)
    
#     option2_button = tk.Button(frame, text="Option 2", command=lambda: option_selected("Option 2"))
#     option2_button.pack(side=tk.LEFT, padx=5)
    
#     # Store the frame reference to remove it when a new image is uploaded
#     display_image.frame = frame

# def option_selected(option):
#     if option == "Option 1":
#         text = simpledialog.askstring("Enter Text", "Enter some text:")
#         if text:
#             display_text(text)
#     else:
#         messagebox.showinfo("Option Selected", f"You selected: {option}")

# def display_text(text):
#     # Clear any previous text displayed
#     if hasattr(display_text, 'text_label'):
#         display_text.text_label.destroy()
    
#     text_label = tk.Label(root, text=text)
#     text_label.pack(pady=10)
    
#     # Store the label reference to remove it when a new text is displayed
#     display_text.text_label = text_label

# root = tk.Tk()
# root.title("Image Uploader")

# upload_button = tk.Button(root, text="Upload Image", command=open_file)
# upload_button.pack(pady=20)

# root.mainloop()


#------------------
# import tkinter as tk
# from tkinter import filedialog, messagebox
# from PIL import Image, ImageTk

# def open_file():
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if filepath:
#         display_image(filepath)

# def display_image(filepath):
#     img = Image.open(filepath)
#     img.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
#     img = ImageTk.PhotoImage(img)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
#     if hasattr(display_image, 'frame'):
#         display_image.frame.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is uploaded
#     display_image.label = label
    
#     # Add frame with options
#     frame = tk.Frame(root)
#     frame.pack(pady=10)
    
#     option1_button = tk.Button(frame, text="Option 1", command=lambda: option_selected("Option 1"))
#     option1_button.pack(side=tk.LEFT, padx=5)
    
#     option2_button = tk.Button(frame, text="Option 2", command=lambda: option_selected("Option 2"))
#     option2_button.pack(side=tk.LEFT, padx=5)
    
#     # Store the frame reference to remove it when a new image is uploaded
#     display_image.frame = frame

# def option_selected(option):
#     messagebox.showinfo("Option Selected", f"You selected: {option}")

# root = tk.Tk()
# root.title("Image Uploader")

# upload_button = tk.Button(root, text="Upload Image", command=open_file)
# upload_button.pack(pady=20)

# root.mainloop()

#----------------------
# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk

# def open_file():
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if filepath:
#         display_image(filepath)

# def display_image(filepath):
#     img = Image.open(filepath)
#     img.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
#     img = ImageTk.PhotoImage(img)
    
#     # Clear any previous image displayed
#     if hasattr(display_image, 'label'):
#         display_image.label.destroy()
    
#     label = tk.Label(root, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     # Store the label reference to remove it when a new image is uploaded
#     display_image.label = label

# root = tk.Tk()
# root.title("Image Uploader")

# upload_button = tk.Button(root, text="Upload Image", command=open_file)
# upload_button.pack(pady=20)

# root.mainloop()


#-------------------------
# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk

# def open_file():
#     filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#     if filepath:
#         display_image(filepath)

# def display_image(filepath):
#     img = Image.open(filepath)
#     img.thumbnail((300, 300))  # Resizing image to fit within a 300x300 box
#     img = ImageTk.PhotoImage(img)
    
#     popup = tk.Toplevel()
#     popup.title("Selected Image")
    
#     label = tk.Label(popup, image=img)
#     label.image = img  # Keep a reference to the image object to prevent garbage collection
#     label.pack()
    
#     close_button = tk.Button(popup, text="Close", command=popup.destroy)
#     close_button.pack()

# root = tk.Tk()
# root.title("Image Uploader")

# upload_button = tk.Button(root, text="Upload Image", command=open_file)
# upload_button.pack(pady=20)

# root.mainloop()

#--------------------------------------------

# from tkinter import *
# from tkinter import filedialog
# from tkinter.filedialog import askopenfile
# from PIL import Image, ImageTk, ImageFont, ImageDraw

# window = Tk()

# canvas = Canvas(height=526, width=800,
#                 bg="#f7f5dd", highlightthickness=0)
# img = Image.open('Day-85/base.jpg')
# front_img = PhotoImage(file="Day-85\images\card_front.png")
# back_img = PhotoImage(file="Day-31\images\card_back.png")
# c_img = PhotoImage(img)
# canvas_image = canvas.create_image(400, 263, image=front_img)
# canvas.grid(row=0, column=0, columnspan=2)



# window.mainloop()
