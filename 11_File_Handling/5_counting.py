# Count lines, words, characters....

file = open("data.txt", "r")
content = file.read()

# Characters
chars = len(content)

# Words
words = len(content.split())

# Lines
lines = len(content.split("\n"))

print("Characters:", chars)
print("Words:", words)
print("Lines:", lines)

file.close()