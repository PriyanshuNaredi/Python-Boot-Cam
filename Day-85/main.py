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
    dialog.title("Watermark Text Options")
    
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
    
    font_color_var = tk.StringVar(dialog,value='white')
    
    
    font_color_button = tk.Button(dialog, text="Select Color", command=lambda: select_font_color(dialog))
    if (font_color_button):
        font_color = '#FFFFFF'
    font_color_button.grid(row=2, column=1, padx=5, pady=5)

    
    # Apply button
    apply_button = tk.Button(dialog, text="Apply", command=lambda: apply_watermark(filepath, watermark_text_entry.get(), font_size_var.get(), font_color, dialog))
    apply_button.grid(row=3, column=0, columnspan=2, pady=10)
    
    # Cancel button
    cancel_button = tk.Button(dialog, text="Cancel", command=dialog.destroy)
    cancel_button.grid(row=4, column=0, columnspan=2, pady=10)

def select_font_color(dialog):
    global font_color
    color = colorchooser.askcolor(title="Select Font Color",color='#FFFFFF')
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