



a = 10
b = 5

try:
    print("opened")
    print(a/b)
    usr_input = int(input("Enter a number: "))
    print(usr_input)
except ZeroDivisionError as e:
        print("Hey, you cannot divide a number by zero", e)

except ValueError as e:
    print("Invalid value")

finally:
    print("closed")

