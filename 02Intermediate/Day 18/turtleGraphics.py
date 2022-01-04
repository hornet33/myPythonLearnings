import turtle
from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=1.0, height=1.0)  # Maximize screen
turtle.colormode(255)  # Changed turtle's colormode to support rgb(0-255) mode


def set_my_turtle(t):
    t.shape("turtle")
    t.color("green3")
    t.speed(8)
    return t


def set_my_screen(s, t):
    s.reset()
    t = set_my_turtle(t)
    return t


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


# My turtle properties
my_turtle = Turtle()
# my_turtle = set_my_screen(screen, my_turtle)
#
# # Draw a square
# for _ in range(1, 5):
#     my_turtle.forward(100)
#     my_turtle.right(90)
#
# # Screen clear
# my_turtle = set_my_screen(screen, my_turtle)
#
# # Draw a dashed line
# for _ in range(10):
#     my_turtle.pendown()
#     my_turtle.forward(5)
#     my_turtle.penup()
#     my_turtle.forward(5)
# my_turtle.showturtle()
#
# # Reset screen and turtle
# my_turtle = set_my_screen(screen, my_turtle)
#
# # Draw geometric shapes from 3 sides (triangle) to 10 sides
# for sides in range(3, 11):
#     degree = 360 / sides
#     print(f"{degree} - {sides}")
#     for _ in range(sides):
#         my_turtle.forward(100)
#         my_turtle.right(degree)

# Draw a random walk
my_turtle = set_my_screen(screen, my_turtle)
my_turtle.pensize(10)  # Thick pen size
# 4 orientations - 0 (East), 90 (North), 180 (West), 270 (South)
degree_top_bottom = [90, 270]
degree_right_left = [0, 180]
degree = [degree_right_left, degree_top_bottom]
current_degree = random.choice(degree[random.randint(0, 1)])

for _ in range(400):
    my_turtle.setheading(current_degree)  # Random orientation
    my_turtle.color(get_random_color())  # Random color
    my_turtle.forward(20)  # Move
    # last_degree = current_degree
    # if last_degree in degree_right_left:
    #     current_degree = random.choice(degree_top_bottom)
    # elif last_degree in degree_top_bottom:
    #     current_degree = random.choice(degree_right_left)
    current_degree = random.choice(degree[random.randint(0, 1)])


# # Draw a circle of circles in random colors
# my_turtle = set_my_screen(screen, my_turtle)
# my_turtle.speed(0.25)
# turns = 200
# degree = 360 / turns
# for _ in range(turns):
#     my_turtle.circle(100)
#     # my_turtle.right(degree)
#     my_turtle.setheading(my_turtle.heading() + degree)
#     my_turtle.color(get_random_color())

# Code to keep the screen alive until the end of the program
screen.exitonclick()
