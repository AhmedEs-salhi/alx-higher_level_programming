#!/usr/bin/python3
class MyClass:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country


me = MyClass("Ahmed", 21, "Morocco")
print(me.__dict__)
me.__dict__["name"] = "Linus"
print(me.__dict__)