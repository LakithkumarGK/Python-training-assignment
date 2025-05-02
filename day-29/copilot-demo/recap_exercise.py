class Car(object):

    # Class variables
    nCars = 0

    # Constructor
    def __init__(self, brand, model, year, mileage=0): # double underscored = dunder
        # Instance variables
        self.brand = brand
        self.model = model
        self.year  = year
        self.mileage = mileage

    # Member functions
    def drive(self, distance):
        self.mileage += distance

    def display_info(self):
        print("BRAND".ljust(10), '|', self.brand)
        print("MODEL".ljust(10), '|', self.model)
        print("YEAR".ljust(10), '|', self.year)
        print("MILEAGE".ljust(10), '|', self.mileage)


# Extending the Car to an ElectricCar -> Inheritance        

class ElectricCar(Car):

    def __init__(self, brand, model, year, mileage=0, battery=10):
        super().__init__(brand, model, year, mileage)  # initialize the parent with appropriate values
        # local to ElectricCar - instance variables
        self.battery = battery

    # Newly added mothod
    def charge(self, units):
        self.battery += units

    # Overridden methods to accomodate the changes in the electric car
    def drive(self, distance):
        self.battery -= distance/10  # charge reduces 1 unit for 10 KMS driven -> assumption

    def display_info(self):
        super().display_info()
        print("CHARGE".ljust(10), '|', self.battery)

# Test code

if __name__ == "__main__":

    c1 = Car("Toyota", "Innova Crysta", 2024, 1000)
    c1.drive(100)
    c1.display_info()

    print("\n")

    c2 = ElectricCar("Hyundai", "IONIQ", 2024, 1000, 10)
    c2.drive(50)
    c2.charge(300)
    c2.display_info()