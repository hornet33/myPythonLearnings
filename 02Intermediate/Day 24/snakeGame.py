# Python program to implement a basic Snake game
import time
import turtle
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score_keeper import ScoreBoard

# Screen settings
screen = Screen()
start_game = turtle.Turtle()  # To type the starting text


def set_screen():
    """Function to set the screen to desired properties"""
    screen.clear()
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


# Game play on!
def snake_play():
    """Function to play the snake game"""
    start_game.clear()  # Clear the "PRESS SPACEBAR TO CONTINUE" text to start game

    snake = Snake()  # Start the snake in initial position
    food = Food()  # Create food object
    score_board = ScoreBoard()  # Create score board

    # Screen listeners for key press
    screen.listen()
    screen.onkey(key="Up", fun=snake.turn_up)
    screen.onkey(key="Down", fun=snake.turn_down)
    screen.onkey(key="Left", fun=snake.turn_left)
    screen.onkey(key="Right", fun=snake.turn_right)

    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.12)
        snake.move()

        # Generate food and check if food eaten by snake
        if snake.head.distance(food) < 15:
            food.refresh()
            score_board.increase_score()
            snake.add_tail()

        # Detect if wall is hit
        if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
            game_on = False  # Game over

        # Detect if own part of the snake's body is hit
        for block in snake.snake_body[1:]:  # Slice excluding the head of the snake
            # if block == snake.head:
            #     continue
            # elif
            if snake.head.distance(block) < 1:
                game_on = False

    score_board.game_over()
    restart_on_game_over()

    snake = None
    score_board = None
    food = None


def restart_on_game_over():
    """Function to restart on game over"""
    time.sleep(2)
    start_screen()


def start_screen():
    set_screen()
    start_game.hideturtle()
    start_game.penup()
    start_game.color("yellow")
    start_game.goto(0, 0)
    start_game.write("PRESS SPACEBAR TO PLAY!", move=False, align="center", font=("Tahoma", 20, "bold"))
    screen.update()
    screen.listen()
    screen.onkey(key="space", fun=snake_play)


# Main logic
start_screen()
screen.exitonclick()
