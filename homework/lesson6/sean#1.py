words = ["me", "he", "she", "you", "I", "his", "her", "it", "its", "us"]
x = input("give me a word. ")
print(x in words)
if (x in words) == True :
    print(words)
if (x in words) == False :
    words.append(str(x))
    print(words)

store = ["Name", "color", "x"]
y = input("What's your name? ")
store[0] = y
z = input("What is your favorite color? ")
store[1] = z
a = input("How many pets do you have? ")
store[2] = a
print(store[0] + "'s favorite color is " + store[1] + ". They have " + store[2] + " pets. ")