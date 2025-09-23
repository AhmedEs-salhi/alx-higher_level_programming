#!/usr/bin/python3

class Dad:
    def age_validator(self, age):
        if not isinstance(age, int):
            raise TypeError("You should have an integer as an age")
        return age

class Me(Dad):
    def __init__(self, age):
        self.age = self.age_validator(age)


try:
    me = Me(21)
except Exception as err:
    print(err)
else:
    print(me.age)