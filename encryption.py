from cryptography.fernet import Fernet

key = open("key.txt","rb")
key = key.read()
cipher = Fernet(key)

filename = "message.txt"

with open (filename , "rb") as pt:
    plaintext = pt.read()

ciphertext = cipher.encrypt(plaintext)

with open ("ciphertext","wb") as ef:
    ef.write(ciphertext)