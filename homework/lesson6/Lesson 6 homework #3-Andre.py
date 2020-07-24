user1 = "Billy Bob Joe III"
user2 = "Jhonny Didn't Eat Sugar"
user3 = "Hacking Shotgun Memer"
userlogin = input("What is your username? ")
if userlogin == "Billy Bob Joe III":
    print("Welcome Billy.")
    RetirementSavings = dict({1776 : 999999999})
    VacationBudget = dict({1917 : 500000})
    GamingBudget = dict({2012 : 1000000})
    user1account = {0000 : RetirementSavings , 0o0001 : VacationBudget , 0o0010 : GamingBudget}
    print(user1account.get(0o0001))
    user1account = user1account.get(int(input("What is the ID of the account you want to open? ")))
    accountbalance = user1account.get(int(input("What is your password? ")))
    if accountbalance == None:
        while accountbalance == None:
            print("The password you entered is incorrect. Please try again.")
            accountbalance = user1account.get(int(input("What is your password? ")))
            print(accountbalance)
    else:
            print(accountbalance)

elif userlogin == "Jhonny Didn't Eat Sugar":
    SugarSpendingBudget = dict({19217117 : 100000000000000000000})
    BribePapaBudget = dict({1415 : 999999999})
    TaxiEscapeBudget = dict({172114 : 999})
    user2accounts = {0o0011 : SugarSpendingBudget , 0o0100 : BribePapaBudget, 0o0101 : TaxiEscapeBudget}
    user2input = input("What is the ID of the account you want to open? ")
    if accountbalance == None:
        while accountbalance == None:
            print("The password you entered is incorrect. Please try again.")
            accountbalance = user2accounts.get(int(input("What is your password? ")))
            if accountbalance == 999999999:
                print(accountbalance)
            else:
                print("")
    else:
        user2accounts = user2accounts.get(int(user2input))
        accountbalance = user2accounts.get(int(input("What is your password? ")))
        if accountbalance == None:
            while accountbalance == None:
                print("The password you entered is incorrect. Please try again.")
                accountbalance = user2accounts.get(int(input("What is your password? ")))
                if accountbalance == 999999999:
                    print(accountbalance)
                else:
                    print("")
else:
    print("This account does not exist at this time.")









#P.S. Jhonny's SugarSpending Budget's password is the numerical version of sugar if a = 1, b = 2, c = 3, etc. (19 = s, 21 = u, 7 = g, 1 = a, 17 = r). His other passwords are words too. 
#(Also, the other passwords have hidden meanings too, but are not necessarily words)