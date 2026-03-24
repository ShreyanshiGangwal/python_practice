# Find max and min in tuple....

num = tuple(map(int, input("Enter numbers separated by space: ").split()))
print(num)

value = input("Enter what value you want 'max' or 'min': ").lower()

if value == 'max':
    find = max(num)
    print('Your maximum value is', find)
elif value == 'min':
    find = min(num)
    print('Your minimum value is', find)
else:
    print('Please enter the given value, try again....')