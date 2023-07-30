def add_numbers(x, y):
    result = x + y
    return result

sum_result = add_numbers(3, 5)
print(sum_result)  # Output: 8

def get_coordinates():
    x = 10
    y = 20
    return x, y

coordinates = get_coordinates()
print(coordinates)  # Output: (10, 20)

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero."
    return x / y

result = divide(10, 2)
print(result)  # Output: 5.0

result = divide(10, 0)
print(result)  # Output: "Cannot divide by zero."

def no_return():
    pass

result = no_return()
print(result)  # Output: None

def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(5))  # Output: "Positive"
print(check_number(-2))  # Output: "Negative"
print(check_number(0))  # Output: "Zero"

def get_adder(x):
    def adder(y):
        return x + y
    return adder

add_5 = get_adder(5)
print(add_5(3))  # Output: 8

def find_element_in_list(element, my_list):
    for item in my_list:
        if item == element:
            return True
    return False

numbers = [1, 2, 3, 4, 5]
result = find_element_in_list(3, numbers)
print(result)  # Output: True

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

result = factorial(5)
print(result)  # Output: 120
