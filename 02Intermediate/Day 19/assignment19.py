# Python program to implement a turtle race
import random
import turtle

# Set the screen configurations
my_screen = turtle.Screen()
screen_width = 500
screen_height = 400
my_screen.setup(width=screen_width, height=screen_height)

# Globals
all_turtles = []
colors = ['blue', 'green', 'red', 'yellow', 'orange', 'black']
lane_space = 50
start_x = -1 * (screen_width / 2) + 15
start_y = -1 * ((screen_height / 2) - (lane_space * 2))
end_x = (screen_width / 2) - lane_space
current_y = start_y

# 6 turtles in the race - create their objects and add to the all_turtles list along with colour and start_x position
for _ in range(6):
    color = random.choice(colors)
    new_turtle = turtle.Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.setposition(start_x, current_y)
    new_turtle.speed("fastest")
    current_y += lane_space

    turtle_data = [new_turtle, color, start_x]
    all_turtles.append(turtle_data)
    colors.remove(color)

# Turtle object to draw a finish line on the screen
end_line_turtle = turtle.Turtle()
end_line_turtle.speed("fastest")
end_line_turtle.penup()
end_line_turtle.goto(end_x, current_y)
end_line_turtle.pensize(4)
end_line_turtle.pendown()
end_line_turtle.right(90)
end_line_turtle.forward(lane_space * 8)
end_line_turtle.hideturtle()

# Take user input to bet on a turtle to win the race
user_bet = my_screen.textinput(title="Turtle Race Betting", prompt="Which turtle colour you want to bet on?")
print(f"Okay - you selected {user_bet} color turtle!")

race_on = True
winning_turtle = []  # Will store the details of the turtle that wins the race
print("RACE IS ON ! ! !")

# Loop until race is on
while race_on:
    # For all turtles, randomly move forward by 1-10 steps
    for current_turtle in all_turtles:
        s = random.randint(1, 10)
        current_turtle[0].forward(s)
        current_turtle[2] += s  # Keep track of where the current turtle is on the x axis

        # If the current turtle has reached the finish line (end_x)
        if current_turtle[2] >= end_x:
            race_on = False
            winning_turtle = current_turtle
            break

print("RACE COMPLETED ! ! !")

if user_bet == winning_turtle[1]:
    print(f"AWESOME!!! Your {user_bet} color turtle won the race!")
else:
    print(f"Sorry, {user_bet} color turtle lost! The {winning_turtle[1]} color turtle won the race.")

my_screen.exitonclick()
