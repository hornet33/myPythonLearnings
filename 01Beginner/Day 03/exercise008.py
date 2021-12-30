# Python program to check if an input number is odd or even
num_to_check = int(input("Enter a whole number: "))
remainder = num_to_check % 2
if remainder == 0:
    print(f"{num_to_check} is an even number")
else:
    print(f"{num_to_check} is an odd number")
