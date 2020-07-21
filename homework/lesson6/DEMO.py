numbers = [1, 2, 3, 5, 8, 13]
x = {"2" : 1, "5" : 2}
print(numbers[4])

numbers.append(numbers[4])
print([numbers])

numbers[6] = 21
print(numbers)

print(12 in numbers)

y = input("Please input a number ")
if y in x:
    print (str(x[y]))