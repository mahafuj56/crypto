def encrypt(text, key):
    order = sorted(range(len(key)), key=lambda i: key[i])
    text += 'X' * (-len(text) % len(key))
    rows = [text[i:i + len(key)] for i in range(0, len(text), len(key))]
    return "".join("".join(row[i] for row in rows) for i in order)


def decrypt(cipher, key):
    order = sorted(range(len(key)), key=lambda i: key[i])
    col_len = len(cipher) // len(key)
    cols = [cipher[i * col_len:(i + 1) * col_len] for i in range(len(key))]
    rows = [""] * col_len
    for pos, col_index in enumerate(order):
        for r in range(col_len):
            rows[r] += cols[pos][r]
    return "".join(rows)


message = input("Enter message: ").replace(" ", "").upper()
key = input("Enter key: ").upper()

first_pass = encrypt(message, key)
double_encrypted = encrypt(first_pass, key)

first_decrypt = decrypt(double_encrypted, key)
decrypted = decrypt(first_decrypt, key)

print("Encrypted:", double_encrypted)
print("Decrypted:", decrypted)