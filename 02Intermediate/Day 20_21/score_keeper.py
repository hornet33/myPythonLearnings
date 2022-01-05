# Python class for the score keeping functionality for the smakeGame program
import turtle


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()

        self.shape()
        self.penup()
        self.score = 0
        self.color("yellow")
        self.goto(0, 305)
        self.write(f"SCORE: {self.score}", move=False, align="center", font=("Tahoma", 10, "bold"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", move=False, align="center", font=("Tahoma", 10, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", move=False, align="center", font=("Tahoma", 20, "bold"))
