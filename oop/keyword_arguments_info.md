# **Keyword Arguments:**

- In Python, when calling a function, you can pass arguments using the name of the parameter (keyword) followed by the value, which is known as a keyword argument.
- Keyword arguments allow you to specify the parameters in any order and make function calls more explicit and self-documenting.

## **Using Keyword Arguments:**

- When calling a function, provide the argument names and their corresponding values using the syntax `parameter_name=value`.
- Example:

```python
def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

# Using keyword arguments
greet(name="Alice", age=25)  # Output: Hello, Alice. You are 25 years old.
greet(age=30, name="Bob")    # Output: Hello, Bob. You are 30 years old.
```

## **Default Values for Parameters:**

- Functions can have default values for parameters, which are used when the corresponding argument is not provided in the function call.
- Default values are specified in the function definition using the `parameter_name=default_value` syntax.
- Example:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")         # Output: Hello, Alice!
greet("Bob", "Hi")     # Output: Hi, Bob!
```

## **Mixing Positional and Keyword Arguments:**

- When calling a function, you can use a mix of positional and keyword arguments. However, positional arguments must come before keyword arguments.
- Example:

```python
def func(a, b, c):
    print(f"a={a}, b={b}, c={c}")

func(1, 2, 3)                 # Output: a=1, b=2, c=3
func(1, c=3, b=2)             # Output: a=1, b=2, c=3
func(c=3, a=1, b=2)           # Output: a=1, b=2, c=3
# func(c=3, 1, 2)             # Raises a SyntaxError, positional arguments must come before keyword arguments
```

## **Arbitrary Keyword Arguments (Double Asterisk `**kwargs`):**

- Functions can accept an arbitrary number of keyword arguments using the `**kwargs` syntax.
- The `**kwargs` parameter represents a dictionary containing the keyword arguments passed to the function.
- Example:

```python
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York
```

## **Benefits of Keyword Arguments:**

- Keyword arguments make function calls more readable and self-explanatory, especially when dealing with functions with many parameters.
- They provide flexibility in the order of arguments when calling a function.
- Default values for parameters allow functions to have optional arguments.

## **Caution with Mutable Default Values:**

- Be careful when using mutable objects (e.g., lists, dictionaries) as default values for parameters. They are created only once, leading to unexpected behavior when modified.
- Example:

```python
def add_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_to_list(1))      # Output: [1]
print(add_to_list(2))      # Output: [1, 2] (unexpected, as we might expect [2])
```

To avoid this issue, use immutable default values (e.g., `None`) and create a new object inside the function if needed.
