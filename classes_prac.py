
class Falcon9:

    def __init__(self):
        print("Its an init function. ")

    def feature1(self):
        print("Amazing speed ")

    def feature2(self):
        print("Heavy motors and steel ")

class Falcon10:

    def __init__(self):
        print("Its in B init ")

    def feature3(self):
        print("Rocket launcher ")

    def feature4(self):
        print("Two seat capacity ")

class Falcon11(Falcon9,Falcon10):

    def __init__(self):
        super().__init__()
        print("Its in 11 class")



pilot1 = Falcon11()

















