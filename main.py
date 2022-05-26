from tkinter import *

def miles_to_km():
    km = float(km_input.get())
    miles = round(km / 1.609)
    miles_result_label.config(text=f"{miles}")

window = Tk()
window.title("Miles to Kilometer Converter")

km_input = Entry()
km_input.grid(column=1 ,row=0, pady=20)

miles_label = Label(text="Kilometers")
miles_label.grid(column=2 ,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0 ,row=1, padx=20)

miles_result_label = Label(text="0")
miles_result_label.grid(column=1 ,row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2 ,row=1, padx=20)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1 ,row=2, pady=20)

window.mainloop()