# Define the class PracticeClass. This class should not have a constructor or any attributes (instance variables). 
# Test your code with the TRY IT button below before submitting your work.
class PracticeClass:
    pass


# Define the class Cat. The class should have a constructor but without any parameters. The constructor will generate the following attributes.
# breed - "american shorthair"
# color - "black"
# name - "kiwi"
class Cat:
    def __init__(self):
        self.breed = "american shorthair"
        self.color = "black"
        self.name = "kiwi"

if __name__ == "__main__":
    mycat = Cat()       
    print(f"My cat is an {mycat.color} {mycat.breed}. She is named {mycat.name}.")


# Define the class SuperHero. The class should have a constructor that accepts the following parameters (in this order):
# name- String with the name of the super hero, e.g. "Spider-Man"
# secret_identity - String with the true name of the hero, e.g. "Peter Parker"
# powers - A list of strings with each element representing a power, e.g. ["superhuman strength", "superhuman speed", "superhuman reflexes", "superhuman durability", "healing factor", "spider-sense alert", "heightened senses", "wallcrawling"]
class SuperHero:
    def __init__(self, name, secret_identity, powers):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers

if __name__ == "__main__":
    superman = SuperHero("Superman", "Clark", ["flight", "laser eyes", "super strenght", "x-ray vision"])
    print(superman.name, superman.secret_identity, superman.powers)


# Define the class Observation which will help record observational data from a scientific outpost in Antarctica. The class should have a constructor that accepts parameters for date, temperature, elevation, precipitation, and penguins. 
# Since Antarctica is a desert, precipitation should default to 0.
# date- String with the date of the observation, e.g. "October 26, 2019"
# temperature - Float with the temperature in Celsius, e.g. -47
# elevation - Float with elevation in meters, e.g. 329.4
# penguins - Integer representing the number of penguins observed, e.g. 3
# precipitation- Float with precipitation in centimeters, e.g. 0.7
import copy

class Observation:
    def __init__(self, date, temperature, elevation, penguins, precipitation = 0):
        self.date = date
        self.temperature = temperature
        self.elevation = elevation
        self.penguins = penguins
        self.precipitation = precipitation

if __name__ == "__main__":
    today = Observation("October 25, 2019", -47, elevation = 329.4, penguins = 3)
    tomorrow = copy.deepcopy(today)
    tomorrow.date = "October 26, 2019"
    tomorrow.precipitation = 0.7
    print(today.date, today.temperature, today.elevation, today.penguins, today.precipitation)
    print(tomorrow.date, tomorrow.temperature, tomorrow.elevation, tomorrow.penguins, tomorrow.precipitation)


# Define the class BigCat which will help record information on the animals in the Panthera genus (tiger, lion, jaguar, leopard, and snow leopard). 
# Since all animals are in the same genus, the object should have the class attribute genus with the value panthera. The constructor should accept the following parameters (in this order):
# species- String with the species of the animal, e.g. "tigris"
# common_name - String with the common name of the animal, e.g. "tiger"
# habitat - List of strings with location of the animal, e.g. ["asia"]
class BigCat:
    genus = "panthera"
    def __init__(self, species, common_name, habitat):
        self.species = species
        self.common_name = common_name
        self.habitat = habitat

if __name__ == "__main__":
    tiger = BigCat("tigris", "tiger", ["asia"])
    print(tiger.genus, tiger.species, tiger.common_name, tiger.habitat)