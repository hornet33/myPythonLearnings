# f-strings in Python are used for incorporating different data types using placeholders
# Python internally does all the type checking and type casting

score = 0  # Type int
height = 1.7526  # Type float
male = True  # Type boolean
print_string = f"Score is {score}, Height is {height}, Male is {male}"
# Always place a small 'f' at the beginning (before quotes) of the string to denote an f-string
# Use curly braces (like in pom.xml) to add a variable placeholder in the f-string
# Python will replace the placeholder with the variable values and type check/cast internally
print(print_string)
