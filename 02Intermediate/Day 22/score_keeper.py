# Python class for the score keeping functionality for the smakeGame program
import turtle

SCORE_COLOR = "orange"


class ScoreBoard(turtle.Turtle):
    def __init__(self, x_pos, player):
        super().__init__()
        self.player = player
        self.shape()
        self.penup()
        self.score = 0
        self.color(SCORE_COLOR)
        self.goto(x_pos, 305)
        if x_pos > 0:
            self.align = "right"
        else:
            self.align = "left"

        self.write(f"{self.player} SCORE: {self.score}", move=False, align=self.align, font=("Tahoma", 14, "bold"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.player} SCORE: {self.score}", move=False, align=self.align, font=("Tahoma", 14, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER - RESTARTING GAME!", move=False, align="center", font=("Tahoma", 20, "bold"))
