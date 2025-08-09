PASSWORD = "password.txt"

while True:
    mode = input("Type 'add' to save, 'view' to read, or 'q' to quit: ").strip().lower()

    if mode == "q":
        break
    elif mode == "add":
        a_name = input("Account Name: ")
        pwd = input("Password: ")
        with open(PASSWORD, "a") as file:
            file.write(a_name + "|" + pwd + "\n")
        print("Password saved successfully!")
    elif mode == "view":
        with open(PASSWORD, "r") as file:
            lines = file.readlines()
            for line in lines:
                account, password = line.strip().split("|")
                print(f"Account: {account}, Password: {password}")
    else:
        print("Invalid mode.")