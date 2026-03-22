# Count vowels and consonants in a string....

str = input("Enter a string: ")
vowels = 0
consonants = 0

for char in str:
    if char.isalpha():  # Check if the character is an alphabet
        if char.lower() in 'aeiou':  # Check if it's a vowel
            vowels += 1
        else:  # If it's not a vowel, it must be a consonant
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)