import os
from cryptography.fernet import Fernet

KEY_FILE = "key.key"
PASSWORD = "password.txt"
MASTER_PASSWORD = "pwd123"

#key generation
def write_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as file:
            file.write(key)

write_key()

# loading key
def load_key():
    with  open(KEY_FILE, "rb") as file:
        return file.read()

key = load_key()
fer = Fernet(key)

m_pwd_entered = input("Enter the master password: ")
if m_pwd_entered != MASTER_PASSWORD:
    print("Access Denied.")
    quit()

def add():
    a_name = input("Account Name: ")
    pwd = input("Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()  # Take a password string → turn it into bytes → encrypt → turn it back into a string.

    with open(PASSWORD, "a") as file:
        file.write(a_name + "|" + encrypted_pwd+ "\n")
        print("✅ Password saved successfully!!")


def view():
    try:
        with open(PASSWORD, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No passwords found.")
                return
            for line in lines:
                account, enc_pwd = line.strip().split("|")
                try:
                    decrypted = fer.decrypt(enc_pwd.encode()).decode()
                    print(f"🔐 Account: {account}, Password: {decrypted}")
                except Exception as e:
                    print(f"⚠ Error decoding password for {account}: {e}")
    except FileNotFoundError:
        print("No Passwords saved yet.")


while True:
    print("\n🔧 What would you like to do?")
    print("Type 'add' to save, 'view' to read, or 'q' to quit.")
    mode = input("> ").strip().lower()
    if mode == "q":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("❌ Invalid mode.")
        continue
