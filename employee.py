class Employee():
    """Create a representation of an employee."""

    def __init__(self, first_name, last_name, salary):
        """Initialize the employee."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary

    def give_raise(self, increase=5000):
        """Increase salary by $5,000 unless otherwise specified."""
        self.salary += increase