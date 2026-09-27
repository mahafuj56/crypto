from math import gcd

p = int(input("Enter prime p: "))

# Find primitive root
for g in range(2, p):
    if len({pow(g, i, p) for i in range(1, p)}) == p - 1:
        break

print("Primitive root =", g)
print("Elements =", [pow(g, i, p) for i in range(1, p)])

a = int(input("Enter exponent a: "))
A = pow(g, a, p)

print("g^a mod p =", A)
print("Inverse   =", pow(A, -1, p))
