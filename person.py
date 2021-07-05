  
class Person:
    def __init__(self, name, age, city, address, phone_number):
        self._name = name
        self._age = age
        self._city = city
        self._address = address
        self._phone_number = phone_number

    @property
    def city(self, _default = None):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def phone_number(self, _default=None):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
   
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
        return f'Name: {self._name}\nAge: {self._age}\nAddress: {self._address}\nCity: {self._city}\nPhone: {self._phone_number}'