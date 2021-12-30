# Python program to check if a given number is a prime number or not

def prime_checker(number):
    is_prime = True
    for div in range(2, number):
        if number % div == 0:
            is_prime = False
            break
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Main
n = int(input("Check this number: "))
prime_checker(number=n)
