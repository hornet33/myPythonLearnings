# Python program to simulate a simple coffee maker system including inventory and cash transactions
from coffee_data import *
from helpers.utilities import *

# Storing as Globals to avoid typos
ESPRESSO = "espresso"
LATTE = "latte"
CAPPUCCINO = "cappuccino"
INGREDIENTS = "ingredients"
MILK = "milk"
WATER = "water"
COFFEE = "coffee"
COST = "cost"
MONEY = "money"
VALID_USER_INPUT = [ESPRESSO, LATTE, CAPPUCCINO, 'report', 'off']
# Add a new item to the resources' dictionary to keep track of the money made
resources[MONEY] = 0


# Function to print the report of the resources
def print_report():
    """Function to print the report of the resources"""
    print("-----------")
    print("R E P O R T")
    print("-----------")
    print(f"Water   : {resources[WATER]} ml")
    print(f"Milk    : {resources[MILK]} ml")
    print(f"Coffee  : {resources[COFFEE]} g")
    print(f"Money   : ${get_formatted_two_decimals(resources[MONEY])}")
    print("")


# Function to take user input and check validity of input
def get_user_choice_of_coffee():
    """Function to take user input and check validity of input"""
    print("Welcome to Python Coffee Maker!")
    print("-------------------------------")
    user_choice = input("What would you like (Espresso / Latte / Cappuccino): ").lower()
    while user_choice not in VALID_USER_INPUT:
        user_choice = input("\nInvalid input - please choose from Espresso / Latte / Cappuccino: ")
    return user_choice


# Function to check if resources are enough for user choice of coffee. If not, return the resource which is not enough.
def check_resources_for_coffee(type_of_coffee):
    """Function to check if resources are enough for type of coffee. If not, return the resource which is not enough."""
    required_resources = MENU[type_of_coffee][INGREDIENTS]
    if required_resources[WATER] > resources[WATER]:
        return WATER
    elif type_of_coffee != ESPRESSO and required_resources[MILK] > resources[MILK]:  # ESPRESSO has no milk
        return MILK
    elif required_resources[COFFEE] > resources[COFFEE]:
        return COFFEE
    else:
        return ''  # This return means no resource is insufficient (all required resources are available)


# Function to take the input of the coins from user. Returns the total value of the coins.
def get_user_coins():
    """Function to take the input of the coins from user. Returns the total value of the coins."""
    print("\nPlease enter your coins now...")
    quarters = int(input("How many quarters : "))
    dimes = int(input("How many dimes    : "))
    nickels = int(input("How many nickels   : "))
    pennies = int(input("How many pennies   : "))
    # Calculate value of coins
    coins_value = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    return coins_value


# Function to "make" coffee - reduce resources, add money to resources
def make_coffee(type_of_coffee):
    """Function to "make" coffee - reduce coffee ingredients from resources and add money to resources"""
    # Resources used to make the cup of coffee
    required_resources = MENU[type_of_coffee][INGREDIENTS]
    # Deducting required ingredients from the resources
    resources[WATER] -= required_resources[WATER]
    resources[COFFEE] -= required_resources[COFFEE]
    if selection != ESPRESSO:  # Deduct milk for coffee type which is not espresso
        resources[MILK] -= required_resources[MILK]
    # Add money from coffee to the resources['money']
    resources[MONEY] += cost_of_selection


# Main
screen_clear()
selection = get_user_choice_of_coffee()
# Loop until the secret word "off" is entered by user to exit
while selection != 'off':
    if selection == 'report':
        print_report()
    else:  # For any type of coffee - same steps will be performed
        # Check if resources are sufficient - if yes, show the cost of the coffee; else show sorry message
        resource_not_enough = check_resources_for_coffee(selection)
        if resource_not_enough == '':  # Means all resources are ok for the coffee selection made
            # Save the cost of the selection in a variable
            cost_of_selection = MENU[selection][COST]
            print(f"Thanks - that will be ${cost_of_selection}")
            # Take the input of coins from the user
            total_coin_value = get_user_coins()
            # Check if user has given enough coins to buy the coffee - if yes, make coffee; if no, show sorry message
            if total_coin_value >= cost_of_selection:
                # Calculate the change and show to the user
                change_to_return = round(float(total_coin_value - cost_of_selection), 2)
                if change_to_return > 0:
                    print(f"Thanks - you gave ${get_formatted_two_decimals(total_coin_value)}, "
                          f"and here's your change of ${get_formatted_two_decimals(change_to_return)}")
                else:
                    print(f"Thanks - you gave ${get_formatted_two_decimals(total_coin_value)}")
                # "Make" the coffee & add money to resources
                make_coffee(selection)
                # Tell user to enjoy!
                print(f"Here's your cup of {selection} - enjoy!\n")
            else:  # Not enough money, show sorry message
                print("\nSorry that's not enough money. Money refunded. Please try another selection.\n")
        else:  # Not enough resources, show sorry message
            print(f"\nSorry, we cannot make your {selection} - not enough {resource_not_enough}. "
                  f"Please try another selection.\n")
    # Get next user selection
    selection = get_user_choice_of_coffee()

# Print a bye message
print("\nThank you for using Python Coffee Maker!")
