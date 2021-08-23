text = input()
words = text.split()
web_prefixes = ("https://", "http://", "www.")
for word in words:
    if word.lower().startswith(web_prefixes):
        print(word)
