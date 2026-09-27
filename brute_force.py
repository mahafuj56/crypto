

# Write a Python program to decrypt a Caesar Cipher encrypted message using brute-force attack.

def encrypt(text, shift):
    return ''.join(
        chr((ord(c) - (65 if c.isupper() else 97) + shift) % 26 + (65 if c.isupper() else 97))
        if c.isalpha() else c for c in text)

def decrypt(text, shift):
    return encrypt(text, -shift)

def brute_force(cipher):
    for shift in range(26):
        print(f"Shift {shift:2d}:", decrypt(cipher, shift))

text = input("Plain text: ")
shift = int(input("Shift: "))

cipher = encrypt(text, shift)
print("Encrypted:", cipher)
print("Decrypted:", decrypt(cipher, shift))
print()
brute_force(cipher)


# Plain text: HELLO
# Shift: 3