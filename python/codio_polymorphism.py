'''
Notes:
Polymorphism - single interface is applicable with different types (i.e. + operator)
-> method overriding is a form
Method Overloading - single method name that can take different sets of parameters
-> also example of polymorphism
-> when two methods have same name, python recognizes the last method (ignores rest)
-> declare method with optional parameters set to None
-> ex: print(int.__mul__(num1, num2)) for *, (int.__truediv__(num1, num2))
Operator overloading - __operation__ (dunder/magic methods)
-> applies to all inssnes suitibility by what it does, not by type
-> ex: The print_hit function does not care if the object is has the type BaseballPlayer 
or Song. It only cares if the object has a hit method. Duck typing is an example of polymorphism 
because, in this case, a single function works with objects of different types.
-> define function (i.e. print_function) taking obj as parameter and executing wanted method
-> check for existence of method (try except AttributeError)
'''
# Use the Lottery class to the left as the parent class. Create the PowerBall class as a child class of 
# Lottery. Override the shuffle method so that it returns a list of six random integers between 1 and 99.
import random

class Lottery:
    def shuffle(self):
        results = []
        for i in range(5):
            results.append(random.randint(1, 20))
        return results

class PowerBall(Lottery):
    def shuffle(self):
        results = []
        for i in range(6):
            results.append(random.randint(1,99))
        return results

if __name__ == "__main__":
    output = PowerBall()
    print(output.shuffle())


# Complete the Airplane and Train classes so that when an instance of each is passed to the passengers function, 
# they will return the total number of passengers on board.
class Airplane:
    def __init__(self, first_class, business_class, coach):
        self.first_class = first_class
        self.business_class = business_class
        self.coach = coach
    
    def total(self):
        total_p = self.first_class + self.business_class + self.coach # can just return this instead of dummy var
        return total_p

class Train:
    def __init__(self, car1, car2, car3, car4, car5):
        self.car1 = car1
        self.car2 = car2
        self.car3 = car3
        self.car4 = car4
        self.car5 = car5

    def total(self):
        total_p = self.car1 + self.car2 + self.car3 + self.car4 + self.car5 # can just return this instead of dummy var
        return total_p
  
def passengers(obj):
    print(f'There are {obj.total()} passengers on board.')

if __name__ == "__main__":
    my_plane = Airplane()
    my_train = Train()
    passengers(my_plane)
    passengers(my_train)