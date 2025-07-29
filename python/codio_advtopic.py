'''
Importing Modules - contains classes/functions
List of Objects - can also read CSV file
-> allows iteration through list for multiple objects
Composition - make a functional whoel out of smaller parts
-> create component class and put in composite class
-> i.e. engine object (class) as an instance attribute for car object
-> one way street (composite can acess component but not other way)
-> inheritance extention and composition can do the same thing (choose by "is a" or "has a")
__str__ method makes human-readable string representation of user defined object
-> normally only class and memory location printed
-> print statement automatically calls
__repr__ method - information useful for developer
-> use print(rep(obj)) otherwise will default to __str__
-> usually one line of code (i.e: in __repr__ method, return f'Dog({self.name})
-> __str__ default calls __repr__, which default return class name and object location
'''
# Write a script that imports the Phone and Laptop classes. These classes are found in the tech module. 
# Your script must import the classes as follows:
# import tech
# Instantiate an instance of the Phone class and call it my_phone. It should have the name "Pixel 5", the 
# color "sage", and 128 gigabytes of storage. Important, all numbers passed to the constructor should be integers.
# Instantiate an instance of the Laptop class and call it my_laptop. It should have the name "MacBook Pro", 
# a size of 15 inches, and 256 gigabytes of storage. Important, all numbers passed to the constructor should be integers.
import tech

my_phone = tech.Phone(name = "Pixel 5", color = "sage", storage = 128)
my_laptop = tech.Laptop(name = "MacBook Pro", size = 15, storage = 256)


# You have been given the class Band. Extend the class such that it will produce specific output when using the print and repr.
class Band:
    def __init__(self, name, genre, members):
        self.name = name
        self.genre = genre
        self.members = members
    
    def __str__(self):
        return f"{self.name} is a {self.genre} band."

    def __repr__(self):
        return f"Band({self.name}, {self.genre}, {self.members})"

if __name__ == "__main__":
    dead = Band('The Grateful Dead', 'rock\'n roll', ['Jerry', 'Bob', 'Mickey', 'Bill', 'Phil', 'Pigpen'])
    print(dead)
    print(repr(dead))


# Create the Dog class with attributes for name and breed. Then create a list called dogs that contains five Dog objects according to the following table:
# Position	  Name	  Breed
# 1	Marceline German  Shepherd
# 2	Cajun	  Belgian Malinois
# 3	Daisy	  Border  Collie
# 4	Rocky	  Golden  Retriever
# 5	Bella	  Irish   Setter
# Verify that the name and breed of the dogs in the list match the order of the table. In addition, the auto-grader expects the list to be named dogs.
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
dogs = []
dogs.append(Dog("Marceline", "German Shepherd"))
dogs.append(Dog("Cajun", "Belgian Malinois"))
dogs.append(Dog("Daisy", "Border Collie"))
dogs.append(Dog("Rocky", "Golden Retriever"))
dogs.append(Dog("Bella", "Irish Setter"))
print(dogs)


# You are given code for the Library class (in its own file). This is a composite class. You are going to create 
# the Book class (the component class) in book.py file. Look over the Library class carefully to determine what 
# attributes are needed for the Book class. In addition, the table of output contains a hint as to what method the Book class needs.
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
    
    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.genre})"


# You are going to write a program that simulates an online shopping cart. Create the composite class ShoppingCart in 
# the shopping_cart.py file, and create the component class Item in the item.py file. The tables below indicate which 
# attributes and methods your classes will need to create.
# The Shopping Cart Class
# Important, the ShoppingCart class should initialize the attributes to either a 0 or an empty list. Your ShoppingCart class should have the following attributes:
# Attribute	Explanation
# items	List of Item elements
# total	Total value of all of the items in the shopping cart
# It should also have the following methods:
# Method	Explanation
# __init__	The constructor should not take have any arguments
# add_item	Add an item to the shopping cart and then calls the calculate_total method
# calculate_total	Assigns the total value of the shopping cart to the total attribute
# get_total	Returns the total value of the shopping cart
# get_num_items	Returns the number of different items in the shopping cart
# get_items	Returns a list of all of the items in the cart
# __str__	Returns a human-readable string; see the Expected Output section for the format
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0
    
    def calculate_total(self):
        self.items[-1].calculate_subtotal()
        self.total += self.items[-1].get_subtotal()

    def add_item(self, item):
        self.items.append(item)
        self.calculate_total()
    
    def get_total(self):
        return self.total
    
    def get_num_items(self):
        return len(self.items)
    
    def get_items(self):
        return self.items
    
    def __str__(self):
        return f"The cart has {self.get_num_items()} items for a total of ${self.total}"

# The Item Class
# Important, the subtotal attribute is not passed to the constructor. Initialize this attribute with a 0. Your Item class should have the following attributes:
# Attribute	Explanation
# name	Name of the item
# price	How much the item costs
# quantity	How many items you have
# subtotal	Value of all of the items
# It should also have the following methods:
# Method	Explanation
# __init__	The order of the parameters should be name, price, and then quantity
# calculate_subtotal	Assigns the total value of the items to the subtotal attribute
# get_subtotal	Returns the subtotal attribute
# __repr__	Returns a precise object definition; see the Expected Output section for the format
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.subtotal = 0
    
    def calculate_subtotal(self):
        self.subtotal = self.price * self.quantity
    
    def get_subtotal(self):
        return self.subtotal

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity}, {self.subtotal})"
'''
Given Solution:
class ShoppingCart:
  def __init__(self):
    self.items = []
    self.total = 0
    
  def add_item(self, item):
    self.items.append(item)
    self.calculate_total()
    
  def calculate_total(self):
    self.total = 0
    for item in self.items:
      item.calculate_subtotal()
      self.total += item.get_subtotal()
      
  def get_total(self):
    return self.total
  
  def get_num_items(self):
    return len(self.items)
  
  def get_items(self):
    return self.items
  
  def __str__(self):
    return f'The cart has {self.get_num_items()} items for a total of ${self.total}'

class Item:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity
    self.subtotal = 0
    
  def calculate_subtotal(self):
    self.subtotal = self.quantity * self.price
    
  def get_subtotal(self):
    return self.subtotal
  
  def __repr__(self):
    return f'Item({self.name}, {self.price}, {self.quantity}, {self.subtotal})'
'''