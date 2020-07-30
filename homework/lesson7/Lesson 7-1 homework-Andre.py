user_input_array = []
x = 0
while x != "stop":
    userinput = input("What word would you like to add to the array? ")
    if userinput == "stop":
        x = "stop"
    elif (userinput in user_input_array) is True:
        print("The word you entered is already in the array.")
    else: 
        user_input_array.append(userinput)
print(user_input_array)

