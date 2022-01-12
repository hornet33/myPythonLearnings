# # Reading the weather_data.csv file and store in a list
# with open("weather_data.csv",mode="r") as weather_data_file:
#     data = weather_data_file.readlines()
# print(data)

# # Using inbuilt library to work with CSV
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)  # Using the csv reader method from inbuilt csv library
#     # # Accessing the rows in the csv file stored in data
#     # for row in data:
#     #     print(row)  # This allows us to iterate over the csv data where each row is a list
#
#     # Accessing and storing individual elements from the "data" variable
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Using Pandas library - needs to be installed for every project/machine
import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)  # Will retrieve all values for all rows and columns
# print(data["temp"])  # Will retrieve all column values for a particular column

# Pandas has two major types of objects - Series (1 dimension) and Dataframes (2 dimension)
# Dataframe consists of multiple Series objects (each column in a Dataframe is a Series object)
# Pandas provides methods to convert files from one format to another - ex. CSV to dictionary/JSON/etc.
# data_dictionary = data.to_dict()
# print(data_dictionary)

# Converting a Series in a Dataframe to a list to find average temperatures for the data in weather_data.csv file
# temperature_list = data["temp"].to_list()
# avg_temp = sum(temperature_list) / len(temperature_list)
# print(f"Average Temperature = {round(avg_temp, 2)}")
# # Can also use Series methods
# print(data["temp"].mean())  # Gets the mean (average) for the Series data["temp"]
# print(data["temp"].max())
# # Panadas also allows us to use the column names as attributes -> 'data["temp"]' can be written as 'data.temp'
# print(data.temp)  # Same as 'print(data["temp"])'

# Accessing rows in the Pandas Dataframes
# print(data[data.day == "Monday"])  # This will get the row from the data Dataframe which is equal to "Monday"
# print(data[data["day"] == "Monday"])  # Alternate way of doing the same thing as above

# print(data[data.temp == data.temp.max()])  # This will get the row which has the temperature == max temperature

# monday = data[data.day == "Monday"]  # Getting Monday's details in a variable
# temp_in_c = int(monday.temp)  # Getting Monday's temp which is in Celsius and changing to int type
# temp_in_f = (temp_in_c * 9 / 5) + 32  # Converting to Fahrenheit
# print(temp_in_f)

# Creating a dataframe from scratch - from an example dictionary as below
student_dict = {
    "student": ["Amy", "Jamie", "Premi"],
    "score": [50, 60, 70]
}
student_data = pandas.DataFrame(student_dict)  # Using Pandas library to create a Dataframe from the dictionary
print(student_data)
student_data.to_json("student_data.json")  # Using Panads library to export the Dataframe to a JSON file
