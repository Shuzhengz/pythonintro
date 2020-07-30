Words = ["Andre", "wants", "play", "games", "Mom", "says", "no", "bad", "Llst", "words"]
n = len(Words)
#print(n)
NewWord = input("Please input a word to check:")
Found = False
idx = 99
if NewWord == Words[0]:
    Found = True
    idx = 0
elif NewWord == Words[1]:
    Found = True
    idx = 1
elif NewWord == Words[2]:
    Found = True
    idx = 2
elif NewWord == Words[3]:
    Found = True
    idx = 3
elif NewWord == Words[4]:
    Found = True
    idx = 4
elif NewWord == Words[4]:
    Found = True
    idx = 4
elif NewWord == Words[5]:
    Found = True
    idx = 5
elif NewWord == Words[6]:
    Found = True
    idx = 6
elif NewWord == Words[7]:
    Found = True
    idx = 7
elif NewWord == Words[8]:
    Found = True
    idx = 8
elif NewWord == Words[9]:
    Found = True
    idx = 9


if Found:
    n = n + 1
    print("The word user input is in the list already.")
    print(Words[idx])
else:
    Words.append(NewWord)
    print("A new word is added. The new word is: ")
    print(NewWord)
