# Count words in a file...

file = open('data.txt', 'r')
content = file.read()
print(content)

words = content.split()
print('Total words:', len(words))

file.close()
