# For Loops in Python
# Simple for-loop for variables
for i in range(5):
    # range starts from 0 to n-1.
    print(i)  # Will print 0 to 4 (which is n-1 = 5-1)

# Start, end and increment value can be specified - "range(1,6,2)" will loop from 1 to 5 with values of 1, 3, 5
for i in range(1, 6, 2):
    print(i)

# Simple for-loop for a list
states = ["Assam", "Bengal", "Karnataka", "Sikkim"]
for state in states:
    print(state)
