# Python program to implement a basic Snake game
import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score_keeper import ScoreBoard

# Screen settings
screen = Screen()


def set_screen():
    """Function to set the screen to desired properties"""
    screen.bgcolor("black")
    screen.setup(width=650, height=650)
    screen.title("Python Snake Game")
    boundary = Turtle()
    boundary.hideturtle()
    boundary.pensize(2)
    boundary.color("white")
    boundary.speed("fastest")
    boundary.penup()
    boundary.goto(-300, 300)
    boundary.pendown()
    boundary.forward(600)
    for _ in range(3):
        boundary.right(90)
        boundary.forward(600)

    screen.tracer(0)  # Switching off the tracer


set_screen()  # Set the screen
snake = Snake()  # Start the snake in initial position
food = Food()  # Create food object
score_board = ScoreBoard()  # Create score board
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
    time.sleep(0.15)
    snake.move()

    # Generate food and check if food eaten by snake
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.add_tail()

    # Detect if wall is hit
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_on = False  # Game over
        score_board.game_over()

    # Detect if own part of the snake's body is hit
    for block in snake.snake_body:
        if block == snake.head:
            continue
        elif snake.head.distance(block) < 1:
            game_on = False
            score_board.game_over()

screen.exitonclick()
