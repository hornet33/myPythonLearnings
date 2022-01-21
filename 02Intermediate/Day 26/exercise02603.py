# You are going to create a list called result which contains the numbers that are common in both files "file1" "file2"
# file1 contains [1, 2, 3], file2 contains [2, 3, 4] -> Output = [2, 3]

with open("file1.txt", "r") as file1:
    file1_list = file1.readlines()

with open("file2.txt", "r") as file2:
    file2_list = file2.readlines()

result = [int(n) for n in file1_list if n in file2_list]
print(result)
