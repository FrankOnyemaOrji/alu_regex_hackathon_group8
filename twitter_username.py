import re

username_pattern = re.compile(r'@[a-zA-Z0-9]+')
text = input(" Enter text >> ")
match = username_pattern.search(text)
print(match)
results = username_pattern.finditer(text)
for match in results:
    print(f" Found twitter username: {match.group()}")
