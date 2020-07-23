# HOMEWORK : LESSON 4 : CONDITIONS AND BOOLEANS

a = "You can join robotics team"
b = "You can drive and get a job"
c = "You can attend college"
d = "Congratulations! You are a adult"
e = "You can be a President"


AGE = int(input("Please specify your age: "))
print(AGE)

if AGE >= 14 and AGE < 16:
    print(a)
elif AGE >= 16 and AGE < 18:
    print(b)
elif AGE >= 18 and AGE < 21:
    print(c)
elif AGE >= 21 and AGE < 35:
    print(d)
else:
    print(e)

