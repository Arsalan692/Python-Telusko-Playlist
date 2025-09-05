#QUESTION
#Take 10 names from user and display the number of users whose names are more than 5 letters.


def letter_count(list1):
    print("These are the names whose letter count are more than 5: ")
    for j in list1:
        length = len(j)
        if length > 5:

            print(j)


lst = []
for i in range(10):
    usr_inp = input("Enter a name of any person: ")
    lst.append(usr_inp)

letter_count(lst)










