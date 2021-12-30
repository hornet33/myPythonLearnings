# In Python, a dictionary is a {key: value} pair - like maps in Java
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
# Access dictionary elements by the key - key must be exactly the same including case
print(programming_dictionary["Bug"])
print(programming_dictionary.get("Bug"))

# Dictionary is ordered, does not allow duplicate values (last value over-writes the key-value)
my_car_dictionary = {
    "Brand": "Renault",
    "Model": "Duster",
    "Make": "2017",
    "Make": "2021",  # This value will be taken for "Make", not "2017"
}
print(my_car_dictionary)

# Adding elements to a dictionary
my_car_dictionary["Transmission"] = "Automatic"
print(my_car_dictionary)

# Loop through individual dictionary items
for key in my_car_dictionary:
    print(f"{key} = {my_car_dictionary.get(key)}")

# Create an empty dictionary (initialize)
new_dictionary = {}

# Clear a dictionary
my_car_dictionary = {}  # Wipes out the dictionary and sets it to an empty dictionary
print(my_car_dictionary)

# ---- Nesting lists and dictionaries

# Nesting a list within a dictionary
travel_log = {
    "Karnataka": ["Mysore", "Bangalore", "Udupi", "Mangalore", "Coorg"],
    "Kerala": ["Wayanad", "Bekal", "Kottayam"],
    "Bengal": ["Siliguri", "Kolkata", "Darjeeling", "Kalimpong"],
    "Maharashtra": ["Mumbai", "Pune"],
    "Tamil Nadu": ["Chennai", "Ooty", "Kodaikanal", "Yercaud"],
}

# Nesting dictionaries and lists within a dictionary
detail_travel_log = {
    "Karnataka": {
        "cities_visited": ["Mysore", "Bangalore", "Udupi", "Mangalore", "Coorg"],
        "years_visited": [2016, 2021, 2015, 2015, 2017],
    },
    "Kerala": {
        "cities_visited": ["Wayanad", "Bekal", "Kottayam"],
        "years_visited": [2011, 2011, 2014],
    },
    "Bengal": {
        "cities_visited": ["Siliguri", "Kolkata", "Darjeeling", "Kalimpong"],
        "years_visited": [2021, 2018, 2021, 2020],
    },
    "Maharashtra": {
        "cities_visited": ["Mumbai", "Pune"],
        "years_visited": [2006, 2007],
    },
    "Tamil Nadu": {
        "cities_visited": ["Chennai", "Ooty", "Kodaikanal", "Yercaud"],
        "years_visited": [2010, 2016, 2017, 2014],
    },
}

# Accessing elements of nested dictionaries and lists within a dictionary by the key element
print(detail_travel_log.get("Karnataka").get("cities_visited")[0])

# Nesting dictionaries and lists within a list
list_travel_log = [
    {
        "state": "Karnataka",
        "cities_visited": ["Mysore", "Bangalore", "Udupi", "Mangalore", "Coorg"],
        "years_visited": [2016, 2021, 2015, 2015, 2017],
    },
    {
        "state": "Kerala",
        "cities_visited": ["Wayanad", "Bekal", "Kottayam"],
        "years_visited": [2011, 2011, 2014],
    },
    {
        "state": "Bengal",
        "cities_visited": ["Siliguri", "Kolkata", "Darjeeling", "Kalimpong"],
        "years_visited": [2021, 2018, 2021, 2020],
    },
    {
        "state": "Maharashtra",
        "cities_visited": ["Mumbai", "Pune"],
        "years_visited": [2006, 2007],
    },
    {
        "state": "Tamil Nadu",
        "cities_visited": ["Chennai", "Ooty", "Kodaikanal", "Yercaud"],
        "years_visited": [2010, 2016, 2017, 2014],
    },
]

# Accessing elements in dictionaries nested within a list is by list item position
print(list_travel_log[0].get("cities_visited")[0])
