# Slicing is a concept to take only a subset of elements from a list or a tuple
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print(piano_keys[2:5])  # This is slicing - will print "c", "d", "e"
print(piano_keys[2:])  # This will print c - g. Omitting the second argument slices till the end of the list
print(piano_keys[:5])  # This will print a - e. Omitting the first argument slices from the first till the end slice.
print(piano_keys[::2])  # Third argument is for steps. This will print a, c, e, g - every alternate item from start.
print(piano_keys[::-1])  # This will basically reverse the list - step of -1 from end to start of the list.

# The same logic/syntax above works for both lists and tuples

