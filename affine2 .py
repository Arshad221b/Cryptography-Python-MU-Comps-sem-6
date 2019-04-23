text = input("Plain text: ")
key = int(input("enter key: "))
print("enrypted :")
encrypt = ""
decrypt = ""


for t in text:
    encrypt += chr((((ord(t)-65+key)%26)) + 65)
print(encrypt)


print("decrypted text: ")


for t in encrypt:
    decrypt += chr((((ord(t)-65-key)%26)) + 65)

print(decrypt)
