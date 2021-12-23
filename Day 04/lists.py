# A data structure in Python (like ArrayLists in Java)
# Lists in Python maintain the order of elements
sample_list = ["Item1", "Item2", "Item3"]

# To retrieve individual list items, use the index
# First element at 0 - Positive index takes element wrt index 0
print(sample_list[0])

# Negative index takes elements from the end of the list
print(sample_list[-2])  # -1 = last item in the list, -2 = second last item in the list, ...

# If indexes are not in the valid range, an IndexError is raised (index out of range)
# print(sample_list[4]) - index out of range error
# print(sample_list[-5]) - index out of range error

# To modify an existing item simply give the new value to the particular list index
sample_list[0] = "Item-01"
print(sample_list)

# To add a new item to the end of the list, use append() with the value to append
sample_list.append("Item-04")
print(sample_list)
sample_list.append(4)  # Different data types can be put in the same list
print(sample_list)

# To insert a new item in the middle of the list, use the insert() function
sample_list.insert(3, "New Item4")
print(sample_list)

# index() function returns the index where the value is found - if not found, a ValueError is raised
print(sample_list.index("Item2"))

# remove() function removes the first item from the list matching the value - if not found, a ValueError is raised
sample_list.remove("New Item4")
print(sample_list)
sample_list.append("Item-04")
print(sample_list)
sample_list.remove("Item-04")
print(sample_list)

# Go through Python documentation at https://docs.python.org/3/tutorial/datastructures.html for lists
