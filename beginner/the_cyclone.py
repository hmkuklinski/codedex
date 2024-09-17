#codedex project- determining whether an individual is tall enough and has enough credits for a ride!

height= int(input("Enter your height in cm: "))
credits=int(input("How many credits do you have?: "))
minHeight=70
creditsRequired=2

if height>=minHeight and credits>=creditsRequired:
  print("Enjoy the ride!")
elif height!=minHeight and credits >=creditsRequired:
  print ("You are not tall enough to ride.")
elif height>=minHeight and credits<creditsRequired:
  print ("You don't have enough credits.")
else:
  print("You are not tall enough and do not have enough credits.")