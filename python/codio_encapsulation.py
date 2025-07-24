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