class Car():
    def  __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        complete_name = str(self.year) + " " + self.make.title() + " " + self.model.title()
        return complete_name
my_car = Car('volkswagen', 'jetta', 2007)
print(my_car.describe_car())