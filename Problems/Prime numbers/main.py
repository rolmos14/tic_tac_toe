prime_numbers = [n for n in range(2, 1001) if all([n % div for div in range(2, n)])]
