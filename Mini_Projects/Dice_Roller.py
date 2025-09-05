import random

print("This is a dice simulator")
while True:
    user_input = input("Press 'R' to roll the dice: ").lower().strip()
    ran_number = random.randint(1, 6)
    if user_input == "q":
        quit()

    if ran_number == 1:
        print("[---------------]")
        print("[               ]")
        print("[       0       ]")
        print("[               ]")
        print("[---------------]")

    elif ran_number == 2:
        print("[---------------]")
        print("[               ]")
        print("[   0       0   ]")
        print("[               ]")
        print("[---------------]")

    elif ran_number == 3:
        print("[---------------]")
        print("[           0   ]")
        print("[       0       ]")
        print("[   0           ]")
        print("[---------------]")
    elif ran_number == 4:
        print("[---------------]")
        print("[   0       0   ]")
        print("[               ]")
        print("[   0       0   ]")
        print("[---------------]")

    elif ran_number == 5:
        print("[---------------]")
        print("[   0       0   ]")
        print("[       0       ]")
        print("[   0       0   ]")
        print("[---------------]")

    elif ran_number == 6:
        print("[---------------]")
        print("[   0       0   ]")
        print("[   0       0   ]")
        print("[   0       0   ]")
        print("[---------------]")








