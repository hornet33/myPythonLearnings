# Python program to implement Day 15 assignment (Coffee Machine) using OOP
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
coffee_money = MoneyMachine()

choice_of_coffee = 'x'
while choice_of_coffee != 'off':
    choice_of_coffee = input(f"What do you want {coffee_menu.get_items()}: ").lower()

    if choice_of_coffee == 'report':
        coffee_maker.report()
        coffee_money.report()
    elif choice_of_coffee in coffee_menu.get_items():
        coffee_details = coffee_menu.find_drink(choice_of_coffee)
        resource_sufficient = coffee_maker.is_resource_sufficient(coffee_details)
        if resource_sufficient:
            print(f"Thanks - that will be ${coffee_details.cost}")
            if coffee_money.make_payment(coffee_details.cost):
                coffee_maker.make_coffee(coffee_details)

    elif choice_of_coffee == 'off':
        continue
    else:
        print("Wrong input - enter a valid selection: ")

print("Thank you for using Python Coffee Maker!")
