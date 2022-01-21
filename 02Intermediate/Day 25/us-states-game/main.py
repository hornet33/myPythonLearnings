import turtle

BG_IMG = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("US State Game")

# Set the background image as the screen background - turtle works only with gif images
screen.addshape(BG_IMG)
turtle.shape(BG_IMG)


screen.exitonclick()
