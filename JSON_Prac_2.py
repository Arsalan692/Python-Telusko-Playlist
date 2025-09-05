
import json

def ask_fav_number():
    usr_fav_num = input("Enter your favorite number: ")
    with open("users.json", "w") as f:
        json.dump(usr_fav_num, f)

def tell_fav_num():
    with open("users.json") as f1:
        fav_num = json.load(f1)
        print(f"I know your favorite number! It's {fav_num}")


tell_fav_num()



