from cryptography.fernet import Fernet

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.split("|")
            user, passwd = data
            print(f"User: {user.title()}, Password: {passwd.strip()}")

def add():
    account_name = input("Enter your account name: ")
    account_passwd = input("Enter your account password: ")
    with open("passwords.txt", "a") as f:
        f.write(f"{account_name}|{account_passwd}\n")


master_pwd = input("Enter the master password: ")
if master_pwd != "Akuma69":
    print("Invalid password! ")
    quit()
else:
    print("Correct password")

while True:
    print("\nEnter 'q' any time to quit ")
    mode = input("Do you want to add a password or to view passwords? (Enter 'view' or 'add'): ").lower().strip()
    if mode == "q":
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()





