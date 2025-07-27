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


# Create the class Characters which has the attribute phrases which is a list of strings passed as a parameter. 
# Overload the <, >, and == operators so that you can make comparisons based on the total number of characters in the string.
class Characters:
    def __init__(self, phrases):
        self.phrases = phrases
    
    def total_char(self):
        count = 0
        for word in self.phrases:
            for char in word:
                count += 1
        return count
    
    def __lt__(self, second):
        if self.total_char() < second.total_char():
            return True
        else:
            return False
    
    def __gt__(self, second):
        if self.total_char() > second.total_char():
            return True
        else:
            return False
    
    def __eq__(self, second):
        if self.total_char() == second.total_char():
            return True
        else:
            return False
        
if __name__ == "__main__":
    sample_phrases1 = ['cat in the hat', 'green eggs and ham', 'the lorax']
    sample_phrases2 = ['the taming of the shrew', 'hamlet', 'othello']

    c1 = Characters(sample_phrases1)
    c2 = Characters(sample_phrases2)
    print(c1 > c2) # prints 'True'
    print(c1 < c2) # prints 'False'
    print(c1 == c1) # prints 'True'


# Create the Median that has the method calculate_median that calculates the median of the integers passed to the method. 
# Use method overloading so that this method can accept anywhere from two to five parameters.
class Median:
    def __init__(self):
        pass

    def calculate_median(self, num1, num2, num3 = None, num4 = None, num5 = None): # can use *args but for sake of the problem set each is listed explicitly
        list = [num1, num2, num3, num4, num5]
        final_list = []
        for number in list:
            if number != None:
                final_list.append(number)
        final_list.sort()
        length = len(final_list)
        if length % 2 == 0:
            return (final_list[(length // 2) - 1] + final_list[(length // 2)])/2
        else:
            return final_list[length // 2]
        
if __name__ == "__main__":
    m = Median()
    m.calculate_median(3, 5, 1, 4, 2)
    m.calculate_median(8, 6, 4, 2)
    m.calculate_median(9, 3, 7)
    m.calculate_median(5, 2)
'''
class Median:
  def calculate_median(self, n1, n2, n3=None, n4=None, n5=None):
    if n3 is not None and n4 is not None and n5 is not None:
      numbers = [n1, n2, n3, n4, n5]
    elif n3 is not None and n4 is not None:
      numbers = [n1, n2, n3, n4]
    elif n3 is not None:
      numbers = [n1, n2, n3]
    else:
      numbers = [n1, n2]
    
    numbers.sort()
    median_index = len(numbers) // 2
    if len(numbers) % 2 == 0:
      median = (numbers[median_index] + numbers[median_index - 1]) / 2
    else:
      median = numbers[median_index]
    return median
'''


# The Substitute class reads a text file and replaces every fifth word with the string HELLO.
# Create the class Stars which is a child class of Substitute. Then override the swap_words method so that every third word is replaced by a series of *. If the word has three letters then it should be replaced with ***. The number of * should match the number of characters in the word. Write the new string to self.answer_file.
# Important
# Keep the following things in mind as you write your code. Changes should only be made to the Stars class; do not alter the code for the file variables and the Substitute class.
# The source_file attribute represents the file you will read.
# The answer_file attribute represents the file to which you will write your new text.
# The string_to_list method converts the string (the text file) into a 2D list. Each inner list represents a sentence. The elements of each inner list are the words that make up that sentence.
# The list_to_string method converts the 2D list back into a string.
# When you override the swap_words methods, be sure to start with string_to_list and use list_to_string before writing to the file.
# The text used for this activity are the first four sentences of Jane Austen’s Pride and Prejudice.
source_file = '/home/codio/workspace/code/polymorphism/text_1_exercise5.txt'
answer_file = '/home/codio/workspace/code/polymorphism/answer_exercise5.txt'

class Substitute:
    def __init__(self, source_file, answer_file):
        self.source_file = source_file
        self.answer_file = answer_file
        self.words = None
    
    def string_to_list(self):
        '''Read text file, turn it into a
        2D list of words for each line'''
        words = []
        with open(self.source_file, 'r') as file_object:
            lines = file_object.read().split('\n')
            for line in lines:
                words.append(line.split())
        self.words = words
    
    def list_to_string(self):
        '''Convert 2D list back into a 
        string with newline characters'''
        lines = []
        for line in self.words:
            lines.append(' '.join(line))
        string = '\n'.join(lines)
        self.words = string
  
    def swap_words(self):
        self.string_to_list()
        for line in self.words:
            for i in range(len(line)):
                if (i + 1) % 5 == 0:
                    word = line[i]
                    line[i] = 'HELLO'
        self.list_to_string()

class Stars(Substitute):
    def swap_words(self):
        self.string_to_list()
        for line in self.words:
            for i in range(len(line)):
                if (i + 1) % 3 == 0:
                    word = line[i]
                    line[i] = "*" * len(word)
        self.list_to_string()

        with open(self.answer_file, 'w') as f:
            f.write(self.words)