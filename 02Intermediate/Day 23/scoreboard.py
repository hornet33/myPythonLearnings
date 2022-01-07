import time
from turtle import Turtle

SCORE_POSITION = (-290, 280)
FONT = ("Tahoma", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(SCORE_POSITION)
        self.color("black")
        self.write(f"LEVEL: {self.level}", move=False, align="left", font=FONT)

    def level_up(self):
        self.goto(0, 0)
        self.write("LEVEL UP!", move=False, align="center", font=FONT)
        time.sleep(1)
        self.clear()
        self.goto(SCORE_POSITION)
        self.level += 1
        self.write(f"LEVEL: {self.level}", move=False, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", move=False, align="center", font=FONT)
