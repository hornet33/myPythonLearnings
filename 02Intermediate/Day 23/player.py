from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 270


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.left(90)
        self.color("green")
        self.goto(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def has_crossed_safely(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False

    def send_to_start(self):
        self.goto(STARTING_POSITION)
