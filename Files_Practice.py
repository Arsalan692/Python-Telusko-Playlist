while True:
    usr_input = input("Enter your name: ")
    print(f"Hey {usr_input},\n\tWelcome in our company. ")
    if usr_input == "quit":
        break
    with open("guest_book.txt", "a") as file_object:
        file_object.write(f"\n{usr_input} visited our company")
