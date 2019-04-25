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

    def set_number_served(self, number):
        """Allow the number of customers served to be manually set and make sure it is a positive change."""
        if number >= self.number_served:
            print(str(number) + " people have been served today!")
        else:
            print("Oops! Please recount.")	

    def increment_number_served(self, added):
        """Adding a number of customers served."""
        self.number_served += added
        print(str(self.number_served) + " people have been served today!")

my_restaurant = Restaurant('The Pub', 'Polish')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.number_of_people_served()
my_restaurant.set_number_served(42)
my_restaurant.increment_number_served(6)