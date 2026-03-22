# Find largest & smallest element...

# map(int, ...)is used to convert each element of a list from string to integer so that numerical operations like max, min, sum can be performed correctly.
num = list(map(int, input("Enter numbers separated by space: ").split()))

#it is called List Comprehension..
#num = [int(x) for x in input('Enter numbers separated by space: ').split()]

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