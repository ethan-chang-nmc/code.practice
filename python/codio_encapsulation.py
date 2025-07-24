'''
Notes:
_AttributeName is the convention for private (but it is still technically public)
__AttributeName can give appearance of private
-> python does not have true private
-> __ used for name mangling (avoid name collision for inheritance)
-> __AttributeName renamed by interpreter to _ClassName__AttrbuteName
-> use getters/setters to get and manipulate these variables @property, @name.setter
'''