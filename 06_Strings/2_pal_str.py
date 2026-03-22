# Check if a string is a palindrome

str = input("Enter a string: ")

# Remove spaces and convert to lowercase
str = str.replace(' ', ' ').lower()
# Check if the string is equal to its reverse
if str == str[::-1]:
    print('The string is a palindrome.')
else:
    print('The string is not a palindrome.')