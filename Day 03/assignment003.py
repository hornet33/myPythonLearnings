# Python program to simulate a simple treasure game based on questions and responses
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# # # Above is a multi-line string in Python, starts and ends with 3 quotes '''

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

answer1 = input("Which direction do you want to go? Left or Right: ").upper()
if answer1 == 'LEFT':
    answer2 = input("There is a lake in front of you. Do you want to Swim or Wait? ").upper()
    if answer2 == 'WAIT':
        answer3 = input("There are 3 doors in front of you - pick a door colour. Red, Yellow or Blue: ").upper()
        if answer3 == 'YELLOW':
            print("You found the treasure - YOU WIN!")
        elif answer3 == 'RED':
            print("You were burned by fire - GAME OVER!")
        elif answer3 == 'BLUE':
            print("You were eaten by beasts - GAME OVER!")
        else:
            print("There is no door with that colour - GAME OVER!")
    else:
        print("You were attacked by the lake monster - GAME OVER!")
else:
    print("You fell into a hole - GAME OVER!")
