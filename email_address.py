import re
email_pattern = re.compile(r'[\w.-]+@[\w.-]+')

text = input("Enter text>> ")
match = email_pattern.search(text)
print(match)

results = email_pattern.finditer(text)
for match in results:
    print(f"Your email(s) found are {match.group()}")


