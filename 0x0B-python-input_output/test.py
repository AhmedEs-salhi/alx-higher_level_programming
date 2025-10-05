#!/usr/bin/python3
class MyClass:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country


me = MyClass("Ahmed", 21, "Morocco")
print("name" in me.__dict__)