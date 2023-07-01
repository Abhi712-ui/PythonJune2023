# Nested Loops

## Syntax

```python
for outer_item in outer_sequence:
    # Outer loop code

    for inner_item in inner_sequence:
        # Inner loop code
```

## Breakdown

### Outer Loop

- The outer loop iterates over an outer sequence, such as a list, string, or range. It controls the overall iteration process and determines how many times the inner loop will be executed.

### Inner Loop

- The inner loop is nested inside the outer loop. It iterates over an inner sequence, which can be a different sequence or the same as the outer sequence. The inner loop code is executed for each iteration of the outer loop.

### Iteration

- The outer loop starts its first iteration
- The inner loop completes all of its iterations
- The outer loop starts its next iteration
- This process repeats itself until all of the iterations of the outer loop are donw

## Example

```python
rows = 3
columns = 2

for row in range(rows):
    for col in range(columns):
        print(f"Row: {row}, Column: {col}")

print("Nested loops finished!")
```

## Extras

```text
In Python, the end parameter is an optional argument for the print() function. By default, print() adds a newline character (\n) at the end of the printed content, which causes the next print statement to start on a new line.

When you specify end=" " as an argument to print(), it changes the default behavior of the end parameter. In this case, the space character " " is used as the value for end.

The end=" " argument replaces the default newline character (\n) with a space character. So, instead of starting a new line after printing, the print() statement will continue on the same line, separated by a space.
```

```text
In this code, combinations is a list that will hold all the combinations of colors and sizes. 

The list comprehension uses nested loops to iterate over each element in colors and sizes simultaneously, creating combinations.

Here's the step-by-step explanation of how the combinations list is generated:

The outer loop iterates over each color in the colors list. For the first iteration, color is assigned the value "red".

The inner loop iterates over each size in the sizes list. For the first iteration of the inner loop, size is assigned the value "small".

The tuple (color, size) is created using the current values of color and size. In this case, the tuple (color, size) would be ("red", "small").

The tuple (color, size) is appended to the combinations list.

The inner loop continues to iterate over the remaining sizes ("medium" and "large"), creating tuples and appending them to combinations.

Once the inner loop finishes, the outer loop proceeds to the next color, and the same process repeats for each color and size combination.

Finally, when all iterations are completed, the combinations list contains all the possible combinations of colors and sizes.

The resulting combinations list will be a list of tuples, where each tuple represents a combination of a color and a size. The order of the tuples in the list follows the order of the nested loops: colors are traversed first, and for each color, sizes are traversed.

In the example, the output is 
[('red', 'small'), ('red', 'medium'), ('red', 'large'), ('green', 'small'), ('green', 'medium'), ('green', 'large'), ('blue', 'small'), ('blue', 'medium'), ('blue', 'large')] 
which shows all the possible combinations of colors and sizes.
```
