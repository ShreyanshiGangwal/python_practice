# Remove spaces from a string

str = input("Enter a sentence: ")

#str = str.replace(" ", "")

str = ''.join(str.split())

print("String after removing spaces:", str)