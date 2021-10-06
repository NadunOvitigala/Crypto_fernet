from cryptography.fernet import Fernet

key = open("key.txt","rb")
key = key.read()
cipher = Fernet(key)

with open ("ciphertext" , "rb") as pt:
    cipertext = pt.read()

plaintext = cipher.decrypt(cipertext)

with open ("decryptfile.txt","wb") as ef:
    ef.write(plaintext)