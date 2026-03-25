# Copy content of one file to another...

file1 = open("data.txt", "r")
content = file1.read()

file2 = open("copy.txt", "w")
file2.write(content)

file1.close()
file2.close()