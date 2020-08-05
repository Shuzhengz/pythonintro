def age_can_do():
    name = input("what is your name? ").upper()
    print("please input your age in numbers only.")
    age = input("What is your age? ")
    if (name == "SEAN" or name == "SHUHENG"):
        print("Sean, you suck.")
    elif int(age) <0:
        print("Go to another universe. You can't exist in this one.")
    elif int(age) < 14 and int(age) >= 0:
        print("You can stay alive.")
    elif int(age) >= 14 and int(age) < 16:
        print("You can stay alive and join the robotics team.")
    elif int(age) >= 16 and int(age) <18:
        print("You can stay alive, join the robotics team, drive and get a job.")
    elif int(age) >= 18 and int(age) <21:
        print("You can stay alive, join the robotics team, drive, get a job and attend college.")
    elif int(age) >= 21 and int(age) <35:
        print("You can stay alive, join the robotics team, drive, get a job, attend college, and be an adult.")
    elif int(age) >= 35 and int(age) < 50:
        print("You can stay alive, join the robotics team, drive, get a job, attend college, be an adult, and become President.")
    elif int(age) >= 50 and int(age) < 150:
        print("If its legal, just do your thing, BOOMER.")
    elif int(age) >= 150 and int(age) < 500:
        print("You can go commit deathpacito.")
    else:
        print("Bruh. Stop trying to troll.")

age_can_do()