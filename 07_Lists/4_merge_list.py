# Merge two lists and also removing the duplicates.....

a = list(map(int, input('Enter the first list values with space: ').split()))
b = list(map(int, input('Enter the second list values with space: ').split()))

print('First list:', a)
print('Second list:', b)

c = a + b

new = []
for x in c:
    if x not in new:
        new.append(x)

#if we want to use list comprehension method so..
#[new.append(x) for x in c if x not in new]

print('Merged list without duplicates:', new)