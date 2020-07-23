# HOMEWORK: LESSON 2 : VARIABLES
# THE CUSTOMER INPUTS ARE SKIPED. THEY ARE ASSIGNED HERE

import statistics

PZ1 = 1
PEPP1 = 21
OLIVE1 = 31

PZ2 = 2
PEPP2 = 22
OLIVE2 = 32

PZ3 = 3
PEPP3 = 23
OLIVE3 = 33

print("The average of customers' order is: ")
print("  " + str((PZ1 + PZ2 + PZ3) / 3) + " pizzas with \n  " + str((PEPP1 + PEPP2 + PEPP3) / 3) + " peppronis and \n  " + str((OLIVE1 + OLIVE2 + OLIVE3) / 3) + " olives.")

x = statistics.mean([1, 2, 3])
print("\n\n\nThe average of customers' order is: ")
print(str(x) + " pizzas")
