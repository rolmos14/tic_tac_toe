numbers = [int(x) for x in input()]
run_avg = [(numbers[i] + numbers[i + 1]) / 2 for i in range(len(numbers) - 1)]
print(run_avg)
