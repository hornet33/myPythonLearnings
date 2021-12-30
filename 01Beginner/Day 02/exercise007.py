# Python program to calculate remaining days, weeks and months left from current age to reach 90 years
age = input("What is your current age?")
age_as_int = int(age)
remaining_years_from_90 = 90 - age_as_int
remaining_days = remaining_years_from_90 * 365
remaining_weeks = remaining_years_from_90 * 52
remaining_months = remaining_years_from_90 * 12
message = f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months to reach 90 years of age"
print(message)
