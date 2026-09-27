# Write a Python program to encrypt and decrypt a message using a Monoalphabetic Substitution Cipher

import random
import string

def generate_cipher():
    # Generate a random substitution mapping (A → random letter)
    return dict(zip(string.ascii_uppercase, random.sample(string.ascii_uppercase, 26)))

def encrypt(text, cipher):
    # Replace each letter in text using the cipher mapping
    return ''.join(cipher.get(c, c) for c in text.upper())

def decrypt(ciphertext, cipher):
    # Reverse the cipher mapping to get the original text
    reverse_cipher = {v: k for k, v in cipher.items()}
    return ''.join(reverse_cipher.get(c, c) for c in ciphertext.upper())

# Generate cipher
cipher = generate_cipher()

# User input
text = input("Enter the Plain text: ")

# Encrypt and decrypt
encrypted = encrypt(text, cipher)
decrypted = decrypt(encrypted, cipher)

# Display results
print("\nInput Text      :", text)
print("Cipher Mapping  :", cipher)
print("Encrypted Text  :", encrypted)
print("Decrypted Text  :", decrypted)






