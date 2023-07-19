def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!

def add_numbers(x, y):
    return x + y

result = add_numbers(3, 5)
print(result)  # Output: 8

def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user()  # Output: Hello, Guest!
greet_user("Alice")  # Output: Hello, Alice!

def sum_all(*args):
    return sum(args)

result = sum_all(1, 2, 3, 4, 5)
print(result)  # Output: 15

add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

def multiply(x, y):
    """
    Multiply two numbers and return the result.

    Parameters:
    x (int): The first number.
    y (int): The second number.

    Returns:
    int: The product of x and y.
    """
    return x * y

global_var = 10  # global_var is a global variable

def my_function():
    local_var = 20  # local_var is a local variable
    print(global_var)
    print(local_var)

my_function()
print(global_var)  # Output: 10
# print(local_var)  # Raises a NameError as local_var is not defined in this scope
