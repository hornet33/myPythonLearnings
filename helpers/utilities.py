import os
import random


def screen_clear():
    """Function to clear the screen when running from the console/terminal"""
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platform
        _ = os.system('cls')


def get_random_number(start, end):
    """Function to generate a random number between (start, end) and return it"""
    return random.randint(start, end)


def get_formatted_two_decimals(number):
    """Function to return the 2 decimal places formatted string for a given number"""
    return "{:.2f}".format(number)


def get_mouse_click_coor(x, y):
    """Function that will print the (x,y) co-ordinates where a mouse click has occurred on the screen"""
    print(x, y)
