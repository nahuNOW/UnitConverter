import tkinter as tk
from tkinter import ttk

def convert():
    value = float(entry.get())
    conversion_type = conversion.get()
    if conversion_type == "Inches to Centimeters":
        result.set(f"{value * 2.54:.2f} cm")
    elif conversion_type == "Feet to Meters":
        result.set(f"{value * 0.3048:.2f} m")
    elif conversion_type == "Miles to Kilometers":
        result.set(f"{value * 1.60934:.2f} km")
    elif conversion_type == "Pounds to Kilograms":
        result.set(f"{value * 0.453592:.2f} kg")
    elif conversion_type == "Gallons to Liters":
        result.set(f"{value * 3.78541:.2f} L")

app = tk.Tk()
app.title("Customary to Metric Converter")

frame = ttk.Frame(app, padding=20)
frame.grid()

entry_label = ttk.Label(frame, text="Value:")
entry_label.grid(column=0, row=0)
entry = ttk.Entry(frame, width=15)
entry.grid(column=1, row=0)

conversion_label = ttk.Label(frame, text="Conversion:")
conversion_label.grid(column=0, row=1)
conversion = ttk.Combobox(frame, values=["Inches to Centimeters", "Feet to Meters", "Miles to Kilometers", "Pounds to Kilograms", "Gallons to Liters"])
conversion.grid(column=1, row=1)
conversion.current(0)

result_label = ttk.Label(frame, text="Result:")
result_label.grid(column=0, row=2)
result = tk.StringVar()
result_display = ttk.Label(frame, textvariable=result)
result_display.grid(column=1, row=2)

convert_button = ttk.Button(frame, text="Convert", command=convert)
convert_button.grid(column=0, row=3, columnspan=2)

app.mainloop()
