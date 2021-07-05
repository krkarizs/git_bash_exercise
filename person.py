class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self, _default = None):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self, _default = None):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    def __str__(self):
        return f'Name: {self._name}\nAge: {self._age}'