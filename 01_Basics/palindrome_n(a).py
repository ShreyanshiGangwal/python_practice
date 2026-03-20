# (a) Take input and check if it is a palindrome number.

num = input("Enter a number: ")

if num == num[::-1]:            # [::-1] use for reversing the string.
    print("Palindrome Number")
else:
    print("Not a Palindrome")
