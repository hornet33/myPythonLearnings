from turtle import Turtle
from game_data import *

PADDLE_COLOR = "white"


class Paddle(Turtle):
    def __init__(self, width, height, x_pos, y_pos):
        super().__init__()
        self.width = width
        self.height = height
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(x_pos, y_pos)

    def move_up(self):
        print(f"UP - {self.ycor()} - {TOP_WALL}")
        if self.ycor() >= TOP_WALL:
            return
        self.goto(self.xcor(), self.ycor() + self.width)

    def move_down(self):
        print(f"DOWN - {self.ycor()} - {BOTTOM_WALL}")
        if self.ycor() <= BOTTOM_WALL:
            return
        self.goto(self.xcor(), self.ycor() - self.width)
