# Check subset 

A = set(map(int, input("Enter elements of set A: ").split()))
B = set(map(int, input("Enter elements of set B: ").split()))

if A.issubset(B):
    print("A is a subset of B")
else:
    print("A is not a subset of B")