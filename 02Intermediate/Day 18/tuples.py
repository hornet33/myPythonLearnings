# A Python data-type which is IMMUTABLE, and contains a set of ORDERED items
my_tuple = (2, 4, 6)
# To access elements, same like a list or dictionary - using square brackets. Index begins at 0.
print(my_tuple[0])  # will print '2'

# Biggest difference is that tuple items CANNOT BE CHANGED - no assignment, no changing, no modification
# my_tuple[0] = 3 will give a type error
