# E1-6	Write a Python program to encrypt and decrypt a message using the Playfair Cipher.

import string

def make_matrix(key):
    key = "".join(dict.fromkeys((key+"ABCDEFGHIKLMNOPQRSTUVWXYZ").upper().replace("J","I")))
    return [key[i:i+5] for i in range(0,25,5)]

def find(m, c):
    for i in range(5):
        if c in m[i]:
            return i, m[i].index(c)

def prepare(t):
    t = t.upper().replace("J","I").replace(" ","")
    p, i = [], 0
    while i < len(t):
        a = t[i]; b = t[i+1] if i+1<len(t) else 'X'
        if a == b: p.append(a+'X'); i += 1
        else: p.append(a+b); i += 2
    return p

def encrypt(text, key):
    m = make_matrix(key)
    res = ""
    for a,b in prepare(text):
        r1,c1 = find(m,a); r2,c2 = find(m,b)
        if r1==r2: res += m[r1][(c1+1)%5] + m[r2][(c2+1)%5]
        elif c1==c2: res += m[(r1+1)%5][c1] + m[(r2+1)%5][c2]
        else: res += m[r1][c2] + m[r2][c1]
    return res

def decrypt(text, key):
    m = make_matrix(key)
    res = ""
    for i in range(0,len(text),2):
        a,b = text[i], text[i+1]
        r1,c1 = find(m,a); r2,c2 = find(m,b)
        if r1==r2: res += m[r1][(c1-1)%5] + m[r2][(c2-1)%5]
        elif c1==c2: res += m[(r1-1)%5][c1] + m[(r2-1)%5][c2]
        else: res += m[r1][c2] + m[r2][c1]
    return res

# test
k = "MONARCHY"
msg = "INSTRUMENTS"

e = encrypt(msg, k)
d = decrypt(e, k)

print("Enc:", e)
print("Dec:", d)


# Enter key: MONARCHY
# Enter message: INSTRUMENTS

# Key      : MONARCHY
# Encrypted: GATLMZCLRQXA
# Decrypted: INSTRUMENTSX