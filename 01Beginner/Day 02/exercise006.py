# Python program to calculate the BMI (Weight / Height^2) and print in whole number
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = int(float(weight) / (float(height) ** 2))
print(bmi)
