
import json

def get_stored_username():
    filename = "users.json"
    try:
        with open(filename) as f:
            user = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user


def greet_user():
    user_name = get_stored_username()
    if user_name:
        print(f"welcome back, {user_name}")
    else:
        usr_input = input("Enter your name: ")
        filename = "users.json"
        with open(filename, "w") as f:
            json.dump(usr_input, f)
            print(f"Welcome back {usr_input},\n\tHow may I help you")


print(get_stored_username())
