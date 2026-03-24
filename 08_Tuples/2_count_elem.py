# Count occurrences of element...

num = tuple(map(int, input('Enter numbers separated by space: ').split()))
print('Your tuple is', num)

x = int(input("Enter the number to count: "))

number = num.count(x)
print(f'{x} occurs {number} times')