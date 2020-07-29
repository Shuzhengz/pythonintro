#lesson1:
def Lesson_1():
    print("I am Sean and I am 13 years old")
    agemonth = 13*12
    print("and I am " + str(agemonth) + " month old")
print(Lesson_1())

#lesson2:
def Lesson_2():
    name = input("What is your name? ")
    x = input("How many pizza you want? ")
    y = input("How many pepperonis do you want on YOUR FREAKING PIZZA? ")
    z = input("HOW MANY OLIVES DO YOU WANT ON YOU FREAKEDY FREAKING PIZZA!!! ")
    print(name + " orderd " + x + " FREAKING PIZZAS WITH " + y + " FREAKING PEPPERONIS AND " + z + " **** OLIVES.")
    print('''
    And you will get an extra FOOT LETTUCE ON YOUR PIZZA!
    HAVE A LOVELY F***ING DAY
    ''')
print(Lesson_2())

#lesson4:
def Lesson_4():
    x = int(input("What is your age? "))
    if x >= 14:
        print("You could join the Robotics Team.")
    if x >= 16:
        print("You could drive and get a job.")
    if x >= 18:
        print("You can attend to college")
    if x >= 21:
        print("You are an adult.")
    if x >= 35:
        print("You could become the President.")
    if x < 14:
        print("Sorry, you couldn't do anything...")
print(Lesson_4())

#lesson6.1:
def Lesson_6_1():
    words = ["me", "he", "she", "you", "I", "his", "her", "it", "its", "us"]
    x = input("give me a word. ")
    print(x in words)
    if (x in words) == True :
        print(words)
    if (x in words) == False :
        words.append(str(x))
        print(words)
print(Lesson_6_1())

#lesson6.2:
def Lesson_6_2():
    store = ["Name", "color", "x"]
    y = input("What's your name? ")
    store[0] = y
    z = input("What is your favorite color? ")
    store[1] = z
    a = input("How many pets do you have? ")
    store[2] = a
    print(store[0] + "'s favorite color is " + store[1] + ". They have " + store[2] + " pets. ")
print(Lesson_6_2())

#lesson7.1:
def Lesson_7_1():
    f = []
    v = input(str("Give me a word: "))
    while v != str("stop"):
        f.append(v)
        v = (input(str("Give me a word: ")))
    if v == str("stop"):
        print(f)
print(Lesson_7_1())

#lesson7.2:
def Lesson_7_2():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(l)
    d = [10 ,9 ,8 ,7 ,6 ,5, 4, 3, 2, 1]
    print(d)
    print("I might be cheating")
print(Lesson_7_2())