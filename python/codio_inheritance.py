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


# Use the parent class Book to help you solve this problem. Create the child class BlogPost and override the constructor so that the child class has the following attributes:
# website - a string that represents the website hosting the blog post
# title - a string that represents the title of the blog post
# author - a string that represents the author of the blog post
# word_count - an integer that represents the number of words in the blog post
# genre - a string that represents the genre of the blog post
# page_views - an integer that represents the page views for the blog post
class Book:
  def __init__(self, title, author, genre):
    self.title = title
    self.author = author
    self.genre = genre

class BlogPost(Book):
    def __init__(self, website, title, author, word_count, genre, page_views):
        super().__init__(title, author, genre)
        self.website = website
        self.word_count = word_count
        self.page_views = page_views


# Create the class Child such that the following criteria are met:
# Child is a subclass of Parent1 and Parent2
# Override identify so that it returns “This method is called from Child”
# Create the method identify2 that invokes the identify method from Parent2. This must be done using the super() keyword.