class Robot:
    def __init__(self, H_Pos, Arm_V_Pos, Has_Cube, ScorePoints):
        self.Position = H_Pos
        self.Arm_Position = Arm_V_Pos
        self.Has_Cube = Has_Cube
        self.ScorePoints = ScorePoints

    def Move(self, H_Steps):
        self.Position += H_Steps
    
    def Arm_Raise(self, V_Steps):
        self.Arm_Position += V_Steps

    def Cube_PickupOrDrop(self, pd):
        if pd == 1:
            # ROBOT CAN PICK UP A CUBE ONLY WHEN ROBOT AT SPACE 3 WITH ARM LOCATION AT GROUND
            if self.Position == 3 and self.Arm_Position == 0:
                self.Has_Cube = True
        elif pd == -1:
            if self.Has_Cube:
                self.Has_Cube = False
            else:
                print("The robot has nothing to drop.")
        else:
            print("Only 1 or -1 is a allowed operation command!")
    
    def Cube_Drop(self):
        if self.Has_Cube:
            self.Has_Cube = False
        else:
            print("The robot has nothing to drop.")

    def Score(self, so):
        if self.Position == 7 and self.Arm_Position == 10 and self.Has_Cube and so == 1:
            self.ScorePoints += 1
            self.Has_Cube = False


#####  ROBOT STARTS  #####
MyRobot = Robot(0, 0, False, 0)
#MyRobotInfo = [str(MyRobot.Position), str(MyRobot.Arm_Position), str(MyRobot.Has_Cube), str(MyRobot.ScorePoints)]
MyRobotInfo = [(MyRobot.Position), (MyRobot.Arm_Position), (MyRobot.Has_Cube), (MyRobot.ScorePoints)]
print(MyRobotInfo)
print("\n")


op = 0
# op == 1 :     MOVE FORWARD/BACKWARD
# op == 2 :     ARM RAISE/DROP
# op == 3 :     PICKUP/DROP A CUBE
# op == 5 :     SCORE

while op != 99:
    op = int(input("Specify the operation of the robot:  "))
    if op == 1:     # MOVE HORIZONTALLY
        hs = int(input("How many steps the robot is to move horizontally (negative steps means moving backwards):  "))
        MyRobot.Move(hs)
    elif op == 2:   # RAISE ARM
        ar = int(input("How many steps the robot's arm is to raise vertically (negative steps means moving down):  "))
        MyRobot.Arm_Raise(ar)
    elif op == 3:   # PICK UP A CUBE
        pd = int(input("Have the robot pickup or drop a cube?  (1: Pickup;   -1: Drop):    "))
        MyRobot.Cube_PickupOrDrop(pd)
    elif op == 5:  # SCORE
        s = int(input("Do you want to score now? (1: Score;  Others: Don't score)   "))
        MyRobot.Score(s)

    MyRobotInfo.pop()
    #MyRobotInfo = [str(MyRobot.Position), str(MyRobot.Arm_Position), str(MyRobot.Has_Cube), str(MyRobot.ScorePoints)]
    MyRobotInfo = [(MyRobot.Position), (MyRobot.Arm_Position), (MyRobot.Has_Cube), (MyRobot.ScorePoints)]

    if op != 99:
        print("\n")
        print(MyRobotInfo)
        print("\n")
        #print("Robot position is:        " + str(MyRobot.Position))
        #print("Robot arm position is:    " + str(MyRobot.Arm_Position))
        #print("Robot has a cube:         " + str(MyRobot.Has_Cube))
        #print("Robot has score:          " + str(MyRobot.ScorePoints))

#    #MyRobot.pop()
#    MyRobotInfo = [MyRobot.Position, MyRobot.Arm_Position, MyRobot.Has_Cube, MyRobot.ScorePoints]
