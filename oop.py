import random
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I","J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Å", "Ä", "Ö"]


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
            self.licenseplate += str(random.randint(0,9))
        return self.licenseplate
    
    def get_horsepower(self):
        return random.randint(100, 500)

car1 = Car("Toyota", 2020)

print(car1.horsepower, car1.licenseplate, car1.make, car1.year,)


    