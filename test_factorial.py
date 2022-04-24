from factorial import fact
from termcolor import cprint
import unittest

# Testing the fact module using my own function
def test_factorial(test_value, expected_value):
    if fact(test_value) == expected_value:
        cprint(f":) factorial of {test_value} is {fact(test_value)}, expected {expected_value}", color="green")
    else:
        cprint(f":( factorial of {test_value} is {fact(test_value)}, expected {expected_value} not {fact(test_value)}", color="red")

print("\nTest using my own function:")
test_factorial(0, 1)
test_factorial(1, 1)
test_factorial(2, 2)
test_factorial(3, 6)

# Testing fact funtion using assertions. Advantage - reduce posibility of error in testing script
# However not user friendly as the output error message is a bit cryptic
def assertion_test():
    assert fact(0) == 1
    assert fact(1) == 1
    assert fact(2) == 2
    assert fact(3) == 6

print("\nTest using assertions:")
assertion_test()

# Better - user friendly output messages with minimum code as possible
class Tests(unittest.TestCase):
    
    def test_0(self):
        """Test if factorial of 0 is 1"""
        self.assertTrue(fact(0) == 1)

    def test_1(self):
        """Test if factorial of 1 is 1"""
        self.assertTrue(fact(1) == 1)

    def test_2(self):
        """Test if factorial of 2 is 2"""
        self.assertTrue(fact(2) == 2)

    def test_3(self):
        """Test if factorial of 3 is 6"""
        self.assertTrue(fact(3) == 6)

print("\nTest using unittest module:")
unittest.main()