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