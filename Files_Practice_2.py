

while True:
    usr_input1 = input("Enter your name: ")
    if usr_input1 == "quit":
        break
    print(f"Hey {usr_input1}.. ")

    usr_input2 = input("Why you like programming? : ")

    if usr_input2 == "quit":
        break

    with open("guest_book.txt", "a") as file_object:
        file_object.write(f"\n{usr_input1} likes programming because,\n\t{usr_input2}")

