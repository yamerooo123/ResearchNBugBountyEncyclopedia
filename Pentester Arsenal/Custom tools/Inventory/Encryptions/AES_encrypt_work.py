from cryptography.fernet import Fernet

# paste encrpyted message here
encrypted_message = b"encrypted message"
enc_key = b"encrypted key"

f = Fernet(enc_key)

# decrypt the message
try:
    decrypted_message = f.decrypt(encrypted_message)
    print(f"Decryption Success! The decrypted message is: {decrypted_message.decode()}")
except Exception as e:
    print(f"Decryption Failed: {e}")
