import turtle
import pandas

BG_IMG = "blank_states_img.gif"  # Path to the background image
STATE_DATA = "50_states.csv"  # Path to the states data file

screen = turtle.Screen()
screen.title("US State Game")

# Set the background image as the screen background - turtle works only with gif images
screen.addshape(BG_IMG)
turtle.shape(BG_IMG)

# List to store the correct guesses made so far
correct_guessed_states = []

# Get States data
states_data = pandas.read_csv(STATE_DATA)
states_list = states_data.state.to_list()

while len(correct_guessed_states) < 50:
    # Get user input
    user_answer = screen.textinput(title=f"{len(correct_guessed_states)}/50 - Guess The State",
                                   prompt="Enter the name of the state:").title()
    print(user_answer)

    # Type "exit" to exit the game
    if user_answer == "Exit":
        # Save the list of states not guessed in a csv file

        # ******* Method 1 - Without using List Comprehension get the list of states not guessed correctly
        # states_missed = []
        # for state in states_list:
        #     if state not in correct_guessed_states:
        #         states_missed.append(state)

        # ******* Method 2 - Using List Comprehension get the list of states not guessed correctly
        states_missed = [state for state in states_list if state not in correct_guessed_states]

        # Convert to a Data Frame using the states missed list
        data = pandas.DataFrame(states_missed)
        # Save to a csv file
        data.to_csv("states_to_learn.csv")
        # Exit the while loop
        break

    if user_answer in states_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data_row = states_data[states_data.state == user_answer]
        t.goto(int(state_data_row.x), int(state_data_row.y))
        t.write(state_data_row.state.item())  # Get the actual data without the other info
        correct_guessed_states.append(user_answer)
