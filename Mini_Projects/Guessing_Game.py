
import random

user_name = input("Enter your name: ")
print(f"Hey {user_name.title()},")
ask_for_playing = input("Do you wanna play a guessing game? (yes/no) ")

if ask_for_playing.lower().strip() != "yes":
    quit()

try:
    user_number = int(input("Enter a number under which you want to guess numbers: "))
    if user_number <= 0:
        print("Enter a number larger than zero next time!")
        quit()
except ValueError:
    print("Enter digits not alphabets! ")
    quit()

random_number = random.randint(1, user_number)
print("(Enter 'q' any time to quit) ")
print("\nYou have only 3 chances to guess the number! ")
i = 1
state = True
while state:
    usr_guess = input(f"Guess the number: ")
    if i >= 2:
        print(f"0 changes left!, try your best next time")
        print(f"The secret number is {random_number}")
        state = False
        break

    if usr_guess.lower() == "q":
        break
    if int(usr_guess) == random_number:
        print(f"You guessed it!, The number is {random_number} ")
        print(f"You guessed the number in {i} attempts")
        break
    elif int(usr_guess) < random_number:
        print("Your guess is less than the number.. ")
        i += 1
    elif int(usr_guess) > random_number:
        print("Your guess is greater than the number..")
        i += 1


print("Thanks for playing the game! ")











