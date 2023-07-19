# If Statements

## basic syntax

``` text
if condition:
    # code block to be executed if the condition is true
```

- Condition - logical operation that has a boolean value

- Code Block - What gets executed based on the value of the statement, designated by an indent

- If-Else Statement: In addition to the basic if statement, you can extend it with an else clause to specify an alternative code block to execute when the condition is false.

## else if statement syntax

```text
if condition:
    # code block to be executed if the condition is true
else:
    # code block to be executed if the condition is false

```

- If you have multiple conditions to check, you can use the elif statement, which stands for "else if". It allows you to specify additional conditions to evaluate when the preceding conditions are false

```text
if condition1:
    # code block to be executed if condition1 is true
elif condition2:
    # code block to be executed if condition1 is false and condition2 is true
elif condition3:
    # code block to be executed if condition1 and condition2 are false and condition3 is true
else:
    # code block to be executed if all conditions are false

```

- The indentation actually matters btw, and you can also nest if statements
