# Write user input to file...

data = input("Enter something: ")

file = open("data.txt", "w")
file.write(data)

file.close()