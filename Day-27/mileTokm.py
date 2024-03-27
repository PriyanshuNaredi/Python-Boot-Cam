from tkinter import *

def mile_to_km():
    input_mile = input.get()
    ans = float(input_mile) * 1.60934
    converted.config(text=ans)


window = Tk()
window.title("Miles To KiloMeter Converter")
window.config(padx=20, pady=20)

input = Entry(width=7)
input.grid(column=1, row=0)

mile_label = Label(text="Miles", font=("Arial", 16, "bold"))
mile_label.grid(column=2, row=0)

convert_text = Label(text="is equal to ", font=("Arial", 16, "bold"))
convert_text.grid(column=0, row=1)

converted = Label(text=0, font=("Arial", 16, "bold"))
converted.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 16, "bold"))
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)

window.mainloop()
