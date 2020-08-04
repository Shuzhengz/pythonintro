def array_func():
    Words = ["hello", "world", "of", "tanks", "video", "games", "phantom", "forces", "stupid", "hackers"]
    user = input("Please input a word (no capitals): ")
    if (user in Words) is False:
        Words.append(user)
        print("Added new word to array")
        print(Words)
    else:
        print("The word you just entered is already in the system")

array_func()

