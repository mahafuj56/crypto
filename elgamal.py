import random

p = 257
g = 2

private_key = random.randint(2, p - 2)
public_key = pow(g, private_key, p)

message = input("Enter message: ")

encrypted = []
for char in message:
    m = ord(char)
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    c2 = (m * pow(public_key, k, p)) % p
    encrypted.append((c1, c2))

decrypted = ""
for c1, c2 in encrypted:
    s = pow(c1, private_key, p)
    m = (c2 * pow(s, -1, p)) % p
    decrypted += chr(m)

print(f"Public Key: (p={p}, g={g}, y={public_key})")
print(f"Private Key: {private_key}")
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)