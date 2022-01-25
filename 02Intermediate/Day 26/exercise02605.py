weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


def celsius_to_fahrenheit(celsius_temp):
    return celsius_temp * 9 / 5 + 32


weather_f = {day: celsius_to_fahrenheit(temp_c) for (day, temp_c) in weather_c.items()}
print(weather_f)

