p, g = 23, 5

a = int(input("Alice private key: "))
b = int(input("Bob private key: "))

A = pow(g, a, p)
B = pow(g, b, p)

ka = pow(B, a, p)
kb = pow(A, b, p)

print("Alice key:", ka)
print("Bob key:", kb) 