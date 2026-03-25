# Use try-except-else-finally...

try:
    num1 = int(input('Enter number: '))
    num2 = int(input('Enter divisor: '))

    result = num1 / num2

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Invalid input!")

else:
    print("Result:", result)

finally:
    print("perfect!!!")