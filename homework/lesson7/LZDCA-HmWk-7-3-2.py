UpperBond = 4000000

F1 = 1  #1st Fabonacci number
F2 = 2  #2nd Fabonacci number


Sum_Even_Fabonacci = 2
idx = 3

#while F1 + F2 < 4000000:
while (F1 + F2) < UpperBond:        # New Fabonacci number is F1 + F2
    if (F1 + F2) % 2 == 0:
        Sum_Even_Fabonacci = Sum_Even_Fabonacci + F1 + F2
    if idx % 2 == 0:
        F2 = F1 + F2
    else:
        F1 = F1 + F2
        
    
    idx = idx + 1
    #print("F1 = " + str(F1) + "    F2 = " + str(F2) + "    F_New = " + str(F1 + F2))
    
#Sum of even Fabonacci number below 4000000 is:       4613732
print("Sum of even Fabonacci number below " + str(UpperBond) + " is:  " + str(Sum_Even_Fabonacci))


