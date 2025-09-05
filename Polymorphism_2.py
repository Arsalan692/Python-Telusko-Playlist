

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        student3 = Student(m1, m2)
        return student3

    def __mul__(self, other):
        m1 = self.m1 * other.m1
        m2 = self.m2 * other.m2
        student4 = Student(m1, m2)
        return student4

    def __gt__(self, other):
        student1_m = self.m1 + self.m2
        student2_m = other.m1 + other.m2
        if student1_m > student2_m:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.m1}, {self.m2}"




student1 = Student(55, 45)
student2 = Student(66, 72)


if student1 > student2:
    print("student1 wins")
else:
    print("student2 wins")

print(student2)


#This is another topic which is method over_loading...

class Student:

    def __init__(self, marks1, marks2):
        self.marks1 = marks1
        self.marks2 = marks2

    def sum(self, a=None, b=None, c=None):

        if a != None and b != None and c != None:
            s = a + b + c
        elif a!=None and b!=None:
            s = a + b
        else:
            s = a
        return s



student1 = Student(98, 69)

print(student1.sum(50, 50, 50))








