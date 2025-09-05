import random

print("Welcome to Rock, Paper, Scissors game let's play it")

user_score = 0
machine_score = 0
draws = 0


my_moves = ["rock", "paper", "scissors"]

print("Enter 'q' any time to quit")

while True:
    user_move = input("\nEnter your move (Rock, Paper or Scissors): ").lower()
    ran_choice = random.choice(my_moves)

    if user_move == ran_choice:
        print(ran_choice.title(), "  (Round Draw)")
        draws += 1
        continue

    elif user_move == "rock" and ran_choice == "paper":
        print(ran_choice.title())
        machine_score += 1

    elif user_move == "rock" and ran_choice == "scissors":
        print(ran_choice.title())
        user_score += 1

    elif user_move == "paper" and ran_choice == "rock":
        print(ran_choice.title())
        user_score += 1

    elif user_move == "paper" and ran_choice == "scissors":
        print(ran_choice.title())
        machine_score += 1

    elif user_move == "scissors" and ran_choice == "rock":
        print(ran_choice.title())
        machine_score += 1

    elif user_move == "scissors" and ran_choice == "paper":
        print(ran_choice.title())
        user_score += 1

    elif user_move == "q":
        break

    else:
        print("Invalid command! (Only 'Rock', 'paper' and 'scissors' are accepted! )")


print(f"Your score is {user_score} and my score is {machine_score} and there were {draws} draws. ")
if user_score > machine_score:
    print("You win! ")
elif user_score == machine_score:
    print("It's a draw! ")
else:
    print("You lose! ")












