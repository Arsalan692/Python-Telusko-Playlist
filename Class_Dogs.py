
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def sit(self):
        print(f"{self.name} has been sitted")


    def roll(self):
        print(f"{self.name} has over rolled")

    def info(self):
        print(f"This dog's name is {self.name}\nThis dog's age is {self.age}")



dog1 = Dog("Harry", 9)
dog2 = Dog("Tommy", 12)

print(dog1.name)
dog2.roll()

