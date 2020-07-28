class Car:
    brand = "x"

    def __init__(self, year, colour):
        self.year = year
        self.colour = colour

    def drive(self):
        print("where is the car?")

class Van(Car):
    size = "yes"

big_van = Van(1900, "invisible")
big_van.brand = input("What brand?!")
print (big_van.brand)
big_van.drive()
