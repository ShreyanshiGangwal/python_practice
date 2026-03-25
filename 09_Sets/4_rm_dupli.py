# Remove duplicates using set...

num = list(map(int, input('Enter numbers separated by space: ').split()))
print('Your list is', num)

print('Now removing the duplicate numbers into the list using set.')

rm_dupli = set(num)
print('After removing duplicates:', rm_dupli)
