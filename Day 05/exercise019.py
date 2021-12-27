# Python program for the "FizzBuzz" problem
# If a number is divisible by 3, print "Fizz"
# If a number is divisible by 5, print "Buzz"
# If a number is divisible by BOTH 3 and 5, print "FizzBuzz"

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
