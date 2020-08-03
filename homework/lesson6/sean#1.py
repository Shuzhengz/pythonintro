words = ["me", "he", "she", "you", "I", "his", "her", "it", "its", "us"]
x = input("give me a word. ")
print(x in words)
if (x in words) == True :
    print(words)
if (x in words) == False :
    words.append(str(x))
    print(words)