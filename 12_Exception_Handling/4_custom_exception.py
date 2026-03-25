# Create Custom Exception..

class AgeError(Exception):      #custom error
    pass

try:
    age = int(input("Enter age: "))
    
    if age < 18:
        raise AgeError("You are not eligible!")     #raise → manually error throwing
    
    print("You are eligible!")

except AgeError as e:
    print(e)