class Animal:
    info_animal = "eukaryotic, able to move, diet of organic materials, can reproduce, breathes air"

class Mammal(Animal):
    info_mammal = Animal.info_animal + '''
warm-blooded, has a backbone, has fur (at some point in lifespan)'''

class Cat(Mammal):

    def __init__(self, info):
        self.info_cat = "Cat: " + Mammal.info_mammal + '''
Has a tail, has sensitive nose, has ability to land from heights without injury, 
has sharp teeth and claws, preys on small animals such as mice and rabbits. Many cats are domesticated.'''
example_cat = Cat("")
print(example_cat.info_cat)
