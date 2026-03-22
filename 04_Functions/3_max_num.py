# Function to return max of 3 numbers....

def max_num(a,b,c,):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
max_num = max_num(10, 20, 15)
print(max_num)