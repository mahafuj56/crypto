def caesar(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result


message = input("Enter message (Original): ")
S = int(input("Enter shift value (K): "))

ciphertext = caesar(message, S)
plaintext = caesar(ciphertext, -S)

print("Ciphertext (Encrypted ):", ciphertext)
print("Plaintext (Decrypted ): ", plaintext)