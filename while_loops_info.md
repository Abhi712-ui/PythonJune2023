# While Loops

- A while loop is a control flow statement that allows you to repeatedly execute a block of code as long as a specified condition is true.

```text
while condition:
    # Code block to be executed

```

## breakdown

### Condition

- The condition is an expression that determines whether the loop should continue iterating or not. It is evaluated before each iteration of the loop. If the condition is initially false, the code block inside the loop will never execute.

### Code Block

- The code block is the set of statements that are executed repeatedly as long as the condition remains true. It is indented under the `while` statement and must maintain consistent indentation throughout.

### Flow Control

- The condition is evaluated.
- If the condition is true, the code block inside the loop is executed.
- After executing the code block, the condition is evaluated again.
- If the condition is still true, the loop continues, and the code block is executed again.
- This process repeats until the condition becomes false, at which point the loop terminates, and the program continues with the next statement after the loop
- It's important to ensure that the condition eventually becomes false; otherwise, you may end up with an infinite loop, where the loop continues indefinitely.

```python

count = 0

while count < 5:
    print("Count:", count)
    count += 1

print("Loop finished!")
```

- In this example, the while loop continues executing the code block as long as the `count` variable is less than 5. With each iteration, the value of `count` is incremented by 1 using `count += 1`. Once the condition `count` < 5` becomes false, the loop terminates, and the program proceeds to the next statement after the loop.
