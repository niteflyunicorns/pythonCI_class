import unittest 
from prime import is_prime 

class PrimesTestCase(unittest.TestCase):
   def test_is_five_prime(self):    
      self.assertTrue(is_prime(5)) 

   # Test for invalid input (non-integer)
    def test_non_integer_input(self):
        self.assertFalse(is_prime("10"))  # String input should return False
        self.assertFalse(is_prime(3.5))   # Float input should return False
        self.assertFalse(is_prime([5]))   # List input should return False

    # Test for values less than or equal to 1
    def test_values_less_than_or_equal_to_1(self):
        self.assertFalse(is_prime(0))     # 0 is not a prime
        self.assertFalse(is_prime(1))     # 1 is not a prime
        self.assertFalse(is_prime(-5))    # Negative numbers are not prime

    # Test for prime numbers
    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))      # 2 is a prime
        self.assertTrue(is_prime(3))      # 3 is a prime
        self.assertTrue(is_prime(11))     # 11 is a prime
        self.assertTrue(is_prime(29))     # 29 is a prime

    # Test for non-prime numbers
    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(4))     # 4 is not a prime
        self.assertFalse(is_prime(9))     # 9 is not a prime
        self.assertFalse(is_prime(15))    # 15 is not a prime
        self.assertFalse(is_prime(100))   # 100 is not a prime
   

if __name__ == '__main__':
	unittest.main()
