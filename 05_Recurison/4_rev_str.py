# Reverse a string using recursion.....

def rev_str(s):
    if len(s) == 0:
        return s
    else:
        return rev_str(s[1:]) + s[0]  # s[1:] is the string without the first character and s[0] is the first character. We are calling the function recursively on the string without the first character and then adding the first character at the end of the result.
    
print(rev_str("Hello World"))