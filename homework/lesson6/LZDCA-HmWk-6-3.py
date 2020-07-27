#items = {123 : 'milk' , 124 : 'Cheese'}
#print(items.get(123))

Accnts = {
            1 : '$1000' , 
            2 : '$2000' , 
            3 : '$3000' , 
            4 : '$4000' , 
            5 : '$5000' , 
            6 : '$6000', 
            7 : '$7000' , 
            8 : '$8000' , 
            9 : '$9000' , 
            10 : '$10000'
         }
#Accnts = dict([('01' : '1000'), ('02' : '2000')])


UserAccnt = input("Check user's account: ")
#print("User account " + UserAccnt)
print("User account " + UserAccnt + " has " + Accnts.get(int(UserAccnt)) + "\n" + "\n")



Accnts.pop(4)


r = range(1, 11)
for idx in r:
    print(Accnts.get(idx))
