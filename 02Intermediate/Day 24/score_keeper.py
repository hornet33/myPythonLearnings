# Python class for the score keeping functionality for the smakeGame program
import turtle

HIGH_SCORE_FILE = "scorefile.txt"


def get_high_score():
    with open(HIGH_SCORE_FILE, mode="r") as score_file:
        high_score = score_file.read()
        print(high_score)
        # if high_score == None:
        #     return 0
        return high_score


def update_high_score(new_high_score):
    with open(HIGH_SCORE_FILE, mode="w") as score_file:
        score_file.write(str(new_high_score))


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()

        self.shape()
        self.penup()
        self.score = 0
        self.high_score = get_high_score()
        self.color("yellow")
        self.goto(0, 305)
        self.refresh_scoreboard()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score} | HIGH SCORE: {self.high_score}", move=False, align="center",
                   font=("Tahoma", 10, "bold"))

    def game_over(self):
        self.reset_scores()
        self.goto(0, 0)
        self.write("GAME OVER - RESTARTING GAME!", move=False, align="center", font=("Tahoma", 20, "bold"))

    def reset_scores(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            update_high_score(self.high_score)
        self.refresh_scoreboard()

