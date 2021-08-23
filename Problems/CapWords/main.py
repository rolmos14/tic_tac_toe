words = input().split('_')
title_words = [word.title() for word in words]
print("".join(title_words))
