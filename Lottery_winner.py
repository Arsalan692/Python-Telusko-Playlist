
from random import choice


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"if your four number or or word matches with this list then you will win a prize")
my_ticket = [3, 6, 8]

j = 0
while j < 10000:
    ran_choice = []
    for i in range(3):
        choiced = choice(lst)
        ran_choice.append(choiced)
    if ran_choice == my_ticket:
        print(ran_choice)
        print(j)
        break
    else:
        j += 1






