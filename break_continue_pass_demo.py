numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        break
    print(num)

# Output: 1 2

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

# Output: 1 3 5

for i in range(5):
    if i == 2:
        pass
    else:
        print(i)

# Output: 0 1 3 4
