sequence = [int(i) for i in input().split()]
number = int(input())
if number in sequence:
    print(" ".join([str(i) for i in range(len(sequence)) if sequence[i] == number]))
else:
    print("not found")
