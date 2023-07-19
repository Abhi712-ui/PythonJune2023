name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello,", name)
print("You are", age, "years old.")

# Prompting the user for input
name = input("Enter your name: ")
print("Hello,", name)

# Accepting integer input
age = int(input("Enter your age: "))
print("You are", age, "years old.")

# Accepting float input
height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters.")

# Accepting multiple inputs
num1, num2 = input("Enter two numbers separated by a space: ").split()
num1 = int(num1)
num2 = int(num2)
print("Sum:", num1 + num2)

# Accepting input with default value
country = input("Enter your country (default is 'Unknown'): ") or "Unknown"
print("Your country:", country)

# Accepting input without displaying a prompt
secret_code = input()
print("Secret code entered:", secret_code)

# Using eval() to accept any valid Python expression
result = eval(input("Enter an expression: "))
print("Result:", result)
