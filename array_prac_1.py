import array as a
arr = a.array("i", [])
purpose = input("Do you want search a value or add some values in array (search/add)? : ")
if purpose == "add":
    num = int(input("How much values do you want to add in your array? : "))

    for i in range(num):
        values = int(input("Enter a value to add: "))
        arr.append(values)

    print(f"ADDED: {arr}")

    ask_num = int(input("Enter the index value of the number you want to search: "))
    print(arr[ask_num])













