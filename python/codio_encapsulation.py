'''
Notes:
_AttributeName is the convention for private (but it is still technically public)
__AttributeName can give appearance of private
-> python does not have true private
-> __ used for name mangling (avoid name collision for inheritance)
-> __AttributeName renamed by interpreter to _ClassName__AttrbuteName
-> use getters/setters to get and manipulate these variables @property, @name.setter
'''
# Define the Country class which has attributes for name, capital, population, and 
# continent. Please use the Python convention for making these attributes private.
# You do not need to create any getters or setters; just follow the Python convention for private attributes.
class Country:
    def __init__(self, name, capital, population, continent):
        self._name = name
        self._capital = capital
        self._population = population
        self._continent = continent

if __name__ == "__main__":
    my_country = Country('France', 'Paris', 67081000, 'Europe')
    print(my_country._name, my_country._capital, my_country._population, my_country._continent)


# Define the Artist class which has attributes for name, medium, style, and famous_artwork. Do not use the Python 
# convention to make these attributes.
# You do not need to create any getters or setters; do not follow the Python convention for private attributes.
class Artist:
    def __init__(self, name, medium, style, famous_artwork):
        self.__name = name
        self.__medium = medium
        self.__style = style
        self.__famous_artwork = famous_artwork

if __name__ == "__main__":
    my_artist = Artist('Bill Watterson', 'ink and paper', 'cartoons', 'Calvin and Hobbes')
    print(my_artist._Artist__name, my_artist._Artist__medium, my_artist._Artist__style, my_artist._Artist__famous_artwork)
    # print(my_artist.__name, my_artist.__medium, my_artist.__style, my_artist.__famous_artwork)


# Define the BankAccount class which has attributes for checking and savings. Use the Python convention to make these 
# attributes private. Create the getters get_checking and get_savings, and create the setters set_checking and set_savings.
# Do not use the property decorator or function; follow the Python convention for private attributes.
class BankAccount:
    def __init__(self):
        self._checking = 0
        self._savings = 0
    
    def get_checking(self):
        return self._checking
    
    def get_savings(self):
        return self._savings
    
    def set_checking(self, amount):
        self._checking = amount
    
    def set_savings(self, amount):
        self._savings = amount


# Define the Dancer class which has attributes for name, nationality, and style. Use the Python convention to make these 
# attributes private. Create the getters and setters using the property function.
# Use the property function; follow the Python convention for private attributes.
class Dancer:
  def __init__(self, name, nationality, style):
    self._name = name
    self._nationality = nationality
    self._style = style
    
  def get_name(self):
    return self._name
  
  def set_name(self, new_name):
    self._name = new_name
    
  def get_nationality(self):
    return self._nationality
  
  def set_nationality(self, new_nat):
    self._nationality = new_nat
    
  def get_style(self):
    return self._style
  
  def set_style(self, new_style):
    self._style = new_style
    
  name = property(get_name, set_name)
  nationality = property(get_nationality, set_nationality)
  style = property(get_style, set_style)
        