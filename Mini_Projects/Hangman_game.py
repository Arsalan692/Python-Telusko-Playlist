
import random

user_name = input("Enter your name: ")
print(f"Welcome {user_name}")
print("-------------------")
print("Try to guess the word in less than 10 attempts")

words = ["smoke", "police", "giant", "football", "computer"]
ran_word = random.choice(words)
turns = 10
guess_made = ""
while True:
    main = ""
    for letter in ran_word:
        if letter in guess_made:
            main += letter
        else:
            main += "_ "
    print(f"Guess the word: {main}")
    user_guess = input()
    if user_guess in ran_word:
        guess_made += user_guess

    if main.strip() == ran_word:
        print("You Win")
        break

    if user_guess not in ran_word:
        turns -= 1
        if turns == 9:
            print("  o_________________o")
            print("  |                 |")
            print("  |                  ")
            print("  |                  ")
            print("  |                  ")
            print("  |                  ")
            print("  |                  ")
            print("  |                  ")
            print("  |                  ")
            print("  |                  ")
            print("__|__                ")
        elif turns == 8:
                print("  o_________________o")
                print("  |                 |")
                print("  |                 |")
                print("  |                  ")
                print("  |                  ")
                print("  |                  ")
                print("  |                  ")
                print("  |                  ")
                print("  |                  ")
                print("  |                  ")
                print("__|__                ")
        elif turns == 7:
                print("  o_________________o")
                print("  |                 |")
                print("  |                 |")
                print("  |                 |")
                print("  |                  ")
                print("  |                  ")
                print("  |                  ")
                print("  |                  ")
                print("  |                  ")
                print("  |                  ")
                print("__|__                ")
        elif turns == 6:
                print("  o_________________o")
                print("  |                 |")
                print("  |                 |")
                print("  |                 |")
                print("  |                 O")
                print("  |                  ")
                print("  |                  ")
                print("  |                  ")
                print("  |                  ")
                print("  |                  ")
                print("__|__                ")
        elif turns == 5:
                print("  o_________________o")
                print("  |                 |")
                print("  |                 |")
                print("  |                 |")
                print("  |                 O")
                print("  |                 |")
                print("  |                  ")
                print("  |                  ")
                print("  |                  ")
                print("  |                  ")
                print("__|__                ")
        elif turns == 4:
                print("  o_________________o")
                print("  |                 |")
                print("  |                 |")
                print("  |                 |")
                print("  |                 O")
                print("  |                 |")
                print("  |                 |")
                print("  |                  ")
                print("  |                  ")
                print("  |                  ")
                print("__|__                ")
        elif turns == 3:
                print("  o_________________o")
                print("  |                 |")
                print("  |                 |")
                print("  |                 |")
                print("  |                 O")
                print("  |                 |")
                print("  |                 |")
                print(r"  |                  \ ")
                print("  |                  ")
                print("  |                  ")
                print("__|__                ")
        elif turns == 2:
                print("  o_________________o")
                print("  |                 |")
                print("  |                 |")
                print("  |                 |")
                print("  |                 O")
                print("  |                 |")
                print("  |                 |")
                print(r"  |                / \ ")
                print("  |                  ")
                print("  |                  ")
                print("__|__                ")
        elif turns == 1:
                print("  o_________________o")
                print("  |                 |")
                print("  |                 |")
                print("  |                 |")
                print("  |                 O")
                print("  |               / |")
                print("  |                 |")
                print(r"  |                / \ ")
                print("  |                  ")
                print("  |                  ")
                print("__|__                ")
        elif turns == 0:
                print("  o_________________o")
                print("  |                 |")
                print("  |                 |")
                print("  |                 |")
                print("  |                 O")
                print(r"  |               / | \ ")
                print("  |                 |")
                print(r"  |                / \ ")
                print("  |                  ")
                print("  |                  ")
                print("__|__                ")
                print()
                print("YOU KILLED AN INNOCENT MAN!, YOU FAILED :(")
                break