import tkinter as tk
import random

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year
        self.licenseplate = self.new_licenseplate()
        self.horsepower = self.get_horsepower()

    def new_licenseplate(self):
        self.licenseplate = ""
        for i in range(3):
            self.licenseplate += random.choice(alphabet)
        self.licenseplate += " "
        for i in range(3):
            self.licenseplate += str(random.randint(0, 9))
        return self.licenseplate

    def get_horsepower(self):
        return random.randint(100, 500)

car1 = Car("Toyota", 2020)

root = tk.Tk()

info = f"HP: {car1.horsepower}\nLicenseplate: {car1.licenseplate}\nMake: {car1.make}\nYear: {car1.year}"
label = tk.Label(root, text=info)
label.pack()

root.mainloop()