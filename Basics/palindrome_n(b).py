# (b) Take input and check if it is a palindrome number.
# Logic based - Interview level solution.

num = int(input('Enter a number: '))

original = num
rev = 0

while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10

if original == rev:
    print('Palindrome Number')
else:
    print('Not a Palindrome')