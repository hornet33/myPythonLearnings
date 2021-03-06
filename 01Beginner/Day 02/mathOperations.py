# Mathematical operations in Python
# Division in Python always results in a float type
# ** means exponent in Python
# BODMAS rule applies - if same priority then left-most operand takes precedence
print(3 * 3 + 3 / 3 - 3)  # Answer is 7.0 (division results in float)
print(3 * (3 + 3) / 3 - 3)  # Answer is 3.0 (bracket first and division results in float)

# Rounding of numbers
print(round(8 / 3))  # Rounds to next higher integer
print(round(8 / 3, 2))  # Rounds to 2 decimal places
print(8 // 3)  # Floor function to next smaller integer
