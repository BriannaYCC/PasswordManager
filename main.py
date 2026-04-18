from cryptography.fernet import Fernet

key = Fernet.generate_key()

cipher = Fernet(key)

ultraSecretPassword = "Bri4nn42023!"
passwordEncrypted = ultraSecretPassword.encode()

encryptedPassWord = cipher.encrypt(passwordEncrypted)

decryptedPassWord = cipher.decrypt(encryptedPassWord)

print("Here is your password: " + decryptedPassWord.decode())


