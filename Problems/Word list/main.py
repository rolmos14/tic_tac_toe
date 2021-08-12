text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

max_len = int(input())
shorter_or_equal = [word for sentence in text for word in sentence if len(word) <= max_len]
print(shorter_or_equal)
