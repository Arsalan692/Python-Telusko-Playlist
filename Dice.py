
from random import randint
from time import sleep

class Dice:
    def __init__(self):
        self.sides = 20

    def roll_dice(self):
        number = randint(1, self.sides)
        print("Rolling...")
        sleep(1)
        print(f"Its {number}")


dice1 = Dice()
dice1.roll_dice()


