# Sort list without built-in sort()....
# using bubble sort method

numbers = list(map(int, input('Enter the numbers of list with the spaces: ').split()))
print(numbers)

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
         if numbers[j] > numbers[j + 1]:      #swaping the numbersa
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)