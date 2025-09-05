

class A:

    def show(self):
        print("Its in A show")

class B(A):

    def show(self):
        print("Its in B show") #class B is first checking its content then\n
                               # it is coming to its parent class which is class A
                               #this is called method_overriding
                               #because we are overriding the show method(function)


b1 = B()
b1.show()












