import unittest
from Unit_Employee import Employee

class test_employee(unittest.TestCase):

    def test_give_default_raise(self):
        employ1 = Employee("Arsalan", "Ahmed", 10000)
        def_salary = employ1.give_raise()
        self.assertEqual(def_salary, 15000)

    def test_give_custom_raise(self):
        employ1 = Employee("Arsalan", "Ahmed", 10000)
        custom_raise = 7000
        cus_salary = employ1.give_raise(custom_raise)
        self.assertEqual(cus_salary, 17000)


if __name__ == "__main":
    unittest.main()



