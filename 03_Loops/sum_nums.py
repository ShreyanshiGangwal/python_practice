# Sum of first N numbers...
n = int(input("Enter a number: "))

# Sum of first N numbers using for loop...
sum = 0
i = 1
for i in range(1, n + 1):
    sum += i
print("The sum of the first", n, "numbers is:", sum)

# Sum of first N numbers using while loop...

#while i <= n:
#    sum += i
#    i += 1
#print("The sum of the first", n, "numbers is:", sum)