# Define the class PracticeClass. This class should not have a constructor or any attributes (instance variables). 
# Test your code with the TRY IT button below before submitting your work.
class PracticeClass:
    pass


# Define the class Cat. The class should have a constructor but without any parameters. The constructor will generate the following attributes.
# breed - "american shorthair"
# color - "black"
# name - "kiwi"
# Test your code with print statements and the TRY IT button below before submitting your work.
class Cat:
    def __init__(self):
        self.breed = "american shorthair"
        self.color = "black"
        self.name = "kiwi"

if __name__ == "__main__":
    mycat = Cat()       
    print(f"My cat is an {mycat.color} {mycat.breed}. She is named {mycat.name}.")