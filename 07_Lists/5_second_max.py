# Find second largest number...

number = list(map(int, input('Enter numbers separated by space: ').split()))
print('Your list is',number)

largest = number[0]
sec_largest = None

for num in number:
    if num > largest:           # Agar current number sabse bada nikla
        sec_largest = largest   # To old largest → ab second largest ban gaya
        largest = num           # or New number → largest ban gaya
    elif num != largest and (sec_largest is None or num > sec_largest):
        sec_largest = num
    
if sec_largest is None:
    print("No second largest number")
else:
    print("Second largest number is:", sec_largest)