# Find the largest of three numbers.  
''' 
if we want to find the largest of three numbers with decimal points, 
then we will choose float data type otherwise we can choose int data type.
'''

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
num3 = float(input('Enter the 3rd number: '))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print('The largest number is: ', largest)