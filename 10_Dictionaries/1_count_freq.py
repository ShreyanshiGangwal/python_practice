# Count frequency of elements...

numbers = list(map(int, input("Enter numbers: ").split()))
print('Your list is', numbers)
freq = {}

for num in numbers:
    freq[num] = freq.get(num, 0) + 1
    
print("Frequency:", freq)