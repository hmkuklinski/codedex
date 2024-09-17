import unittest
import Python1.codedex.intermediate.bank_account as bank_account

class TestBankAccount(unittest.TestCase):
    #test correct initialization of bank account amount
    def test_initial_balanace(self):
        self.assertEqual(self.account.balance, 100)
    #define the setup function
    def setUp(self):
        self.account= bank_account.BankAccount(100)
    #define the teardown function
    def teardown(self):
        self.account = None
    #check the deposit function works
    def test_deposit_positive_amount(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)
    #check value error if call deposit but don't actually deposit
    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

if __name__ == '__main__':
    unittest.main()
    