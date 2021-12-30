# Python program to add a new dictionary (with nested list) which is nested inside an outer list

# Original list with nested inner dictionary with a nested list
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# Function that will add a new list item (dictionary) in the travel_log list
def add_new_country(country, visits, city_list):
    # --- Approach 1
    position = len(travel_log)  # Get the last position of the list - new item will go here
    travel_log.append({})  # Append an empty dictionary to the outer list

    # Add the items in the nested dictionary within the outer list
    travel_log[position]["country"] = country
    travel_log[position]["visits"] = visits
    travel_log[position]["cities"] = city_list

    # --- Approach 2
    new_entry = {
        "country": country,
        "visits": visits,
        "cities": city_list
    }
    travel_log.append(new_entry)


# Function call to add values
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

# Print the final list after insertion
print(travel_log)
