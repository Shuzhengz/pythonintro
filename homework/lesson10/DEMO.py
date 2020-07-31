qwerty = "123"

class Car:
    brand = "x"

    def __init__(self, year, colour):
        self.year = year
        self.colour = colour

    def drive(self):
        print("where is the car?")

class Van(Car):
    def __init__(self, year, colour, size):
        Car.__init__(self, year, colour)
        self.size = size

    def load(self):
        return Car.self + self.size


class bigCar(Car):
    def __init__(self, year, colour, tire):
        Car.__init__(self, year, colour)
        self.tire = tire

    def load(self):
        return Car.self + self.sire

big_van = Van(1900, "invisible", "BIG")
big_van.brand = input("What brand?!")
print (big_van.brand)
print (big_van.size)
big_van.drive()
big_van.load()
