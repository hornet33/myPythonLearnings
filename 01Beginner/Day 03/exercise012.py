# Python program for "Love Calculator" :-)
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Converting names to upper case
upper_name1 = name1.upper()
upper_name2 = name2.upper()

# Checking occurrence of "TRUE"
count_T = upper_name1.count("T") + upper_name2.count("T")
count_R = upper_name1.count("R") + upper_name2.count("R")
count_U = upper_name1.count("U") + upper_name2.count("U")
count_E = upper_name1.count("E") + upper_name2.count("E")
count_TRUE = count_T + count_R + count_U + count_E

# Checking occurrence of "LOVE"
count_L = upper_name1.count("L") + upper_name2.count("L")
count_O = upper_name1.count("O") + upper_name2.count("O")
count_V = upper_name1.count("V") + upper_name2.count("V")
# count_E = upper_name1.count("E") + upper_name2.count("E") -- Not needed since count of E is already done in TRUE
count_LOVE = count_L + count_O + count_V + count_E

# Calculate love percent
love_percent = count_TRUE * 10 + count_LOVE

# Print message according to love percent
if love_percent < 10 or love_percent > 90:
    print(f"Your score is {love_percent}, you go together like coke and mentos.")
elif love_percent >= 40 and love_percent <= 50:
    print(f"Your score is {love_percent}, you are alright together.")
else:
    print(f"Your score is {love_percent}.")
