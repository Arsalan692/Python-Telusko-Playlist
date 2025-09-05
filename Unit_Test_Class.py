from Journal_Practice import AnonymousSurvey


question = "What is your name? "

survey1 = AnonymousSurvey(question)
survey1.show_question()
print("Enter 'q' to quit")
while True:

    usr_response = input("Enter your response: ")
    if usr_response == "q":
        break
    survey1.store_response(usr_response)
    survey1.show_response()

print("Thanks for participating in this survey")

