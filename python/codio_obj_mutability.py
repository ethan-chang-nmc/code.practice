# The code below creates the CelestialBody class as well as the function compared_to_earth. Transform the compared_to_earth 
# function so that it becomes an instance method of the CelestialBody class.
class CelestialBody:
    """Represents a celestial body"""
    def __init__(self, name, diameter, distance, moons):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.moons = moons
    
    def compared_to_earth(self):
        """Determines the size of a celestial
        body relative to Earth using diameter"""
        earth = 12756.3
        relative_size = self.diameter / earth
        return relative_size
    
planet = CelestialBody("Jupiter", 142984, 778360000, 79)
print(planet.compared_to_earth())


# Using the same CelestialBody class, write a static method closer_to_sun that compares two CelectialBody objects and returns 
# the name of the object that is closes to the sun.
class CelestialBody:
    """Represents a celestial body"""
    def __init__(self, name, diameter, distance, moons):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.moons = moons
        
    @staticmethod
    def closer_to_sun(cb1, cb2):
        if cb1.distance < cb2.distance:
            return cb1.name
        else:
            return cb2.name

mercury = CelestialBody("Mercury", 4879.4, 57909000, 0)
venus = CelestialBody("Venus", 12103.6, 108160000, 0)

if __name__ == "__main__":
    print (CelestialBody.closer_to_sun(mercury, venus))


# Using the same CelestialBody class, create a factory method called make_earth. This method returns a CelestialBody object 
# for planet Earth. Earth is 149,600,000 km from the Sun, has a diameter of 12,756.3 km, and has one moon.
class CelestialBody:
    """Respresents a celetstial body"""
    def __init__(self, name, diameter, distance, moons):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.moons = moons
    
    @classmethod
    def make_earth(cls):
        return cls("Earth", 12756.3, 149600000, 1)
    
if __name__ == "__main__":
    planet = CelestialBody.make_earth()
    print(planet.name, planet.diameter, planet.distance, planet.moons)


# Create the following methods for the Library class:
# add_books - takes a list of book titles (strings) and adds each title to the list of available books
# borrow_book - takes a book title (string) and moves it from the available list to the list of books on loan
# return_book - takes a book title (string) and moves it from the list of books on loan to the list of available books
class Library:
    """List of available books and list of books on loan"""
    def __init__(self):
        self.available = []
        self.on_loan = []
    
    def add_books(self, input):
        for book in input:
            self.available.append(book)
    
    def borrow_book(self, title):
        self.available.remove(title)
        self.on_loan.append(title)
    
    def return_book(self, title):
        self.on_loan.remove(title)
        self.available.append(title)

if __name__ == "__main__":
    my_library = Library()
    my_library.add_books(["Four Seasons", "Say Nothing", "Milkman", "Harry Potter and the Order of the Phoenix"])
    print(my_library.available)
    my_library.borrow_book("Harry Potter and the Order of the Phoenix")
    my_library.borrow_book("Say Nothing")
    print(my_library.available)
    print(my_library.on_loan)
    my_library.return_book("Say Nothing")
    print(my_library.available)
    print(my_library.on_loan)
'''
self note: dont forget to add docstring to method!
'''


# Create the following methods for the Subway class:
# board - Accepts an integer that represents the number of passengers boarding the subway.
# disembark - Accepts an integer that represents the number of passengers exiting the subway. There cannot be a negative number of passengers on a subway. The fewest number of passengers on a subway is 0.
# advance - Moves the subway to the next stop. If self.direction is "south" the subway moves from Alewife to Kendall. If self.direction is "north" the subway moves from Kendall to Alewife. When the subway has reached its final stop, self.direction should change.
# distance - Accepts a string that represents a stop and returns the number of stops between the subway and the desired stop. The distance should be a positive number.
# change_fare - Accepts a float and changes the fare for all instances of the Subway class.
# calculate_fares - Calculates the fare for each passenger boarding the subway and adds it to total_fares.
class Subway:
    fare = 2.4
    def __init__(self):
        self.stops = ["Alewife", "Davis", "Porter", "Harvard", "Central", "Kendall"]
        self.current_stop= "Alewife"
        self.direction = "south"
        self.passengers = 0
        self.total_fares = 0

    def calculate_fares(self, board):
        "calculates fares of people boarding"
        self.total_fares += board * self.fare

    def board(self, people):
        "boards people"
        self.passengers += people
        self.calculate_fares(people)
    
    def disembark(self, people):
        "deboards people, prevents going below 0"
        if people > self.passengers:
            self.passengers = 0
        else:
            self.passengers -= people
    
    def advance(self):
        "moves subway to next stop and changes directions when at ends"
        if (self.direction == "north") and (self.stops.index(self.current_stop) == 0):
            self.direction = "south"
        elif (self.direction == "south") and (self.stops.index(self.current_stop) == len(self.stops) - 1):
            self.direction = "north"
        else:
            pass
        if self.direction == "south":
            self.current_stop = self.stops[self.stops.index(self.current_stop) + 1]
        else:
            self.current_stop = self.stops[self.stops.index(self.current_stop) - 1]
    
    def distance (self, destination):
        "calculates distance between current and desired stop"
        dist = self.stops.index(self.current_stop) - self.stops.index(destination)
        if dist < 0:
            dist *= -1
        return dist
    
    @classmethod
    def change_fare(cls, new_fare):
        "changes the fare for all instances of Subway class"
        cls.fare = new_fare
'''
Given solution: Forgot to check for negative passengers
def disembark(self, passengers_leaving):
    """Subtracts the number of people exiting the subway"""
    if passengers_leaving > self.passengers:
      self.passengers = 0
    else:
      self.passengers -= passengers_leaving

'''