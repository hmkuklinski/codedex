#drive thru 

def welcome():
  print("Hello! Welcome to McDonald\'s! What can I get started for you?")
  print("Here's our menu: ")
  #lists out our menu items in an array
  menu= ["1. 🍔  Cheeseburger", "2. 🍟  Fries", "3.🥤  Soda", "4.🍦  Ice Cream", "5.🍪  Cookie"]
  
  #for loop that goes through each of the values in our array and prints them out:
  for i in range (0,5):
    print(menu[i])

def get_item(item_number):
  if item_number==1:
    return '🍔 Cheeseburger'
  elif item_number==2:
    return '🍟 Fries'
  elif item_number==3:
    return '🥤 Soda'
  elif item_number==4:
    return '🍦 Ice Cream'
  elif item_number==5:
    return '🍪 Cookie'
  else:
    return 'Please make another selection of 1-5.'

#calling the functions
welcome()
item_number=int(input("Please select the number of the item you wish to order: "))
print(get_item(item_number)) #inputs the user's item selection in the get_item function, which returns the menu item "value" and prints it out