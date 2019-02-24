class Restaurant():
    def __init__(self, name, type):
        self.name = name.title()
        self.type = type
    def describe_restaurant(self):
        message = self.name.title() + " is a lovely " + self.type + " restaurant."
        print(message)
    def open_restaurant(self):
        message = "\nWelcome! " + self.name.title() + " is open!"

restaurant = Restaurant('Ginos', 'Italian')
restaurant.describe_restaurant()

restaurant = Restaurant('The Inn', 'German')
restaurant.describe_restaurant()

restaurant = Restaurant('Lakeside', 'seafood')
restaurant.describe_restaurant()