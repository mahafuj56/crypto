key = input("Enter Key: ").lower().replace('j', 'i')
text = input("Enter Text: ").lower().replace('j', 'i').replace(' ', '')

matrix = "".join(dict.fromkeys(key + "abcdefghiklmnopqrstuvwxyz"))

prepared = ""
for char in text:
    prepared += char if not prepared or len(
        prepared) % 2 == 0 or prepared[-1] != char else 'x' + char
if len(prepared) % 2:
    prepared += 'x'

encrypted = ""
for i in range(0, len(prepared), 2):
    pos1, pos2 = matrix.index(prepared[i]), matrix.index(prepared[i + 1])
    row1, col1, row2, col2 = pos1 // 5, pos1 % 5, pos2 // 5, pos2 % 5

    if row1 == row2:
        encrypted += matrix[row1 * 5 + (col1 + 1) %
                            5] + matrix[row2 * 5 + (col2 + 1) % 5]
    elif col1 == col2:
        encrypted += matrix[((row1 + 1) % 5) * 5 + col1] + \
            matrix[((row2 + 1) % 5) * 5 + col2]
    else:
        encrypted += matrix[row1 * 5 + col2] + matrix[row2 * 5 + col1]

decrypted = ""
for i in range(0, len(encrypted), 2):
    pos1, pos2 = matrix.index(encrypted[i]), matrix.index(encrypted[i + 1])
    row1, col1, row2, col2 = pos1 // 5, pos1 % 5, pos2 // 5, pos2 % 5

    if row1 == row2:
        decrypted += matrix[row1 * 5 + (col1 - 1) %
                            5] + matrix[row2 * 5 + (col2 - 1) % 5]
    elif col1 == col2:
        decrypted += matrix[((row1 - 1) % 5) * 5 + col1] + \
            matrix[((row2 - 1) % 5) * 5 + col2]
    else:
        decrypted += matrix[row1 * 5 + col2] + matrix[row2 * 5 + col1]

digram_text = " ".join(prepared[i:i + 2] for i in range(0, len(prepared), 2))

print(f"Prepared Text: {digram_text}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
