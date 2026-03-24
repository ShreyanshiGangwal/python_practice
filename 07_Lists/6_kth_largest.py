# Find kth largest element....

number = list(map(int, input('Enter numbers separated by space: ').split()))
print('Your list is', number)

k = int(input("Enter value of k: "))

# Remove duplicates
num = list(set(number))

#Sort in descending order
num.sort(reverse=True)

# Check if k is valid
if k > len(num) or k <= 0:
    print("Invalid k value")
else:
    print(f"{k}th largest element is:", num[k-1])