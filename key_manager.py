from cryptography.fernet import Fernet
import os

# Generate Keys
def gen_and_save_key():
    key = Fernet.generate_key()
    # writes key into new .keys file in bytes
    with open("adminKeys.keys", "wb") as keyFile:
        keyFile.write(key)

def getKey():
    # checks if keys have been generatd
    if not os.path.exists("adminKeys.keys"):
        print("Error, no valid keys. Generating keys now...")
        gen_and_save_key()
    
    with open("adminKeys.keys", "rb") as keyFile:
        return keyFile.read()
    
