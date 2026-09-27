# Write a Python program to encrypt and decrypt a message using the RSA algorithm.

def rsa_keygen(p, q, e):
    n = p * q
    phi = (p-1) * (q-1)
    d = pow(e, -1, phi)
    return (e, n), (d, n)

def rsa_encrypt(m, pub):
    e, n = pub
    return pow(m, e, n) # c = m^e mod n

def rsa_decrypt(c, priv):
    d, n = priv
    return pow(c, d, n) #m = c^d mod n (c=encrpted value= 26)

# Input
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
e = int(input("Enter public exponent e: "))
m = int(input("Enter message (number): "))

# Keys
pub, priv = rsa_keygen(p, q, e)

# Encrypt & Decrypt
c   = rsa_encrypt(m, pub)
dec = rsa_decrypt(c, priv)

# Output
print("\nPublic key :", pub)
print("Private key:", priv)
print("Message    :", m)
print("Encrypted  :", c)
print("Decrypted  :", dec)



# Enter prime p: 3
# Enter prime q: 11
# Enter public exponent e: 3
# Enter message (number): 5

# Public key : (3, 33)
# Private key: (7, 33)
# Message    : 5
# Encrypted  : 26
# Decrypted  : 5