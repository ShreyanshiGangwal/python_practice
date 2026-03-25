# Multiple exceptions handling....

try:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter divisor: "))
    
    result = num1 / num2
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Invalid input!")

except Exception as e:
    print("Something went wrong:", e)