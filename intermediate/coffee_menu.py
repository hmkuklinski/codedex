import unittest

class CoffeeMenu:
    def __init__(self):
        self.menu = {
        'espresso': 2.50,
        'latte': 2.75,
        'cappuccino': 3.20,
        'americano': 2.70
        }
    #creating an add method for the dictionary:
    def add_item(self, item, price):
        self.menu[item]= price
    
    #to return value for key specified (aka menu item)   
    def get_price(self, item):
        #if not found, default will return None
        #if found, returns item's price from dictionary
        return self.menu.get(item, None)
        
    
class TestCoffeeMenu(unittest.TestCase):
    #setUp function:
    def setUp(self):
        self.coffee_menu = CoffeeMenu()
    #teardown function:
    def teardown(self):
        self.coffee_menu = None
    
    #get test for item on menu:
    def test_get_price_existing_item(self):
        #pick an item we know is in the menu and return price
        self.assertEqual(self.coffee_menu.get_price('americano'), 2.70)
        
    #if item isn't on menu:
    def test_get_price_non_existing_item(self):
        self.assertNotIn('mocha', self.coffee_menu.menu)
        
    #test for seeing if item was added to menu:
    def test_add_item(self):
        self.coffee_menu.add_item('mocha', 2.80) #specify item and price
        self.assertIn('mocha' ,self.coffee_menu.menu)
        
if __name__ == '__main__':
    unittest.main()