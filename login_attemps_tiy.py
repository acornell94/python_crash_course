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
    	print("Hello, " + self.first_name)

    def increment_login_attempts(self):
        """Increase the number of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Bring the number of login attempts back to 0."""
        self.login_attempts = 0    

user_1 = User('jake', 'adams', 11, 'san diego')
user_1.describe_user()
user_1.greet_user()
print("\nAttempting to log in 3 times.")
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print("Login attempts: " + str(user_1.login_attempts))
print("\nResetting login attempts:")
user_1.reset_login_attempts()
print("Login attempts: " + str(user_1.login_attempts))