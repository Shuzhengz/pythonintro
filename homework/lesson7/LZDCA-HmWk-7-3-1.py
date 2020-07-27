#r = range(1, 10)
#
#for idx in r:
#    print(((idx % 3) == 0) or ((idx % 5) == 0))
# 

Sum_Multiples = 0

idx = 1
UpperBond = 1000


print("START")

#while idx < 30 and (((idx % 3) != 0) or ((idx % 5) != 0)):
while idx < UpperBond :
    if (((idx % 3) == 0) or ((idx % 5) == 0)):
        Sum_Multiples = Sum_Multiples + idx
        #print("Sum of multiple is:    " + str(Sum_Multiples) + "\n")
    #else:
        #print("idx = " + str(idx))
        #print(idx % 3)
        #print(idx % 5)
    
    idx  = idx + 1
    #if idx > 50:
    #    break

# Sum of multiple is:    233168
print("Sum of multiple is:    " + str(Sum_Multiples) + "\n")



