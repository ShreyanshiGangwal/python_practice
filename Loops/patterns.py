# Print triangle pattern.....

for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

print('This is the end of triangle pattern')
print()

# print pyramid pattern......
for i in range(5):
    for j in range(5 - i - 1):      # to print spaces
        print(" ", end="")
    for k in range(2 * i + 1):      # to print stars
        print("*", end="")
    print()    

print('This is the end of pyramid pattern')