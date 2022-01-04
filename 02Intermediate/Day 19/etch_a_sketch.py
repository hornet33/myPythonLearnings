# Python program to implement a basic etch-a-sketch functionality
import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()


def move_forward():
    my_turtle.forward(10)


def move_back():
    my_turtle.back(10)


def rotate_clockwise():
    my_turtle.setheading(my_turtle.heading() + 10)
    move_forward()


def rotate_anti_clockwise():
    my_turtle.setheading(my_turtle.heading() - 10)
    move_forward()


def reset_screen():
    my_screen.reset()
    my_turtle.home()


my_screen.listen()

my_screen.onkey(key="w", fun=move_forward)
my_screen.onkey(key="s", fun=move_back)
my_screen.onkey(key="a", fun=rotate_anti_clockwise)
my_screen.onkey(key="d", fun=rotate_clockwise)
my_screen.onkey(key="c", fun=reset_screen)

my_screen.exitonclick()
