# Lists

- Lists are ordered, mutable collections of elements that can be of different types.
- They are one of the most commonly used data structures in Python and provide a flexible way to store and manipulate multiple values.
- Lists are defined by enclosing comma-separated elements within square brackets `[ ]`.

## **List Creation:**

- Lists can be created in several ways:
  - Using square brackets with elements: `my_list = [1, 2, 3, 4, 5]`
  - Using the `list()` function: `my_list = list([1, 2, 3, 4, 5])`
  - Empty list: `my_list = []` or `my_list = list()`

## **List Indexing and Slicing:**

- Elements in a list are indexed starting from 0, allowing individual elements to be accessed and modified.
- Indexing syntax: `my_list[index]`
- Negative indexing: `-1` refers to the last element, `-2` refers to the second last, and so on.
- List slicing allows you to extract a portion of a list.
- Slicing syntax: `my_list[start:stop:step]`
- Example: `my_list[1:4]` returns a new list with elements from index 1 to 3.

## **List Methods:**

- Lists have built-in methods to perform various operations:
  - `append()`: Add an element to the end of the list.
  - `extend()`: Extend the list by appending elements from another iterable.
  - `insert()`: Insert an element at a specific position.
  - `remove()`: Remove the first occurrence of a specified element.
  - `pop()`: Remove and return the element at a specified index.
  - `index()`: Return the index of the first occurrence of a specified element.
  - `count()`: Count the number of occurrences of a specified element.
  - `sort()`: Sort the list in ascending order.
  - `reverse()`: Reverse the order of elements in the list.

## **List Operations:**

- Lists support various operations such as concatenation (`+`), repetition (`*`), length calculation (`len()`), and membership testing (`in`).
- Example:

  ```python
  list1 = [1, 2, 3]
  list2 = [4, 5, 6]
  
  concatenated = list1 + list2  # Concatenation
  repeated = list1 * 3  # Repetition
  length = len(list1)  # Length calculation
  is_present = 2 in list1  # Membership testing
  ```

## **List Mutability:**

- Lists are mutable, meaning their elements can be modified.
- You can change, add, or remove elements from a list after it has been created.
- Example:

  ```python
  my_list = [1, 2, 3]
  
  my_list[1] = 4  # Modifying element at index 1
  my_list.append(5)  # Adding a new element at the end
  del my_list[0]  # Removing element at index 0
  ```

## **List Comprehension:**

- List comprehension is a concise way to create lists based on existing lists or other iterables.
- It provides a compact syntax to apply transformations or filters to elements of a list.
- Example:

  ```python
  numbers = [1, 2, 3, 4, 5]
  squared_numbers = [x ** 2 for x in numbers]  #Squaring each element
  even_numbers = [x for x in numbers if x % 2 == 0]  # Filtering even numbers

    ```
