
class Restaurant:

    def __init__(self, res_name, cuisine_type):
        self.res_name = res_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.res_name}")
        print(f"The cuisine type of the restaurant is {self.cuisine_type}")

    def open_status(self):
        print("yes it is open! ")

    def set_number_served(self, served_value):
        self.number_served = served_value

    def increment_number_served(self, num):
        self.number_served += num


restaurant1 = Restaurant("RIDE IN", "Italian")

class IceCreamStand(Restaurant):
    def __init__(self, res_name, cuisine_type, flavor=None):
        super().__init__(res_name, cuisine_type)
        self.flavor = flavor

    def display_flavors(self):
        self.flavor = ["chocalate", 'vanilla', "Strawberry"]
        print(self.flavor)

stand1 = IceCreamStand("Thanda Ice Cream","Cold","vanilla")



