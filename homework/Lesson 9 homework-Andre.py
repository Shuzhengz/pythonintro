import os, time
print("Please do not start until you have finished reading this message.")
print("Press 's' to stop.")
print('''To move forward 1 meter, press 'f', to move backward 1 meter, press 'a'.
to raise the arm by 1 inch, press 'r', to lower the arm by 1 inch, press 'd'.
to grab the cube, press 'e', to score the cube, press 'c'.
After pressing one of these keys, press enter to execute the command.''')

class Robot:
    speed = "super fast"

    def __init__(self, arm_level, robot_pos, cube_storage, score):
        self.arm_level = arm_level
        self.robot_pos = robot_pos
        self.cube_storage = cube_storage
        self.score = score

    def arm_action(self, dist):
        self.arm_level += dist
    def robot_movement(self, dist):
        self.robot_pos += dist
    def cube_action(self, amount):
        self.cube_storage += amount
    def scored(self, amount):
        self.score += amount

my_robot = Robot(0, 0, 0, 0)
print("Hit enter to start.")
z = input("")
print("Started!")
time.sleep(1)
print("Arm Level: " + str(my_robot.arm_level))
print("Robot Position: " + str(my_robot.robot_pos))
print("Cubes: " + str(my_robot.cube_storage))
print("Score: " + str(my_robot.score))
while z != "s":    
    z = input("")
    if z != "s":
        if z == "r":
            if z == "r" and my_robot.arm_level < 15:
                my_robot.arm_action(1)
            else:
                print("You cannot raise the arm above position 15")
                time.sleep(2)
        elif z == "d":
            if my_robot.arm_level == 0:
                print("You cannot lower the arm below level 0.")
                time.sleep(2)
            else:
                my_robot.arm_action(-1)
        elif z == "f":
            if my_robot.robot_pos < 10:
                my_robot.robot_movement(1)
            else:
                print("You cannot go over position 10")
                time.sleep(2)
        elif z == "a":
            if my_robot.robot_pos == 0:
                print("You cannot go behind position 0")
                time.sleep(2)
            else:
                my_robot.robot_movement(-1)
        elif z == "e":
            if my_robot.robot_pos == 3 and my_robot.arm_level == 0 and my_robot.cube_storage == 0:
                my_robot.cube_action(1)
            else:
                print("To pick up a cube, you must be at position 3, the arm must be at position 0, and there cannot be another cube in the storage.")
                time.sleep(3)
        elif z == "c": 
            if my_robot.robot_pos == 7 and my_robot.cube_storage == 1 and my_robot.arm_level == 10:
                        my_robot.scored(3) 
                        my_robot.cube_action(-1)
            else:
                print("To score, you must have a cube, be at position 7, and have the arm at 10.")
                time.sleep(2.5)
        else:
            print("This command doesn't exist.")
            time.sleep(2)
        os.system('cls')
        print("Arm Level: " + str(my_robot.arm_level))
        print("Robot Position: " + str(my_robot.robot_pos))
        print("Cubes: " + str(my_robot.cube_storage))
        print("Score: " + str(my_robot.score))
    else:
        print("Congrats! You scored " + str(my_robot.score) + " points! Have a good day!")
        time.sleep(5)
        os.system('cls')






        

    
