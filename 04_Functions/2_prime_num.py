# Function to check prime number......

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):  # num**0.5 is the square root of num
        if num % i == 0:
            return False
    return True

print(is_prime(int(input("Enter a number: "))))