def add(a, b):
    return a % b

x = add (int(input("Put the number that is being divided: ")), int(input("Put the number that is going to divide: ")))
print(x)
if x == 0:
    print("It is divisable. ")
else:
    print("It is not divisable. ")