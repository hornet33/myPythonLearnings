# Accessing classes and objects and class attribute/methods in Python
from turtle import Turtle, Screen  # In-built Python library

my_turtle = Turtle()  # Creating an object of the class Turtle from package turtle
# Classes are named in Pascal case ("JustLikeThis" - every word starts with a capital letter)
my_turtle.home()
my_turtle.shape("turtle")
my_turtle.color("green3")
my_turtle.forward(100)

my_screen = Screen()  # Object of class Screen
print(my_screen.canvheight)  # Accessing a class attribute through the object
my_screen.exitonclick()  # Accessing a class method through the object
