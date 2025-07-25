'''
Notes:
Method resolution order (.mro()) by depth first, left to right (C# linearization)
-> preserve order of base classes
Extention, Overriding, Multiple Inheritance
'''
# Use the CelestialBody class to the left as the parent class. Create the Satellite and Planet classes, 
# both of which are children of CelestialBody. Using the super() keyword to extend the __init__ method 
# of the parent class, add the attribute host_planet to the Satellite class and add the attribute host_star 
# to the Planet class.
class CelestialBody:
    def __init__(self, size, mass, composition, name):
        self.size = size
        self.mass = mass
        self.composition = composition
        self.name = name

class Satellite(CelestialBody):
    def __init__(self, size, mass, composition, name, host_planet):
        super().__init__(size, mass, composition, name)
        self.host_planet = host_planet

class Planet(CelestialBody):
    def __init__(self, size, mass, composition, name, host_star):
        super().__init__(size, mass, composition, name)
        self.host_star = host_star