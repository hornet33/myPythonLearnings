# ##################### DEBUGGING ##################### #

# # Describe Problem
# def my_function():
#     for i in range(1, 20):  # range() ignores the second argument so i == 20 is never true. Should be range(1, 21)
#         if i == 20:
#             print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
# # randint() includes the second argument and since dice_imgs has upper index of 5, it can give error if dice_num = 6
# # hence randint(1, 6) should be changed to randint(0, 5)

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")
# # Both conditions above miss 1994 and will not print anything for year = 1994
# # So one of the if conditions should change to include 1994 (eg. year > 1980 and year <= 1994)

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
# # 1) Statements inside if should be indented. 2) Input should be cast to int. 3) print should be an f-string.

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# # word_per_page is using a conditional operator == instead of an assignment operator =
# # Should be word_per_page = int(input("Number of words_per_page: "))

# #Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#     b_list.append(new_item)
#     print(b_list)
# mutate([1, 2, 3, 5, 8, 13])
# # b_list.append() should be indented inside the for block to append each new_item in the b_list
