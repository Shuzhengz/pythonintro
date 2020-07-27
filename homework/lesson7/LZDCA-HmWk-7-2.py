My_Arr = ["The ", "array ", "needs ", "to ", "be ", "reversed."]

New_Arr = []

n = len(My_Arr)
#print(n)

#r = range(n)

idx = 0
#while idx in r:
while idx < n:
    #print(idx)
    #print(n-idx)
    New_Arr.append(My_Arr[n-idx-1])
    idx = idx + 1

# The original array and reversed array are:
print("the original array is:    ", end = ' '),  print(My_Arr)
print("the reversed array is:    ", end = ' '),  print(New_Arr) 