
user_input = input("Enter a year: ")
if user_input[-1] and user_input[-2] == "0":
    if int(user_input) % 400 == 0:
        print(f"{user_input} is a leap year. ")
    else:
        print(f"{user_input} is not a leap year. ")
    quit()

if int(user_input) % 4 == 0:
    print(f"{user_input} is a leap year. ")
else:
    print(f"{user_input} is not a leap year. ")








