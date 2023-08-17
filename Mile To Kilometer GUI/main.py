from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

def mile_to_km():
    miles = int(miles_input.get())
    km = round(1.609344*miles)
    km_label.config(text=f"{km}")
    


label1 = Label(text="is equal to")
label1.grid(row=1, column=0)




miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

km_label = Label(text="0")
km_label.grid(row=1, column=1)

label2 = Label(text="miles")
label2.grid(row=0, column=2)

label3 = Label(text="Km")
label3.grid(row=1, column=2)

button = Button(text = "Calculate", command=mile_to_km) 
button.grid(row=2, column=1)

window.mainloop()