def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x


key = input("Enter 4-letter key: ").upper()
text = input("Enter Text: ").upper().replace(' ', '')
if len(text) % 2:
    text += 'X'

key_matrix = [[ord(key[0]) - 65, ord(key[1]) - 65],
              [ord(key[2]) - 65, ord(key[3]) - 65]]

det = (key_matrix[0][0] * key_matrix[1][1] -
       key_matrix[0][1] * key_matrix[1][0]) % 26
inv_det = mod_inverse(det, 26)
inverse_matrix = [[(key_matrix[1][1] * inv_det) % 26, (-key_matrix[0][1] * inv_det) % 26],
                  [(-key_matrix[1][0] * inv_det) % 26, (key_matrix[0][0] * inv_det) % 26]]


def hill_cipher(text, matrix):
    result = ""
    for i in range(0, len(text), 2):
        p1, p2 = ord(text[i]) - 65, ord(text[i + 1]) - 65
        c1 = (matrix[0][0] * p1 + matrix[0][1] * p2) % 26
        c2 = (matrix[1][0] * p1 + matrix[1][1] * p2) % 26
        result += chr(c1 + 65) + chr(c2 + 65)
    return result


encrypted = hill_cipher(text, key_matrix)
decrypted = hill_cipher(encrypted, inverse_matrix)

print(f"Key Matrix: {key_matrix}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
