# Variable Scope

 -Variable scope in Python refers to the region or context in which a variable is defined and can be accessed. Understanding variable scope is crucial for writing reliable and bug-free code. Python has four types of variable scopes:

1. **Local Scope:**
   - Variables defined inside a function have local scope and are accessible only within that function.
   - Local variables are created when the function is called and destroyed when the function returns.
   - Example:

   ```python
   def my_function():
       x = 10  # Local variable
       print(x)

   my_function()  # Output: 10
   # print(x) will raise a NameError since 'x' is not accessible outside the function.
   ```

2. **Enclosing (Nonlocal) Scope:**
   - Variables defined in a nested function (inner function) that refer to variables in the enclosing (outer) function have enclosing scope.
   - These variables are not global but are accessible to the inner function and any other nested functions within it.
   - Example:

   ```python
   def outer_function():
       x = 10  # Outer function variable

       def inner_function():
           nonlocal x
           x = 20  # Enclosing (nonlocal) variable

       inner_function()
       print(x)  # Output: 20
   ```

3. **Global Scope:**
   - Variables defined at the top-level of a module or explicitly declared as global have global scope.
   - Global variables are accessible from any part of the code, including functions, within the same module.
   - Example:

   ```python
   global_var = 100  # Global variable

   def my_function():
       print(global_var)

   my_function()  # Output: 100
   ```

4. **Built-in Scope:**
   - The built-in scope contains all the names of Python's built-in functions and modules.
   - These functions, such as `print()`, `len()`, `range()`, etc., are available throughout the code without importing any module.

**Scope Resolution:**

- Python follows the LEGB rule to resolve variable names (Local, Enclosing, Global, Built-in).
- When a variable is accessed, Python first looks for it in the local scope, then the enclosing scope (if nested), followed by the global scope, and finally in the built-in scope.

**Modifying Global Variables from within a Function:**

- To modify a global variable from within a function, you must use the `global` keyword to indicate that the variable is from the global scope.
- Example:

```python
global_var = 100

def modify_global():
    global global_var
    global_var = 200

modify_global()
print(global_var)  # Output: 200
```

**Caution with Global Variables:**

- While global variables can be convenient, excessive use can lead to code that is hard to understand and maintain.
- It's generally better to pass variables explicitly as arguments to functions or return values from functions to avoid relying heavily on global variables.
