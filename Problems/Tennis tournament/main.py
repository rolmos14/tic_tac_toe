matches = [input() for _ in range(int(input()))]
win_matches = [match.split()[0] for match in matches if match.split()[1] == "win"]
print(win_matches, len(win_matches), sep="\n")
