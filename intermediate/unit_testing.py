import unittest

#standard adding function
def add(a, b):
    return a+b

class TestAddition(unittest.TestCase):
    #define the first unit test
    def test_add(self):
        result = add(3,4)
        
        #define expected result:
        expected_result = 7
        self.assertEqual(result, expected_result)
        
    def test_add2(self):
        result = add(4,4)
        
        expected_result = 8
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()