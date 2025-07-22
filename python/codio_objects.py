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