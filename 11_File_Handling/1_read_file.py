# Read a file and print content...

file = open("data.txt", "r")
content = file.read()
print(content)
file.close()