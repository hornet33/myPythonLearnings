# Open names file and store the names in a list
with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    invited_names_list = names_file.readlines()

# Open letter template and store in a variable
with open("./Input/Letters/starting_letter.txt", mode="r") as letter_template_file:
    letter_template = letter_template_file.read()
    # print(letter_template)

# Loop through name list and save individual letters in output directory
output_file_path = "./Output/ReadyToSend"
for name in invited_names_list:
    name = name.strip()  # To remove the leading/trailing spaces and new-line chars
    print(name)
    file_name = f"letter_for_{name}.txt"
    letter_with_name = letter_template.replace("[name]", name)
    with open(f"{output_file_path}/{file_name}", mode="w") as letter_file:
        letter_file.write(letter_with_name)
