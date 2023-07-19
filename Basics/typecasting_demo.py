# Typecasting examples

# Integer to string
num = 10
num_str = str(num)
print(f"num_str: {num_str}, type: {type(num_str)}")

# Float to integer
float_num = 3.14
int_num = int(float_num)
print(f"int_num: {int_num}, type: {type(int_num)}")

# String to integer
str_num = "100"
int_str = int(str_num)
print(f"int_str: {int_str}, type: {type(int_str)}")

# String to float
str_float = "3.14"
float_str = float(str_float)
print(f"float_str: {float_str}, type: {type(float_str)}")

# Boolean to integer
bool_val = True
int_bool = int(bool_val)
print(f"int_bool: {int_bool}, type: {type(int_bool)}")

# Integer to boolean
num_val = 0
bool_num = bool(num_val)
print(f"bool_num: {bool_num}, type: {type(bool_num)}")

# String to boolean
str_val = "True"
bool_str = bool(str_val)
print(f"bool_str: {bool_str}, type: {type(bool_str)}")

# Typecasting examples

# List to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(f"my_tuple: {my_tuple}, type: {type(my_tuple)}")

# Tuple to list
my_tuple = (4, 5, 6)
my_list = list(my_tuple)
print(f"my_list: {my_list}, type: {type(my_list)}")

# List to set
my_list = [1, 2, 3, 3, 4, 4, 5]
my_set = set(my_list)
print(f"my_set: {my_set}, type: {type(my_set)}")

# Set to list
my_set = {4, 5, 6}
my_list = list(my_set)
print(f"my_list: {my_list}, type: {type(my_list)}")

# List of tuples to dictionary
my_list = [("name", "John"), ("age", 25)]
my_dict = dict(my_list)
print(f"my_dict: {my_dict}, type: {type(my_dict)}")

# Dictionary to list of tuples
my_dict = {"name": "Jane", "age": 30}
my_list = list(my_dict.items())
print(f"my_list: {my_list}, type: {type(my_list)}")
