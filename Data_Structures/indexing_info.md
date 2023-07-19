# **Indexing in Python:**

- Indexing is a fundamental concept in Python, used to access individual elements in sequences like strings, lists, tuples, and other iterables.
- Python uses zero-based indexing, which means the first element in a sequence has an index of 0, the second element has an index of 1, and so on.
- Negative indices count elements from the end of the sequence, with -1 representing the last element.

## **Indexing Operator (`[]`) in Python:**

- The indexing operator `[]` is used to access elements in a sequence using their respective index values.
- It is a powerful and versatile way to extract specific elements or slices from a sequence.

## **Indexing in Strings:**

- Strings in Python are sequences of characters and support indexing using the indexing operator.
- Example:

```python
my_string = "Hello, World!"
print(my_string[0])  # Output: 'H'
print(my_string[-1])  # Output: '!'
```

## **Indexing in Lists and Tuples:**

- Lists and tuples are also sequences and support indexing using the indexing operator.
- Example:

```python
my_list = [1, 2, 3, 4, 5]
my_tuple = (10, 20, 30, 40, 50)

print(my_list[2])  # Output: 3
print(my_tuple[-2])  # Output: 40
```

## **Slice Notation:**

- Slice notation allows you to access a range of elements in a sequence.
- The syntax for slicing is `start:stop:step`.
- The slice includes elements from the `start` index up to, but not including, the `stop` index.
- The `step` value indicates the stride or interval between elements.
- Example:

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_list[2:7])  # Output: [3, 4, 5, 6, 7]
print(my_list[1:9:2])  # Output: [2, 4, 6, 8]
```

## **Indexing in Nested Sequences:**

- You can use multiple levels of indexing with the indexing operator to access elements within nested sequences.
- Example:

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(nested_list[1])  # Output: [4, 5, 6]
print(nested_list[1][2])  # Output: 6
```

## **Index Error and Slicing Out of Range:**

- If you try to access an index that is out of range or use slicing with an index beyond the sequence length, Python raises an `IndexError`.
- Example:

```python
my_list = [1, 2, 3]

# Raises an IndexError because the index 3 is out of range
print(my_list[3])

# No IndexError because slicing does not raise an error, it just returns an empty list
print(my_list[1:5])
```
