# For Loops

- A for loop is a control flow statement used for iterating over a sequence of elements. It allows you to execute a block of code repeatedly, with each iteration handling one element from the sequence.

```text
for element in sequence:
    # Code block to be executed
```

## Component Breakdown

### Sequence

- The sequence is an iterable object, such as a list, tuple, string, or range, that contains the elements to iterate over. The for loop iterates over each element in the sequence and executes the code block for each element.

### Element

- The element represents the current value being processed in the iteration. In each iteration, the element takes on the value of the next element in the sequence until all elements have been processed.

### Code Block

- The code block is the set of statements that are executed repeatedly for each element in the sequence. It is indented under the for loop statement and must maintain consistent indentation throughout.

### Iteration

- The loop variable (`element`) is assigned the value of the first element in the sequence.
- The code block inside the loop is executed for the current element.
- The loop variable is then assigned the value of the next element in the sequence.
- This process repeats until all elements in the sequence have been processed.

- Additionally, Python provides additional functionalities to enhance the usage of for loops, such as the `range()` function for generating numeric sequences and the `enumerate()` function for accessing both the index and value of each element in a sequence.
