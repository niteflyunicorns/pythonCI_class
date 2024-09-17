import unittest 
from prime import is_prime 

class PrimesTestCase(unittest.TestCase):
   def test_is_five_prime(self):    
      self.assertTrue(is_prime(5)) 
	   
    # Test for prime numbers
    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))      # 2 is a prime
   

if __name__ == '__main__':
	unittest.main()
