# Python program to randomly do a spot painting using colorgram and turtle
# import colorgram
#
# colors = colorgram.extract('image.jpg', 110)
# color_list_as_rgb = []
# for c in colors:
#     color_tuple = (c.rgb.r, c.rgb.g, c.rgb.b)
#     color_list_as_rgb.append(color_tuple)
import random
import turtle

turtle.colormode(255)  # This MUST be set to use rgb colours in 0-255 range

rgb_color_list = [(211, 154, 97), (52, 107, 132), (176, 78, 34), (238, 246, 243), (200, 142, 33), (116, 155, 171),
                  (124, 79, 98), (122, 175, 157), (229, 197, 128), (231, 238, 242), (190, 88, 109), (55, 38, 19),
                  (11, 51, 65), (44, 168, 125), (197, 122, 141), (50, 125, 120), (167, 21, 29), (225, 94, 80),
                  (244, 162, 160), (4, 28, 26), (38, 32, 34), (80, 148, 170), (162, 26, 21), (236, 165, 170),
                  (98, 125, 160), (167, 207, 192), (22, 79, 91), (162, 203, 212), (55, 62, 76), (31, 85, 82),
                  (184, 189, 203), (74, 65, 44)]

# Creating the objects
my_turtle = turtle.Turtle()
my_screen = turtle.Screen()
my_screen.setup(width=1.0, height=1.0)  # Maximize screen

# Setting the co-ordinates and dimensions
start_x = -225
start_y = 225
circle_radius = 20
space = 50

# Initialize x and y
x = start_x
y = start_y

# Setting turtle properties
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.speed(0)

# Looping to print the dots in specified size and random color from rgb_color_list
for _ in range(10):
    for _ in range(10):
        my_turtle.setposition(x, y)
        color = random.choice(rgb_color_list)
        my_turtle.dot(circle_radius, color)
        my_turtle.forward(space)
        x += space  # Move forward for the next dot on the same line
    y -= space  # For the next line, change the position of y (vertical)
    x = start_x  # Reset x to the start of the line

my_screen.exitonclick()
