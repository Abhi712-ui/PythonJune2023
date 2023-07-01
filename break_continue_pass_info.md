# `break`, `continue`, and `pass`

## `break`

- The `break` statement is used to terminate the execution of a loop prematurely.
- When a `break` statement is encountered inside a loop, the loop is immediately exited, and the program execution continues with the next statement after the loop.
- `break` is often used in conjunction with conditional statements to exit a loop based on a certain condition.
It is commonly used to terminate a loop early when a specific condition is met, saving unnecessary iterations.

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        break
    print(num)

# Output: 1 2
```

- In this example, the break statement is used to exit the loop when the value of num becomes 3. As a result, the loop terminates prematurely, and only the numbers 1 and 2 are printed.

## `continue`

- The `continue` statement is used to skip the remaining code within a loop for the current iteration and move on to the next iteration.
- When a `continue` statement is encountered inside a loop, the loop skips the remaining code in the current iteration and jumps to the next iteration.
- It is often used in conjunction with conditional statements to skip specific iterations that meet certain conditions.
`continue` allows you to by`pass` certain iterations without terminating the loop entirely.

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        `continue`
    print(num)

# Output: 1 3 5
```

- In this example, the `continue` statement is used to skip the even numbers. When an even number is encountered, the `continue` statement is executed, and the remaining code in the loop for that iteration is skipped. Thus, only the odd numbers are printed.

## `pass`

- The `pass` statement is a null operation that does nothing.
- It is used as a placeholder when a statement is syntactically required but no action is needed.
`pass` is often used as a placeholder for code that will be implemented later or to create empty function or class definitions.
- It allows you to have a valid code structure without any actual code implementation

```python
for i in range(5):
    if i == 2:
        `pass`
    else:
        print(i)

# Output: 0 1 3 4
```

- In this example, when i equals 2, the `pass` statement is executed, which does nothing. It acts as a placeholder. For all other values of i, the corresponding number is printed
