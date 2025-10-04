#!/usr/bin/python3

class MyClass:
    def __init__(self, name, age):
        self.__name = name
        self.age = age
        self.isAdult = "is adult" if self.age > 18 else "is not adult"

    def __str__(self):
        return "[{}] {} has {}, and {}".format(
            self.__class__.__name__,
            self.__name,
            self.age,
            self.isAdult
        )

me = MyClass("Ahmed", 21)
print(me.__dict__)