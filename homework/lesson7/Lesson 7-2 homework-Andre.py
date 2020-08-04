def reverse_array():    
    print("Please input words or numbers for the array when prompted. To stop, type stop (this code is case sensitive, so please add no uppercase letters).")
    user_input_array = []
    x = 0
    while x != "stop":
        userinput = input("What word or number would you like to add to the array? ")
        if userinput == "stop":
            x = "stop"
        elif (userinput in user_input_array) is True:
            print("The word you entered is already in the array.")
        else: 
            user_input_array.append(userinput)
            print("added")
    rev_array = []
    x = len(user_input_array)
    z = 1
    y = user_input_array[x - z]
    while x != z - 1:
        y = user_input_array[x - z]
        x = len(user_input_array)
        rev_array.append(y)
        z = z + 1
    print("The reversed array is:" + str(rev_array))

reverse_array()