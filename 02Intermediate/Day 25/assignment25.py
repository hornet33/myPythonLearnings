# Python program to use the Squirrel Census Data from csv file and get the count of squirrels for each color
import pandas

FUR_COLUMN = "Primary Fur Color"

# Store file contents in squirrel_data variable
squirrel_data = pandas.read_csv("2018_Squirrel_Census_Data.csv")

# Store the unique colors in the color count list
colors_list = squirrel_data[FUR_COLUMN].unique()
# print(colors_list)

# Loop through the Primary fur color column (Series) and update the color count dictionary
colors_count = []
for count_for_color in colors_list:
    colors_count.append(len(squirrel_data[squirrel_data[FUR_COLUMN] == count_for_color]))
# print(colors_count)

# Create a dictionary
colors_dictionary = {
    "colors": colors_list,
    "counts": colors_count
}

# Create a data frame and save as a JSON file
squirrel_dataframe = pandas.DataFrame(colors_dictionary)
# print(squirrel_dataframe)
squirrel_dataframe.to_json("squirrel_color_counts.json")
