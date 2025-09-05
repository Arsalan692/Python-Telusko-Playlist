#QUESTION
#Print fibonacci numbers till given range.


list1 = [0, 1]
usr_input = int(input("Enter the range number to stop fibonacci sequence: "))
convert = str(usr_input)
if usr_input ==1:
    print(0)
    quit()
elif usr_input == 2:
    print(1)
    quit()
elif convert[0] =="-":
    print("Invalid")
    quit()
else:
    for i in range(usr_input - 2):
        addition = list1[-2] + list1[-1]
        list1.append(addition)






















