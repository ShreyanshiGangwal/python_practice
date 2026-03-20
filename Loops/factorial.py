# Factorial using loop....

num = int(input("Enter a number: "))

fact = 1
while num > 0:
    fact *= num
    num -= 1
print("The factorial is:", fact)

#using for loop
#for i in range(1, num + 1):
#    fact *= i
#print("The factorial is:", fact)