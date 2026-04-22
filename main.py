from cryptography.fernet import Fernet
import key_manager

# key to decode 
key_manager.gen_and_save_key()

while True:
    print("[ Password Manager ]")
    print("[1] Login")
    print("[2] Exit")
    userChoice = input(": ")
    if userChoice == '1' or userChoice == '2':
        break
    else: 
        print("Invalid selection.")

# Valid selection is made -> proceed 
if userChoice == '1':
    while True:
        print("\n Please enter your username and password.")
        userName = input("Username: ")
        passWord = input("Password: ")

        if userName == "BINC" and passWord == "test":
            cipher = Fernet(key_manager.getKey())
            break
        else:
            print("Incorrect username and/or password")
if userChoice == '2':
    print("Bye user!")

# Confirmed valid user
while True:
    print("Select an option below: ")
    print("[1] View Passwords")
    print("[2] Add a new password")
    userChoice = input(": ")
    if userChoice == '1' or userChoice == '2':
        break
if userChoice == '2':
    
# ultraSecretPassword = "testpassword"
# passwordEncrypted = ultraSecretPassword.encode()

# encryptedPassWord = cipher.encrypt(passwordEncrypted)

# decryptedPassWord = cipher.decrypt(encryptedPassWord)

# print("Here is your password: " + decryptedPassWord.decode())


