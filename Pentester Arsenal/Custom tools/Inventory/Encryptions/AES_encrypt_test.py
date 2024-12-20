from cryptography.fernet import Fernet 

# make sure to import Fernet. Fernet เอาไว้เจน encryption key
# make sure to generate only one key and save it in an object
enc_key = Fernet.generate_key()
# print(enc_key) if you want to see raw encryption key
# Make an Fernet encryption key
f = Fernet(enc_key)
# in case you wanna see Fernet encryption key, you can print it out
encryption_key = Fernet.generate_key()
# Fernet encryption key is base64 and HMAC so we have to decode to see it
print(f"This is encrypted key: {encryption_key.decode()}")
enc_this = f.encrypt(b"add something to encrypt")
print(f"Here is your encrypted message:{enc_this}")
# To decrpyt it. If we want to decrypt the message. we need to use f object instead of Fernet.
decrypt_this = f.decrypt(enc_this)
print(f"Decrpytion Success!:{decrypt_this}")
