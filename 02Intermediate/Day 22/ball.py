import random
from turtle import Turtle
from game_data import *
import time

BALL_COLOR = "yellow"
INITIAL_MOVE_LIST = [10, -10]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.goto(0, 0)
        self.color(BALL_COLOR)
        self.setheading(45)
        self.x_move = random.choice(INITIAL_MOVE_LIST)
        self.y_move = self.x_move
        # self.y_move = random.randint(10, 25)

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
        self.forward(1)
        time.sleep(START_SPEED)

    def bounce_up_down(self):
        self.y_move *= -1

    def bounce_front_back(self):
        self.x_move *= -1

    def reset_position(self):
        self.color(BALL_COLOR)
        time.sleep(1)
        self.goto(0, 0)
        self.bounce_front_back()  # So that the opposite player gets the first paddle after winning the point
