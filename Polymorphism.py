
class Pycharm:

    def execute(self):
        print("starting")
        print("running")

    def simple_print(self):
        print("something! ")

class Atom:

    def execute(self):
        print("Starting ")
        print("running ")
        print("modifying ")


class Computer:

    def code(self, ide):
        ide.execute()


computer1 = Computer()
ide = Pycharm()
mod_ide = Atom()
computer1.code(mod_ide)












