# Use the turtle module and the listen(), onkey(), onkeypress() methods
import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()


def move_forward():
    my_turtle.forward(10)


my_screen.listen()  # Keeps listening for a key to be pressed - no need for a while loop?
my_screen.onkey(key="space", fun=move_forward)  # Function as an input - onkey() is a higher-order function

my_screen.exitonclick()
