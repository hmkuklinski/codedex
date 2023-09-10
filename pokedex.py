#pokedex

class Pokemon:
	#defines the values of object characteristics of the Pokemon class
	def __init__(self, entry, name, type, description, is_caught, level):
		self.entry = entry
		self.name = name
		self.type = type
		self.description = description
		self.is_caught= is_caught
		self.level = level
	
	#announces the arrival of the pokemon by stating their name, level, type, and a short description
	def stats(self):
		print("\n" + self.name + " has entered the arena!")
		print(self.name + " is a level " + str(self.level) + " " + self.type + " type and is " + self.description)
		if self.is_caught == True:
			print(self.name + " has been captured!")
        else:
            print(self.name + " has yet to be captured!")
	
	#announces that the pokemon is speaking!
	def speak(self):
		print (self.name + " made a sound!")

#creation of the Pokemon in our Pokemon class!
#class requirements =Pokemon(entry, name, type, description, is_caught, level)

pikachu= Pokemon(1, "Pikachu", "lightning", "Ash's loyal sidekick", False , 30)
apom= Pokemon (2, "Apom", "strength", "a purple monkey with a hand as a tail", False ,27)
charmander= Pokemon(3, "Charmander", "fire", "a orange salamander with a love for the heat!", False, 29)

#calling the pokemon to battle!
pikachu.stats()
pikachu.speak()

apom.stats()
apom.speak()

charmander.stats()
charmander.speak()