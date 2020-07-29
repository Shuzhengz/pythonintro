My_List = []
iCnt = 0

uw = ""
while uw != "Stop":
    uw = input("User input a word: ")
    #print(uw == "Stop")
    My_List.append(uw)
    iCnt = iCnt + 1
    #print(My_List[icnt-1])
    if uw == "Stop":
        My_List.pop(iCnt-1)
        iCnt = iCnt - 1

print(My_List)
print(My_List[iCnt-1])    


#r = range(1, iCnt+1)
print(len(My_List))
print(iCnt)


r = range(len(My_List))
for idx in r:
    print(My_List[idx])