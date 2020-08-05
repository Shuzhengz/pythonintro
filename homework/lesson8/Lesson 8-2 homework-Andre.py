def dividing_func(x , y):
    return x % y 

x = int(input("Please input a dividend (number): "))
y = int(input("Please input a divisor (number): "))

if dividing_func(x , y) == 0:
    print("The number " +  str(x) + " is divisible by " + str(y) + ".")
else:
    print("The number " +  str(x) + " is not divisible by " + str(y) + ".")
    print("Their remainder is " + str(x % y) + ".")
