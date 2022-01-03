from turtle import Screen, Turtle

screen = Screen()

# My turtle properties
my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("green3")
my_turtle.speed(1)

# Draw a square
for _ in range(1, 5):
    my_turtle.forward(100)
    my_turtle.right(90)

#

# Code to keep the screen alive until the end of the program
screen.exitonclick()
