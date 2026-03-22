# Swap two variables (without using third variable).

a = 5
b = 10
print("Before swapping: a =", a, "b =", b)

a = a + b           # 5+10 = 15
b = a - b           # 15-10 = 5
a = a - b           # 15-5 = 10
print("After swapping: a =", a, "b =", b)
