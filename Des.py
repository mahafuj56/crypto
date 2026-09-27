from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

message = input("Enter a Message: ").encode()
key = input("Enter an 8-character key: ").encode()

cipher = DES.new(key, DES.MODE_ECB)

encrypted = cipher.encrypt(pad(message, DES.block_size))
decrypted = unpad(cipher.decrypt(encrypted), DES.block_size)

print("Encrypted Message:", encrypted.hex())
print("Decrypted Message:", decrypted.decode())