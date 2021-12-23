# Python program to implement a virtual coin toss randomly

import random

toss_result = random.randint(0, 1)
if toss_result == 0:
    print("Tails")
elif toss_result == 1:
    print("Heads")
# No need for else condition here since only two outcomes are required
