# **2D Lists:**

- A 2D list, also known as a nested list, is a list of lists. It allows you to create a matrix-like structure with rows and columns.
- Each element in a 2D list can be accessed using two indices: one for the row and another for the column.
- The elements within the 2D list can be of any data type, including other lists.

## **Creating a 2D List:**

- 2D lists can be created using various approaches:
  - Initializing a list with nested lists: `my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
  - Using a loop to populate the 2D list:

    ```python
    rows = 3
    cols = 4
    my_list = [[0] * cols for _ in range(rows)]
    ```

  - Adding elements dynamically: `my_list = [[] for _ in range(rows)]` and then using `my_list[row].append(element)` to add elements.

## **Accessing Elements in a 2D List:**

- Elements in a 2D list can be accessed by specifying the row and column indices.
- Syntax: `my_list[row_index][column_index]`
- Example: `my_list[0][1]` returns the element at the first row and second column.

## **Iterating Over a 2D List:**

- You can use nested loops to iterate over all elements of a 2D list.
- Example:

  ```python
  my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  
  for row in my_list:
      for element in row:
          print(element)
  ```

## **Modifying Elements in a 2D List:**

- Elements within a 2D list can be modified by specifying the row and column indices.
- Example:

  ```python
  my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  
  my_list[1][2] = 10
  print(my_list)  # Output: [[1, 2, 3], [4, 5, 10], [7, 8, 9]]
  ```

## **2D List Operations and Methods:**

- 2D lists support various operations and methods similar to 1D lists, including concatenation, repetition, length calculation, and membership testing.
- Example:

  ```python
  list1 = [[1, 2], [3, 4]]
  list2 = [[5, 6], [7, 8]]
  
  concatenated = list1 + list2  # Concatenation
  repeated = list1 * 3  # Repetition
  length = len(list1)  # Length calculation
  is_present = [1, 2] in list1  # Membership testing
  ```

## **Working with Rows and Columns:**

- You can access individual rows or columns of a 2D list by using list indexing and list comprehension techniques.
- Example:

  ```python
  my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  
  # Accessing a row
  row = my_list[1]
  print(row)  # Output: [4, 5, 6]
  
  # Accessing a column using list comprehension
  column = [row[1] for row in my_list]
  print(column)  # Output: [2, 5, 8]
  ```

## **Nested 2D Lists:**

- 2D lists can contain other 2D lists, resulting in nested structures.
- Example:

  ```python
  nested_list = [[1, [2, 3]], [4, [5, 6]]]
  ```
