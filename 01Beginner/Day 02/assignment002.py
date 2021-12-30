# Python program to calculate splitting of a restaurant bill

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

bill_value = float(input("Enter the total bill: $"))
tip_percent = int(input("Enter the desired service tip percentage (10, 12 or 15): "))
num_of_people = int(input("Enter the number of people: "))
per_person_amount = "{:.2f}".format((bill_value / num_of_people) * (1 + (tip_percent / 100)))
# '{:.2f}' is for formatting the output to always 2 decimal places - so "33.6" will display as "33.60"
fMessage = f"Each person should pay ${per_person_amount}"
print(fMessage)
