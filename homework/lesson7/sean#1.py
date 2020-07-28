x = []
y = input(str("Give me a word: "))
while y != str("stop"):
    x.append(y)
    y = (input(str("Give me a word: ")))
if y == str("stop"):
    print(x)