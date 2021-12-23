# Python program to put an "❌" in the spot the user gives as an input
row1 = ["⭕️", "⭕️", "⭕️"]
row2 = ["⭕️", "⭕️", "⭕️"]
row3 = ["⭕️", "⭕️", "⭕️"]
treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# First, separating out the row and col from the input
col = int(position[0]) - 1
row = int(position[1]) - 1

# Put the 'X' in the designated spot - emojis from https://getemoji.com/
treasure_map[row][col] = "❌️"

print(f"{row1}\n{row2}\n{row3}")
