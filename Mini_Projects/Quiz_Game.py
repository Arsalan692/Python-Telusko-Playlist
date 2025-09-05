
user_name = input("Enter your name: ")
print(f"Hey {user_name.strip()},")
ask_playing = input("Do you want to play a quiz game?(yes/no) ")
if ask_playing.lower().strip() != "yes":
    quit()

print("This quiz consist of five questions. ")

score = 0

#QUESTION 1:
answer1 = input("Who is called the father of computer?\nAnswer: ")
if answer1.lower() == "charles babbage":
    print("Correct answer")
    score += 1
else:
    print("Wrong answer")

#QUESTION 2:
answer2 = input("When was python invented?\nAnswer: ")
if answer2.lower() == "1991":
    print("Correct answer")
    score += 1
else:
    print("Wrong answer")

#QUESTION 3:
answer3 = input("Who designed python?\nAnswer:  ")
if answer3.lower() == "guido van rossum":
    print("Correct answer")
    score += 1
else:
    print("Wrong answer")

#QUESTION 4:
answer4 = input("Who is the best hacker in the World?\nAnswer:  ")
if answer4.lower() == "kevin mitnick":
    print("Correct answer")
    score += 1
else:
    print("Wrong answer")

#QUESTION 5:
answer5 = input("Who was the first programmer in the World?\nAnswer:  ")
if answer5.lower() == "ada lovelace":
    print("Correct answer")
    score += 1
else:
    print("Wrong answer")


print(f"You answer {score} questions correctly")
print(f"You got 5 out of {score} and your percentage is {(score / 5) * 100}%")

print(f"\n THANKS FOR PLAYING THE GAME! ")







