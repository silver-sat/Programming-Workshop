# Car class example
#

class Car:

    function = 'Transportation'

    def __init__(self, color, make, age):
        self.color = color
        self.make = make
        self.age = age

    def description(self):
        return f"This car is a {self.age} year old {self.color} {self.make}"

    def efficiency(self, mpg):
        return f"The {self.make} gets {mpg} miles per gallon"

    