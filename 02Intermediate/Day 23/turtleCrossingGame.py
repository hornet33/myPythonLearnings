import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Drawing start and finish lines
line = Turtle()
line.penup()
line.goto(-299, -260)
line.pendown()
line.pensize(2)
line.forward(600)
line.hideturtle()
line.penup()
line.goto(-299, 270)
line.color("green")
line.pendown()
line.forward(600)

# Create random cars
car_manager = CarManager()

# Create the turtle player
player = Player()

# Create scoreboard
score_board = Scoreboard()

# Screen listeners
screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Move the cars on the screen
    car_manager.move()

    # Check if player has crossed safely
    if player.has_crossed_safely():
        score_board.level_up()
        car_manager.level_up()
        player.send_to_start()

    # Check if player has collided with a car
    if car_manager.has_collided_with_player(player):
        score_board.game_over()
        game_is_on = False
        player.color("red")
        screen.update()

screen.exitonclick()


