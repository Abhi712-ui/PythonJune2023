my_list = [1, 2, 3, 4, 5]

print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: 5

# Modifying elements
my_list[2] = 6
print(my_list)  # Output: [1, 2, 6, 4, 5]

print(my_list[1:4])  # Output: [2, 3, 4]
print(my_list[::2])  # Output: [1, 3, 5]

my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

my_list.extend([7, 8, 9])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list.insert(2, 10)
print(my_list)  # Output: [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]

my_list.remove(3)
print(my_list)  # Output: [1, 2, 10, 4, 5, 6, 7, 8, 9]

popped_value = my_list.pop(4)
print(popped_value)  # Output: 5
print(my_list)  # Output: [1, 2, 10, 4, 6, 7, 8, 9]

index = my_list.index(7)
print(index)  # Output: 5

count = my_list.count(2)
print(count)  # Output: 1

my_list.sort()
print(my_list)  # Output: [1, 2, 4, 6, 7, 8, 9]

my_list.reverse()
print(my_list)  # Output: [9, 8, 7, 6, 4, 2, 1]

numbers = [1, 2, 3, 4, 5]

squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4]
