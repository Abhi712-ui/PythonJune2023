countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Liftoff!")

password = ""

while password != "secret":
    password = input("Enter the password: ")

print("Access granted!")

total = 0
number = 1

while number <= 10:
    total += number
    number += 1

print("Sum of numbers from 1 to 10:", total)
