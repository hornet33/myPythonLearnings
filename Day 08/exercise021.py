# Python program to calculate the cans of paint if the height and width of the paint area is provided
import math


def paint_calc(height, width, cover):
    paint_area = height * width
    paint_cans = math.ceil(paint_area / cover)
    print(f"You'll need {paint_cans} cans of paint.")


# Main logic
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
