# **Nested Function Calls:**

- In Python, you can call a function from within another function, creating nested function calls.
- A nested function call occurs when the result of one function call is used as an argument for another function call, forming a chain of function calls.

## **Understanding Nested Function Calls:**

- When a function call is made inside another function's argument list, the inner function is evaluated first, and its result is then passed as an argument to the outer function.
- The result of the outer function call can also be used as an argument for other functions, allowing for more complex function compositions.

## **Example 1: Simple Nested Function Call:**

```python
def square(x):
    return x ** 2

def add(a, b):
    return a + b

result = add(square(3), 5)
print(result)  # Output: 14
```

In this example, `square(3)` is evaluated first, returning `9`. Then, the result of `square(3)` is passed as the first argument to `add(9, 5)`, resulting in the final output of `14`.

## **Example 2: Nested Function Calls with Built-in Functions:**

```python
numbers = [1, 2, 3, 4, 5]

result = sum(filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers)))
print(result)  # Output: 20
```

In this example, we are using the `map` function to square each element of the `numbers` list. Then, we use the `filter` function with a lambda function to keep only the even squared numbers. Finally, the `sum` function is used to add up the resulting filtered numbers, giving us the final output of `20`.

## **Example 3: Recursive Nested Function Calls:**

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

result = factorial(5)
print(result)  # Output: 120
```

In this example, the `factorial` function calls itself recursively with decreasing values of `n` until the base case (n == 0 or n == 1) is reached. The function then returns the final result of the factorial.

## **Example 4: Chaining Multiple Nested Function Calls:**

```python
def greet(name):
    return f"Hello, {name}!"

def capitalize(s):
    return s.upper()

def add_exclamation(s):
    return f"{s}!"

result = add_exclamation(capitalize(greet("Alice")))
print(result)  # Output: HELLO, ALICE!
```

In this example, the function calls are nested with `greet("Alice")` being evaluated first. The result, `"Hello, Alice!"`, is then passed to the `capitalize` function, resulting in `"HELLO, ALICE!"`. Finally, the result of `capitalize(greet("Alice"))` is passed to the `add_exclamation` function, resulting in the final output of `"HELLO, ALICE!"`.
