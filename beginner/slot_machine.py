#Slot Machine!

import random

#our list of the symbols
symbols= ['🍒',' 🍇', '🍉','7️⃣']

def play():
	
	#randomly selects 3 items from the list
	results= random.choices(symbols, k=3)

	#print out our results in a slot machine style:
	print(f"{results[0]} | {results[1]} | {results[2]}")

	#if all the randomly selected items from the symbols list are 7s
	if results[0]== '7️⃣' and results[1]== '7️⃣' and results[2]=='7️⃣' :
	  print("JACKPOT! 💰")
      
	else:
	  print("Thanks for playing")

playAgain=True

while playAgain==True:
	play()
	
	isValidEntry=False
	
	while isValidEntry==False:
		print("\nWould you like to play again?  ")
		answer=input("Please type Yes or No")
		
		if answer.lower() == "y" or answer.lower() == "yes":
			playAgain=True
			isValidEntry=True
		elif answer.lower() == "n" or answer.lower() == "no":
			playAgain=False
			isValidEntry=True
		else:
			print("Invalid answer. Please try again.")
			isValidEntry=False



