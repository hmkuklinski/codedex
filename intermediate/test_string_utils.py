import unittest
import string_utils

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(string_utils.reverse_string('jisung'), 'gnusij')
    def test_capitalize(self):
        word= 'jisung'
        self.assertTrue(string_utils.capitalize_string(word), 'J' in word)
    def test_is_capitalized(self):
        self.assertFalse(string_utils.is_capitalized('jisung'))
if __name__ == '__main__':
    unittest.main()  
        
        