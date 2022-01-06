# Python class for the food functionality used in the snakeGame.py program
import random
import turtle


class Food(turtle.Turtle):
    def __init__(self,):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # Making the circle half the size of the snake block
        self.color("orange")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        self.goto(random_x, random_y)
