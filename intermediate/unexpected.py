import unittest, math

def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b

class TestUnexpected(unittest.TestCase):
    #test for proper square root
    def test_sqrt(self):
        self.assertEqual(get_sqrt(144), 12)
        
    #test for sqrt a negative value --> raises Exception
    def test_negative(self):
        with self.assertRaises(ValueError):
            get_sqrt(-144)
    
    #test for proper division
    def test_divide(self):
        self.assertEqual(divide(144, 12), 12)
        
    #test for dividing by zero --> raises Exception
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            divide(144, 0)
if __name__ == '__main__':
    unittest.main()