# Python program to implement a basic Snake game
import time
import turtle
from snake import Snake

# Screen settings
screen = turtle.Screen()


def set_screen():
    """Function to set the screen to desired properties"""
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.title("Python Snake Game")
    screen.tracer(0)  # Switching off the tracer


set_screen()  # Set the screen
snake = Snake()  # Start the snake in initial position
screen.update()  # Will update the screen to show the current contents of the screen

# Screen listeners for key press
screen.listen()
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)

# Game play on!
game_on = True
while game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()


screen.exitonclick()
