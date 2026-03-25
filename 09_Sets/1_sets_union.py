# Union of sets....

a = set(map(int, input('Enter 1st set numbers separated by space: ').split()))
b = set(map(int, input('Enter 2nd set numbers separated by space: ').split()))
c = set(map(int, input('Enter 3rd set numbers separated by space: ').split()))

print('Set A:', a)
print('Set B:', b)
print('Set C:', c)
print()
print('Now combining all the sets...')
uni = a.union(b,c)
print('Sets union:', uni)