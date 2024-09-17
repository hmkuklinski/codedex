print("BANK OF CODÉDEX")

#prompt the user for the pin
pin = int(input("Enter your PIN: "))

#enter the incorrect pin- will reprompt another pin entry
while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

#enter the correct pin
if pin == 1234:
  print('PIN accepted!')
