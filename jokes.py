import re

joke_pattern = re.compile(r"Why did the .*?\s?.*?\?\s?Because.*")
text = input("Enter text to match >> ")

if re.search(joke_pattern, text):
    match = joke_pattern.search(text)
    results = joke_pattern.finditer(text)
    for match in results:
        print(f" Found Jokes: {match.group()}")
else:
    print("This is not a joke")


