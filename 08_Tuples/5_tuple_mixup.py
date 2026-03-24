# Take the number input from the user and create a tuple. 
# Then: find the maximum and minimum element of the tuple &
# count the number of times the largest element is repeated in the tuple and 
# convert the tuple to a list and reverse it.....

number = tuple(map(int, input('Enter numbers separated by space: ').split()))
print('Your tuple is', number)


maximum = max(number)
minimum = min(number)

print('Your maximum value is', maximum)
print('Your minimum value is', minimum)

# Count of largest element
count_max = number.count(maximum)
print('Count of maximum element:', count_max)

# Convert to list and reverse
convert_list = list(number)
convert_list.reverse()

print('Reversed list:', convert_list)