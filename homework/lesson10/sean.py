class animal:
    def __init__(self, fur):
        self.fur = fur

class mammal(animal):
    def __init__(self, fur, sweat_glands):
        animal.__init__(self, fur)
        self.sweat_glands = sweat_glands

class cat(mammal):
    def __init__(self, fur, sweat_glands, diaphragm):
        animal.__init__(self, fur)
        mammal.__init__(self, fur, sweat_glands)
        self.diaphragm = diaphragm

my_cat = cat("fur, ", "no sweat_glands, ", "diaphragm.")
print("my cat has " + my_cat.fur, my_cat.sweat_glands, my_cat.diaphragm)