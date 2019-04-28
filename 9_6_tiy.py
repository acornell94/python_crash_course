class Restaurant():
    """Create a restaurant"""

    def __init__(self, name, food_type):
        self.name = name
        self.food_type = food_type
        self.number_served = 0

    def describe_restaurant(self):
        """describe restaurant and determine if 'a' or 'an' is appropriate."""
        if self.food_type[0] == 'aeiou': 
            print(self.name.title() + " is an " + self.food_type + " restaurant.")
        else:
            print(self.name.title() + " is a " + self.food_type + " restaurant.")

    def open_restaurant(self):
        """Declare the restuarant is open."""
        print(self.name.title() + " is now open!")

    def number_of_people_served(self):
        """Determine how many people have been served."""
        print(str(self.number_served) + " people have been served today!")

class IceCreamStand(Restaurant):
    """Create a representation of an Ice Cream Stand."""

    def __init__(self, name, food_type='ice cream'):
        super().__init__(name, food_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry', 'mint']

    def list_flavors(self):
        """Display ice cream flavors"""
        print("We have the following flavors of ice cream available:")
        for flavor in self.flavors:
            print(flavor.title())

edwardsville_ice_cream_stand = IceCreamStand('Edwardsville Ice Cream Stand')
edwardsville_ice_cream_stand.list_flavors()