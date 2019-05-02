class User():
    """Collect and manage user info."""

    def __init__(self, first_name, last_name, age, hometown):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.hometown = hometown.title()
        self.login_attempts = 0

    def describe_user(self):
        """Describe a user."""
        msg = self.first_name + " " + self.last_name + " is " + str(self.age) + " years old and is from " + self.hometown +"."
        print(msg)

    def greet_user(self):
    	"""Say 'hello' to the user."""
    	print("Hello, " + self.first_name + "!")

    def increment_login_attempts(self):
        """Increase the number of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Bring the number of login attempts back to 0."""
        self.login_attempts = 0    

class Admin(User):
    """Create an admin user."""
    def __init__(self, first_name, last_name, age, hometown):
        super().__init__(first_name, last_name, age, hometown)
        self.privileges = ['can ban user', 'can add user', 'can add post', 'can delete post']
    
    def show_privileges(self):
        print('You have the following privileges:')
        for privilege in self.privileges:
            print(privilege)

john = Admin('john', 'smith', '30', 'miami')

john.greet_user()
john.show_privileges()