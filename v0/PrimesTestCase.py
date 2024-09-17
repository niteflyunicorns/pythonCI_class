import unittest 
from prime import is_prime 

class PrimesTestCase(unittest.TestCase):
   def test_is_five_prime(self):    
      self.assertTrue(is_prime(5)) 
	   
   def test_is_nine_prime(self):
      self.assertFalse(is_prime(9))

   def test_non_integer_input(self):
        self.assertFalse(is_prime("10"))

   

if __name__ == '__main__':
	unittest.main()
