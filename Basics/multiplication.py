# Take a number and print its multiplication table.

num = int(input("Enter a number: "))
print("Multiplication table of", num)

if num < 0:
    print("Negative numbers are not allowed.")
else:
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)