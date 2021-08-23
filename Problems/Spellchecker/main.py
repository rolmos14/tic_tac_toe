dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

words = input().split()
incorrect = [word for word in words if word not in dictionary]
print("\n".join(incorrect) if incorrect else "OK")
