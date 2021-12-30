# Python program to check days in months
def is_leap(year_to_check_leap):
    if year_to_check_leap % 4 == 0:
        if year_to_check_leap % 100 == 0:
            if year_to_check_leap % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year_to_check, month_to_check):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year_to_check):
        month_days[1] = 29

    return month_days[month_to_check - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
