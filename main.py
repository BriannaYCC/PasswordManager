from cryptography.fernet import Fernet
import sys
import key_manager
from pathlib import Path

authUsernames = []
authPasswords = [] 

# key to decode, cipher does the work 
filePath = Path("adminKeys.keys")
if not filePath.exists():
    key_manager.gen_and_save_key("adminKeys.keys")
cipher = Fernet(key_manager.getKey())

# load existing passwords from files

def loadExistingPasswords():
    try:
        # check if files exist
        with open("usernames.txt", "rb") as usersFile:
            encryptedUsers = usersFile.readlines()
            
        with open("passwords.txt", "rb") as passwordsFile:
            encryptedPasswords = passwordsFile.readlines()

        for encryptUser, encryptPassword in zip(encryptedUsers, encryptedPasswords):
            decryptedUser = cipher.decrypt(encryptUser.strip())
            decryptedPassword = cipher.decrypt(encryptPassword.strip())

            authUsernames.append(decryptedUser.decode())
            authPasswords.append(decryptedPassword.decode())    
    except FileNotFoundError:
        # if no credentials or file doesn't exist
        pass

# decodes username and password, then prints result
def displayPasswords():
    if len(authUsernames) == 0:
        print("\nNo passwords found")
    else:
        # decrypting and handling of file is done elsewhere
        # assumes file is decrypted and info is put into list
        for i in range(len(authUsernames)):
            print("U: " + authUsernames[i] + " P: " + authPasswords[i])

# encodes and encrypts username/password and saves
def createPassword(username, password):
    encodeUser = username.encode()
    encodePassword = password.encode()

    encryptUser = cipher.encrypt(encodeUser)
    encryptPassword = cipher.encrypt(encodePassword)

    with open("usernames.txt", "ab") as usersFile:
        usersFile.write(encryptUser + b"\n")
    with open("passwords.txt", "ab") as passwordsFile:
        passwordsFile.write(encryptPassword + b"\n")

    authUsernames.append(username)
    authPasswords.append(password)

    print("Password successfully added")


loadExistingPasswords()

while True:
    print("\n[ Password Manager ]")
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
        print("\nPlease enter your username and password.")
        userName = input("Username: ")
        passWord = input("Password: ")

        if userName == "BINC" and passWord == "test":
            break
        else:
            print("\nIncorrect username and/or password")
if userChoice == '2':
    print("Bye user!")
    sys.exit(0)
    

# Confirmed valid user
while True:
    print("\nSelect an option below: ")
    print("[1] View Passwords")
    print("[2] Add a new password")
    
    userChoice = input(": ")
    if userChoice == '1' or userChoice == '2':
        break
    else:
        print("\nInvalid choice. Try again.")
if userChoice == '1':
    displayPasswords()
    while True:
        userChoice = input("\n[Y/N] Would you like to add a new password? ")
        if userChoice == "Y" or userChoice == "y":
            userChoice = '2'
            break
        elif userChoice == "N" or userChoice == "n": 
            print("Okay, bye user!")
            sys.exit(0)
        print("\nInvalid choice. Try again.")

if userChoice == '2':
    # confirm new account information is correct
    while True:
        while True:
            print("\nEnter your preferred username and password.")
            newUser = input("Username: ")
            newPassword = input("Password: ")
            confirmPassword = input("Re-enter password: ")
            if newPassword != confirmPassword:
                print("\nPasswords do not match. Try again.")
            else: 
                break
        # creates new entry
        createPassword(newUser, newPassword)

        print("\nHere are all your passwords: ")
        displayPasswords()

        userChoice = input("\n[Y/N] Would you like to add another? ")
        if userChoice == "N" or userChoice == "n":
            print("Okay, bye user!")
            sys.exit(0)
        elif userChoice == "Y" or userChoice == "y":
            continue
        else:
            print("Invalid input. Bye user!")
    
