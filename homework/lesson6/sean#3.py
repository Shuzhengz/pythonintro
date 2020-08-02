x = {"1" : 100, "2" : 200, "3" : 300, "4" : 400, "5" : 500, "6" : 0, "7" : 0, "8" : 10000000, "9" : 0, "10" : 0}
y = input("Give me your password: ")
if y in x:
    print("You have " + str(x[y]) + " dollars in your account. ")
    input("Do you want to DELETE your account or your self or both or neither? ")
    x.pop(y)
    print("BOTH you and your account have been succesfuly DELETED. Thank you for being here, have a lovely day. ")
else:
    print("WRONG PASSWORD, have a lovely day.")