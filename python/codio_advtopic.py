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
