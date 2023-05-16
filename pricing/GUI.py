from msilib.schema import SelfReg
import tkinter as tk
from typing import Self

from function.function5 import calculatePrice5


class Observable:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def unregister_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()


class FunctionDropdown(Observable):
    def __init__(self, parent):
        super().__init__()
        self.function_var = tk.StringVar()
        self.dropdown = tk.OptionMenu(parent, self.function_var, *range(1, 6), command=self.notify_observers)
        self.dropdown.grid(row=0, column=1, padx=10, pady=5)

    def get_function_choice(self):
        return int(self.function_var.get())


class PriceCalculator(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.function_dropdown = FunctionDropdown(self)
        self.price_label = tk.Label(self, text="Price: $ ")
        self.price_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.drink_type_var = tk.StringVar()
        self.size_var = tk.StringVar()
        self.sugar_var = tk.IntVar()
        self.milk_var = tk.StringVar()
        self.whipped_cream_var = tk.StringVar()

        self.create_input_widgets()
        self.create_calculate_button()

    def create_input_widgets(self):
        drink_type_label = tk.Label(self, text="Drink Type:")
        drink_type_label.grid(row=1, column=0, padx=10, pady=5)
        drink_type_entry = tk.Entry(self, textvariable=self.drink_type_var)
        drink_type_entry.grid(row=1, column=1, padx=10, pady=5)

        size_label = tk.Label(self, text="Size:")
        size_label.grid(row=2, column=0, padx=10, pady=5)
        size_entry = tk.Entry(self, textvariable=self.size_var)
        size_entry.grid(row=2, column=1, padx=10, pady=5)

        sugar_label = tk.Label(self, text="Sugar:")
        sugar_label.grid(row=3, column=0, padx=10, pady=5)
        sugar_entry = tk.Entry(self, textvariable=self.sugar_var)
        sugar_entry.grid(row=3, column=1, padx=10, pady=5)

        milk_label = tk.Label(self, text="Milk:")
        milk_label.grid(row=4, column=0, padx=10, pady=5)
        milk_entry = tk.Entry(self, textvariable=self.milk_var)
        milk_entry.grid(row=4, column=1, padx=10, pady=5)

        whipped_cream_label = tk.Label(self, text="Whipped Cream:")
        whipped_cream_label.grid(row=5, column=0, padx=10, pady=5)
        whipped_cream_entry = tk.Entry(self, textvariable=self.whipped_cream_var)
        whipped_cream_entry.grid(row=5, column=1, padx=10, pady=5)

    def create_calculate_button(self):
        calculate_button = tk.Button(self, text="Calculate Price", command=self.calculate_price)
        calculate_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

    def calculate_price(self):
        function_choice = self.function_dropdown.get_function_choice()

        if function_choice == 1:
            options = {
               drink_type': self.drink_type_var.get(),
'size': self.size_var.get(),
'whipped_cream': self.whipped_cream_var.get(),
'availability_L_size': (self.size_var.get() == 'L')
            }
try:
price = calculatePrice1(options)
self.price_label.config(text="Price: $ {}".format(price))
except ValueError as e:
self.price_label.config(text=str(e))
    elif function_choice == 2:
        options = {
            'drink_type': self.drink_type_var.get(),
            'size': self.size_var.get(),
            'sugar': self.sugar_var.get(),
            'milk': self.milk_var.get(),
            'whipped_cream': self.whipped_cream_var.get()
        }
        try:
            price = calculatePrice2(options)
            self.price_label.config(text="Price: $ {}".format(price))
        except ValueError as e:
            self.price_label.config(text=str(e))

    elif function_choice == 3:
        options = {
            'drink_type': self.drink_type_var.get(),
            'size': self.size_var.get(),
            'milk': self.milk_var.get(),
            'sugar': self.sugar_var.get(),
            'whipped_cream': self.whipped_cream_var.get()
        }
        try:
            price = calculatePrice3(options)
            self.price_label.config(text="Price: $ {}".format(price))
        except ValueError as e:
            self.price_label.config(text=str(e))

    elif function_choice == 4:
        options = {
            'drink_type': self.drink_type_var.get(),
            'size': self.size_var.get(),
            'sugar': self.sugar_var.get(),
            'milk': self.milk_var.get(),
            'whipped_cream': self.whipped_cream_var.get()
        }
        try:
            price = calculatePrice4(options)
            self.price_label.config(text="Price: $ {}".format(price))
        except ValueError as e:
            self.price_label.config(text=str(e))

    elif function_choice == 5:
        options = {
            'drink_type': self.drink_type_var.get(),
            'size': self.size_var.get(),
            'sugar': self.sugar_var.get(),
            'milk': self.milk_var.get(),
            'whipped_cream': self.whipped_cream_var.get()
        }
        try:
            price = calculatePrice5(options)
            Self.price_label.config(text="Price: $ {}".format(price))
        except ValueError as e:
            SelfReg.price_label.config(text=str(e))
if name == 'main':
window = tk.Tk()
window.title("Coffee Shop")
calculator = PriceCalculator(window)
calculator.grid(row=0, column=0, padx=10, pady=5)

window.mainloop()

