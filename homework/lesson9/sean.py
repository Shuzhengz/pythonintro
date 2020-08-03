class Robot:
    def __init__(self, pos, arm_pos, cube, score):
        self.pos = pos
        self.arm_pos = arm_pos
        self.cube = cube
        self.score = score

    def drive(self, dist):
        self.pos += dist

    def cube_gone(self, gone):
        self.cube -= gone
    def arm_height(self, arm_up):
        self.arm_pos += arm_up

    def cube_in_arm(self, cube_in_hands):
        if self.cube == 0:
            if self.pos == 3:
                if self.arm_pos == 0:
                    self.cube += cube_in_hands
                else:
                    print("You are not in the right ar hieght. ")
            else:
                print("You are not in postion to pick up the cube. ")
        else:
            print("You have a cube already. ")

    def points(self, add_points):
        if self.cube == 1:
            if self.pos == 7:
                if self.arm_pos == 10:
                    self.score += add_points
                else:
                    print("You arm is not high enough. ")
            else:
                print("You did not reach the scoreing point. ")
        else:
            print("You don't have a cube. ")


my_robot = Robot(0, 0, 0, 0)
while my_robot.score != 15:
    a = int(input("How much do you want to go forword? "))
    my_robot.drive(a)
    print(my_robot.pos, my_robot.arm_pos, my_robot.cube, my_robot.score)
    b = int(input("How much do you want to lift your arm? "))
    my_robot.arm_height(b)
    if my_robot.pos == 3 and my_robot.arm_pos == 0:
        my_robot.cube_in_arm(1)
    if my_robot.pos == 7 and my_robot.arm_pos == 10 and my_robot.cube == 1:
        my_robot.points(5)
        my_robot.cube_gone(1)
    print(my_robot.pos, my_robot.arm_pos, my_robot.cube, my_robot.score)