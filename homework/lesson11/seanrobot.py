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
        self.cube += cube_in_hands

    def points(self, add_points):
        self.score += add_points

my_robot = Robot(0, 0, 0, 0)