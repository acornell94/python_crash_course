import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    """Test the class Employee."""

    def setUp(self):
        """Create an employee to use for all tests."""
        self.bob = Employee('bob', 'vance', 50000)

    def test_give_default_raise(self):
        """Test to see if the default raise of $5,000 works correctly."""
        self.bob.give_raise()
        self.assertEqual(self.bob.salary, 55000)

    def test_custom_raise(self):
        """Test to see if a custom raise will work."""
        self.bob.give_raise(6000)
        self.assertEqual(self.bob.salary, 56000)

unittest.main()