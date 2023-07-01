my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(my_list[0][1])  # Output: 2

my_list[1][2] = 10
print(my_list)  # Output: [[1, 2, 3], [4, 5, 10], [7, 8, 9]]

for row in my_list:
    for element in row:
        print(element)
        
row = my_list[1]
print(row)  # Output: [4, 5, 6]

# Accessing a column using list comprehension
column = [row[1] for row in my_list]
print(column)  # Output: [2, 5, 8]

nested_list = [[1, [2, 3]], [4, [5, 6]]]
