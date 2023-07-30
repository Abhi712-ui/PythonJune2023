def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

# Using keyword arguments
greet(name="Alice", age=25)  # Output: Hello, Alice. You are 25 years old.
greet(age=30, name="Bob")    # Output: Hello, Bob. You are 30 years old.

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")         # Output: Hello, Alice!
greet("Bob", "Hi")     # Output: Hi, Bob!

def func(a, b, c):
    print(f"a={a}, b={b}, c={c}")

func(1, 2, 3)                 # Output: a=1, b=2, c=3
func(1, c=3, b=2)             # Output: a=1, b=2, c=3
func(c=3, a=1, b=2)           # Output: a=1, b=2, c=3
# func(c=3, 1, 2)             # Raises a SyntaxError, positional arguments must come before keyword arguments

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York

def my_function(a, b, *args, x=10, y=20, **kwargs):
    print(f"a={a}, b={b}, args={args}, x={x}, y={y}, kwargs={kwargs}")

my_function(1, 2)  # Output: a=1, b=2, args=(), x=10, y=20, kwargs={}
my_function(1, 2, 3, 4, x=100, y=200, z=300)
# Output: a=1, b=2, args=(3, 4), x=100, y=200, kwargs={'z': 300}

def get_person_details(**kwargs):
    return kwargs

person_info = get_person_details(name="Alice", age=25, city="New York")
print(person_info)
# Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

