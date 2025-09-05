
class Car:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year
        self.milage = 0

    def car_info(self):
        return f"Company: {self.company}\nModel: {self.model}\nYear: {self.year}"

    def read_milage(self):
        return f"Milage: {self.milage}"

    def update_milage(self, milage):
        if milage >= self.milage:
            self.milage = milage

    def increment_milage(self, milage_addition):
        self.milage += milage_addition

    def refill_fuel(self):
        print("Fuel refilled ")

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def battery_info(self):
        print(f"The battery of the car is {self.battery_size} kwh")

    def get_range(self):

        if self.battery_size == 75:
            ranges = 154
        elif self.battery_size == 100:
            ranges = 200
        return f"This car can go about {ranges} miles on a full charge"

    def upgrade_battery(self):
        if self.battery_size <= 100:
            self.battery_size = 100


class ElectricCar(Car):

    def __init__(self, company, model, year):
        super().__init__(company, model, year)
        self.battery = Battery()

    def battery_info(self):
        print(f"The battery of the car is {self.battery.battery_size} kwh")


if __name__ == "__main__":
    tesla = ElectricCar("tesla", "S", "2020")
    print(tesla.battery.get_range())
    tesla.battery.upgrade_battery()
    print(tesla.battery.get_range())
