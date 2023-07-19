my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

print(my_dict['name'])  # Output: 'John'

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

my_dict['age'] = 31  # Modifying value
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

my_dict['occupation'] = 'Engineer'  # Adding new key-value pair
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'occupation': 'Engineer'}

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

keys_view = my_dict.keys()
values_view = my_dict.values()
items_view = my_dict.items()

print(keys_view)  # Output: dict_keys(['name', 'age', 'city'])
print(values_view)  # Output: dict_values(['John', 30, 'New York'])
print(items_view)  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

age = my_dict.get('age')
print(age)  # Output: 30

removed_value = my_dict.pop('city')
print(removed_value)  # Output: 'New York'
print(my_dict)  # Output: {'name': 'John', 'age': 30}

key, value = my_dict.popitem()
print(key, value)  # Output: 'age', 30
print(my_dict)  # Output: {'name': 'John'}

my_dict.clear()
print(my_dict)  # Output: {}

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Iterating over keys
for key in my_dict:
    print(key)

# Iterating over values
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)

numbers = [1, 2, 3, 4, 5]
squared_dict = {x: x ** 2 for x in numbers}
print(squared_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

my_dict = {
    'person1': {'name': 'John', 'age': 30},
    'person2': {'name': 'Jane', 'age': 25}
}

print(my_dict['person1']['name'])  # Output: 'John'
print(my_dict['person2']['age'])  # Output: 25
