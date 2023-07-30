def square(x):
    return x ** 2

def add(a, b):
    return a + b

result = add(square(3), 5)
print(result)  # Output: 14

numbers = [1, 2, 3, 4, 5]

result = sum(filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers)))
print(result)  # Output: 20

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

result = factorial(5)
print(result)  # Output: 120

def greet(name):
    return f"Hello, {name}!"

def capitalize(s):
    return s.upper()

def add_exclamation(s):
    return f"{s}!"

result = add_exclamation(capitalize(greet("Alice")))
print(result)  # Output: HELLO, ALICE!

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]

squared_numbers = [square(num) for num in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

def double(x):
    return x * 2

def increment(x):
    return x + 1

def square(x):
    return x ** 2

result = square(increment(double(5)))
print(result)  # Output: 196

def power(base, exponent):
    return base ** exponent

result = power(square(2), 3)
print(result)  # Output: 8

