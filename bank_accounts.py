#Bank Account

class BankAccount:
	def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
		#sets the values of the parameters equal to the object's values
		self.first_name = first_name
		self.last_name = last_name
		self.account_id = account_id
		self.account_type =	account_type
		self.pin = pin
		self.balance = balance
	
	#we use the self.balance to refer to the object's balance value!
	def deposit(self, amount):
		self.balance += amount 
		return self.balance
	
	def withdraw(self, amount):
		self.balance -= amount
		return self.balance
	
	#by using a formatted print statement, can insert our variable in curly brackets- will automatically fill in the value
	def display_balance(self):
		print(f"${self.balance}")

#create a new object called new_account of the class BankAccount
new_account= BankAccount("Hannah", "mac", 12345, "checking", 1111, 250.00)

#call methods on our new class object of new_account
new_account.deposit(100)
new_account.display_balance()
new_account.withdraw(25)
new_account.display_balance()