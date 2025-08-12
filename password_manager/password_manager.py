PASSWORD = "password.txt"


def add():
    a_name = input("Account Name: ")
    pwd = input("Password: ")
    with open(PASSWORD, "a") as file:
        file.write(a_name + "|" + pwd + "\n")
    print("Password saved successfully!")


def view():
    with open(PASSWORD, "r") as file:
        lines = file.readlines()
        for line in lines:
            account, password = line.strip().split("|")
            print(f"Account: {account}, Password: {password}")


while True:
    mode = input("Type 'add' to save, 'view' to read, or 'q' to quit: ").strip().lower()

    if mode == "q":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode.")
