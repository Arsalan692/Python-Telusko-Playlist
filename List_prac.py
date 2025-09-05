lst = []

print("enter 'q' to quit")
while True:
    user_input = input("Enter the name: ")
    if user_input.lower() == "q":
        break
    lst.append(user_input.title())

for i in lst:
    lst2 = [i]
    print(lst2)