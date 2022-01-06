# Python program to implement a basic Pong game
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score_keeper import ScoreBoard

PADDLE_RIGHT_X = 390
PADDLE_LEFT_X = -390

# Create the screen
screen = Screen()
screen.title("Python Pong Game")
screen.bgcolor("black")
screen.setup(width=900, height=700)
screen.tracer(0)
print(screen.screensize(800, 600))

# Drawing the border
boundary = Turtle()
boundary.hideturtle()
boundary.pensize(1)
boundary.color("white")
boundary.penup()
boundary.goto(-400, 300)
boundary.pendown()
for _ in range(2):
    boundary.forward(800)
    boundary.right(90)
    boundary.forward(600)
    boundary.right(90)

boundary.penup()
boundary.goto(0, 295)
boundary.pensize(2)
# boundary.color("white")
boundary.right(90)
for _ in range(30):
    boundary.pendown()
    boundary.forward(10)
    boundary.penup()
    boundary.forward(10)

# Create and move paddle objects
paddle_right = Paddle(20, 100, PADDLE_RIGHT_X, 0)
paddle_left = Paddle(20, 100, PADDLE_LEFT_X, 0)
screen.update()

# Create and move the ball object
ball = Ball()

# Create scoreboards
score_board_left = ScoreBoard(-400, "LEFT")
score_board_right = ScoreBoard(400, "RIGHT")

screen.listen()
screen.onkeypress(key="Up", fun=paddle_right.move_up)
screen.onkeypress(key="Down", fun=paddle_right.move_down)
screen.onkeypress(key="w", fun=paddle_left.move_up)
screen.onkeypress(key="s", fun=paddle_left.move_down)

game_on = True
while game_on:
    screen.update()
    ball.move()  # Starts with upward movement for a new game

    # Detect collision with the top and bottom walls and bounce
    if ball.ycor() > 281 or ball.ycor() < -280:  # Check for top and lower walls
        ball.bounce_up_down()

    # Detect collision with the paddle and bounce back
    if ball.xcor() >= PADDLE_RIGHT_X - 21 and ball.distance(paddle_right) < 50:
        print(f"Ball hit paddle {ball.distance(paddle_right)}")
        ball.bounce_front_back()

    if ball.xcor() <= PADDLE_LEFT_X + 21 and ball.distance(paddle_left) < 50:
        ball.bounce_front_back()

    # Detect if ball goes beyond the right and left walls
    if ball.xcor() > 400:  # Right player loses point
        print("Point for Left Player")
        score_board_left.increase_score()  # Keep scorecard
        ball.color("red")
        screen.update()
        ball.reset_position()
    elif ball.xcor() < -400:  # Left player loses point
        print("Point for Right Player")
        score_board_right.increase_score()  # Keep scorecard
        ball.color("red")
        screen.update()
        ball.reset_position()

screen.exitonclick()
