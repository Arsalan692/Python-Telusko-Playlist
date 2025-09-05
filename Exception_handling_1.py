


print("Give me two numbers and I will divide them.. ")
print("Enter 'q' to quit")

while True:
    usr_input1 = input("Enter first number: ")
    if usr_input1.lower() == "q":
        break
    usr_input2 = input("Enter second number: ")
    if usr_input2.lower() == "q":
        break
    try:
        final_result = int(usr_input1) / int(usr_input2)

    except ZeroDivisionError:
        print("You cannot divide a number by zero")
    except ValueError:
        pass

    else:
        print(f"your answer is {final_result}")

