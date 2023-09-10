#Solar System
from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)
r=0 #radius of the planet

if random_planet=="Mercury":
  r=2440
elif random_planet=="Venus":
  r=6052
elif random_planet=="Earth":
  r=6371
elif random_planet=="Mars":
  r=3390
elif random_planet=="Saturn":
  r=58232
else:
  print("Oops! An error occurred")


area=4*pi*(r**2)
answer= round(area, 1)
print(f"The planet {random_planet} has an area of {answer}")