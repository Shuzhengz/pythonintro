UserInfo = ["Li Zhang", "Blue"]
n = input("User specify number of pets: ")
UserInfo.append(n)
ToBePrinted = UserInfo[0] + "'s favorite color is " + UserInfo[1] + ". He has "
if int(UserInfo[2]) == 0:
    ToBePrinted = ToBePrinted + "no pet"
else:
    ToBePrinted = ToBePrinted + UserInfo[2] + " pets"
#
# 
print(ToBePrinted)