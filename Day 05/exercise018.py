# Python program to print the sum of all even numbers from 1 to 100

total = 0
for number in range(1, 101):  # Loop through 1 to 100 (n-1 = 101-1 = 100)
    if number % 2 == 0:  # Check if number is even
        total += number  # Add to total if even number
print(total)
