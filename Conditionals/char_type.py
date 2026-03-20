# Check if a character is vowel or consonant..

char = input("Enter a character: ")

if char in 'AEIOUaeiou':
    print(char, 'is a vowel')
elif char.isalpha():                # isalpha() method checks if the character is an alphabetic character (either uppercase or lowercase)
    print(char, 'is a consonant')
else:
    print(char, 'is not an alphabetic character')