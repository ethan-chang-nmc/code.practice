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
