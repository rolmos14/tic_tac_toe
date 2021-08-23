height = int(input())
triangle = []

for i in range(1, height + 1):
    triangle.append(" " * (height - i) + "#" * (2 * i - 1))

print("\n".join(triangle))
