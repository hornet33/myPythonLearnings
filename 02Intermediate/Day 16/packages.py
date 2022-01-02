# Using Python packages by searching on pypi.org
# For example "PrettyTable
# First need to install (instructions can be found in the library page from pypi.org)
# python -m pip install -U prettytable -- install instructions for PrettyTable from CLI
# OR - can install via PyCharm > Settings > Project > Project Interpreter > Packages
# Similar to installing Plugins for PyCharm / IntelliJ

from prettytable import PrettyTable
# Package 'prettytable' is installed hence able to import above - if not installed, that line will give an error
my_pretty_table = PrettyTable()  # Creating an object of PrettyTable class
# Add data to the table
my_pretty_table.field_names = ["Pokemon Name", "Type"]
my_pretty_table.add_row(["Pikachu", "Electric"])
my_pretty_table.add_row(["Squirtle", "Water"])
my_pretty_table.add_row(["Charmander", "Fire"])
my_pretty_table.align = "l"
print(my_pretty_table)
