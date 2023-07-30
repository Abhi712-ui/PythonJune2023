def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # Output: 10
# print(x) will raise a NameError since 'x' is not accessible outside the function.

def outer_function():
    x = 10  # Outer function variable

    def inner_function():
        nonlocal x
        x = 20  # Enclosing (nonlocal) variable

    inner_function()
    print(x)  # Output: 20

global_var = 100  # Global variable

def my_function():
    print(global_var)

my_function()  # Output: 100

# Built-in function 'len' is available without importing any module
my_list = [1, 2, 3]
print(len(my_list))  # Output: 3

global_var = 100

def modify_global():
    global global_var
    global_var = 200

modify_global()
print(global_var)  # Output: 200

def function1():
    global_var = 10
    print("Inside function1:", global_var)

def function2():
    global_var = 20
    print("Inside function2:", global_var)

function1()  # Output: Inside function1: 10
function2()  # Output: Inside function2: 20
print("Outside functions:", global_var)  # Output: Outside functions: 200 (global variable was modified earlier)

def add_numbers(a, b):
    result = a + b
    return result

x = 5
y = 10
sum_result = add_numbers(x, y)
print(sum_result)  # Output: 15
