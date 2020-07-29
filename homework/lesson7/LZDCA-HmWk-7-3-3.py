prime = [1]

GivenNumber = 600851475143 
IterNumber = GivenNumber

idx = 2

while idx <= IterNumber:
    if IterNumber % idx == 0:
        IterNumber = IterNumber / idx

        prime.append(idx)
        #print(prime)
        #print("New prime is:  " + str(idx))
    
    idx = idx + 1

Prime_Max = 1
for idx in prime:
    if idx > Prime_Max:
        Prime_Max = idx

# The The maximum prime for the given number is:  6857
print("The maximum prime for number " + str(GivenNumber) + " is:  " + str(Prime_Max))

