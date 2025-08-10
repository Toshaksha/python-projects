# 🔐 Simple Password Manager 

A beginner-friendly command-line **Password Manager** built in Python.
Securely store, encrypt, and view your passwords using basic encryption.

---

## 📦 Features

- ➕ Add new account-password entries
- 👁️ View saved (decrypted) passwords
- 🔒 Passwords encrypted using the `cryptography` library (`Fernet`)
- 🧠 Protected by a **master password**
- ✅ Clean and beginner-friendly command-line interface

---

## ⚙ How It Works

- When first run, generates a unique encryption key stored in `key.key`
- Passwords are stored in `password.txt`, but encrypted using the `Fernet` algorithm
- Access is protected with a **master password**
- You can **add** or **view** saved credentials via prompts

---

## 🛠 Requirements

- Python 3.x
- [`cryptography`](https://pypi.org/project/cryptography/) module

To install it:

```bash
pip install cryptography
```

---

## ▶️ How to Run

    password_manager.py

You'll be prompted for the master password.
Then you can choose to add, view, or quit.

---

## 💡 Sample Output

```txt
Enter the master password: ****
🔧 What would you like to do?
Type 'add' to save, 'view' to read, or 'q' to quit.
> view

🔐 Account: gmail, Password: mySecret123
🔐 Account: github, Password: codeisfun
```

---

## 🎯 What I Learned

- Basic file I/O in Python
- Symmetric encryption with cryptography.Fernet
- Input validation and clean program structure
- Building secure CLI tools

---

## 🙋‍Credits
Made by Toshaksha - 🔐 Because even beginners deserve encryption!
