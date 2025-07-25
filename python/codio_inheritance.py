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


# Use the parent class Book to help you solve this problem. Create the child class BlogPost and override 
# the constructor so that the child class has the following attributes:
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
# Create the method identify2 that invokes the identify method from Parent2. This must be done using the 
# super() keyword.
class Parent1:
    def identify(self):
       return "This method is called from Parent1"
    
class Parent2:
    def identify(self):
        return "This method is called from Parent2"
  
class Child(Parent2, Parent1):
    def identify(self):
        return "This method is called from Child"
    
    def identify2(self):
        return super().identify()

if __name__ == "__main__":
    child_object = Child()
    print(child_object.identify())
    print(child_object.identify2())


# The code to the left creates a class called Bank. This class has a branch name, the number of customers, and 
# a list of the amount of money in each customer’s bank account. The method branch_total takes the list of customer 
# money and returns the total amount of money held by the bank.
# Create the class RegionalBank as a child of the Bank class. This class has a name, the number of customers in the 
# region, and a 2D list of all of the money in the bank accounts for each branch. Extend the RegionalBank class by 
# adding the method regional_total which returns the total amount of money kept in all of the banks in the region.
# Instantiate an object from the RegionalBank class and use the variable accounts as the 2D list of bank account. 
# Print out the result from regional_total.
import sys
strings = [l.split(",") for l in sys.argv[1].split("*")]
accounts = [[int(n) for n in s] for s in strings]

class Bank:
    def __init__(self, name, customers, accounts):
        self.name = name
        self.customers = customers
        self.accounts = accounts
    
    def branch_total(self, accounts):
        total = 0
        for account in accounts:
            total += account
        return total

class RegionalBank(Bank):
    def __init__(self, name, customers, accounts):
        super().__init__(name, customers, accounts)
    
    def regional_total(self):
        grand_total = 0
        for bank in self.accounts:
            grand_total += self.branch_total(bank)
        return grand_total
    
if __name__ == "__main__":
    here_bank = RegionalBank("here", 3, accounts)
    print(here_bank.regional_total())


# Use the parent classes to the left to help you solve this problem. The first parent is the Person class with some 
# very generic information. The second class, CardHolder, is the class for a credit card holder. Create the child class 
# PlatinumClient. This class inherits all of the attributes of both parent classes. In addition, the child class has the 
# attributes cash_back and rewards. cash_back should be set to 0.02 and rewards should be set to 0. Override the 
# process_sale method so that 2% of each sale is added to rewards.
class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def get_info(self):
        return f"{self.name} lives at {self.address}."
  
class CardHolder:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0
        self.credit_limit = 5000
    
    def process_sale(self, price):
        self.balance += price
    
    def make_payment(self, amount):
        self.balance -= amount
    
class PlatinumClient(Person, CardHolder):
    cash_back = 0.02
    def __init__(self, name, address, account_number):
        Person.__init__(self, name, address)
        CardHolder.__init__(self, account_number)
        self.rewards = 0
    
    def process_sale(self, price):
        CardHolder.process_sale(self, price)
        self.rewards += int(self.cash_back * price)

if __name__ == "__main__":
    platinum = PlatinumClient("Sarah", "101 Main Street", 123364)
    platinum.process_sale(100)
    print(platinum.rewards)
    print(platinum.balance)
    platinum.make_payment(50)
    print(platinum.balance)
    print(platinum.get_info())