#fortune cookie- function that randomly generates what the fortune cookie message will be and prints it out!
import random

#our list of possible fortune cookie messages:
messages=["Don't pursue happiness- create it.", 
           "All things are difficult before they are easy", 
           "The early bird gets the worm, but the second mouse gets the cheese.", 
           "If you eat something and nobody sees you eat it, it has no calories.", 
           "Someone in your life needs a letter from you.", 
           "Don't just think. Act!", 
           "Your heart will skip a beat", 
           "The fortune you search for is in another cookie.", 
           "Help! I'm being held prisoner in a Chinese bakery!"]

#define the function called fortune
def fortune():
  selected_message= random.randint(1,10) #recall the second number is not inclusive
  if selected_message==1:
    message=messages[0]
  elif selected_message==2:
    message=messages[1]
  elif selected_message==3:
    message=messages[2]
  elif selected_message==4:
    message=messages[3]
  elif selected_message==5:
    message=messages[4]
  elif selected_message==6:
    message=messages[5]
  elif selected_message==7:
    message=messages[6]
  elif selected_message==8:
    message=messages[7]
  elif selected_message==9:
    message=messages[8]
  else:
    message="error"

  print(message)

#calling the fortune() function
fortune()
fortune()
fortune()