for i in range(1, 6):
    for j in range(1, 6):
        product = i * j
        print(f"{i} x {j} = {product}")

size = 5

for i in range(1, size + 1):
    for j in range(i):
        print("*", end=" ")
    print()

colors = ["red", "green", "blue"]
sizes = ["small", "medium", "large"]

combinations = [(color, size) for color in colors for size in sizes]

print(combinations)
