#!/usr/bin/python3

from models.rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, id, size, x, y):
        super().__init__(id, size, size, x, y)

    def update(self, *args):
        args_len = len(args)
        attr_dict = self.__dict__
        if args_len < 2:
            attr_dict["id"] = args[0]
        else:
            attr_dict["_Rectangle__width"], attr_dict["_Rectangle__height"] = args[1]
            index = 2
            
    
    def __str__(self):
        return "{}".format(self.__dict__)

s = Square(1, 2, 3, 4)
print(s)
s.update(1024)
print(s)
