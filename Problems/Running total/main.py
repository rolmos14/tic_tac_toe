numbers = [int(x) for x in input()]
cumulative_sum = [sum(numbers[:i + 1]) for i in range(len(numbers))]
print(cumulative_sum)
