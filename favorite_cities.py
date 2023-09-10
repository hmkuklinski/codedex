# practicing classes- favorite cities


class City:
  def __init__(self,name, country, population, landmarks):
    self.name=name
    self.country=country
    self.population=population
    self.landmarks=landmarks

nyc= City("New York City", "USA", 3000000, ["The Empire State Building", "The Statue of Liberty", "Madison Square Gardens"])

pgh= City("Pittsburgh", "USA", 1000000, ["PNC park", "Heinz Field", "The Pointe"])

#vars allows us to check the stats of the class!
print(vars(nyc))
print(vars(pgh))