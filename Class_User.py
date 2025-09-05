

class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = f"{self.first_name.title()} {self.last_name.title()}"
        self.login_attempts = 0


    def describe_user(self):
        print(f"The name of the user is {self.full_name}")
        print(f"{self.full_name}'s age is {self.age}")

    def greet_user(self):
        print(f"Hey {self.full_name}, Welcome to the company")

    def increment_login_attempts(self):
        while self.login_attempts <= 5:
            self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0



user2 = User("Arsalan", "Ahmed", 17)

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Admin authorities: ")
        for i in self.privileges:
            print(f"- {i}")



class Admin(User):
    def __init__(self, first_name, last_name, age ):
        super().__init__(first_name, last_name, age)
        self.authorities = Privileges()







