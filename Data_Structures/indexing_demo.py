my_string = "Hello, World!"
print(my_string[0])  # Output: 'H'
print(my_string[-1])  # Output: '!'

my_list = [1, 2, 3, 4, 5]
my_tuple = (10, 20, 30, 40, 50)

print(my_list[2])  # Output: 3
print(my_tuple[-2])  # Output: 40

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_list[2:7])  # Output: [3, 4, 5, 6, 7]
print(my_list[1:9:2])  # Output: [2, 4, 6, 8]

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(nested_list[1])  # Output: [4, 5, 6]
print(nested_list[1][2])  # Output: 6

my_list = [1, 2, 3]

try:
    print(my_list[3])  # Raises an IndexError because the index 3 is out of range
except IndexError as e:
    print(f"Index Error: {e}")

sliced_list = my_list[1:5]  # No IndexError, returns an empty list since slicing doesn't raise an error
print(sliced_list)  # Output: [2, 3]

my_list = [1, 2, 3, 4, 5]

my_list[2] = 10  # Modifying the element at index 2
print(my_list)  # Output: [1, 2, 10, 4, 5]

my_string = "Hello, World!"

first_letter = my_string[0]
last_letter = my_string[-1]

print(f"First letter: {first_letter}, Last letter: {last_letter}")
# Output: First letter: H, Last letter: !

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = numbers[1::2]  # Start from index 1, skip every 2nd element
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

reverse_numbers = numbers[::-1]  # Reverse the list using negative step
print(reverse_numbers)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

