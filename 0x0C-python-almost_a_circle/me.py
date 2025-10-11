class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def update(self, *args):
        attr_dict = self.__dict__
    
        index = 0
        for key in attr_dict:
            try:
                attr_dict[key] = args[index]
            except IndexError:
                break
            else:
                index += 1

    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.__dict__)


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
    
    def update(self, *args):
        arguments = list(args)
        for i in range(len(args)):
            arguments[i] = self.width
        super().update(tuple(arguments))

r = Rectangle(1024, 98)
s = Square(512)
print(r)
print(s)
r.update(1337)
s.update(100, 23)
print(r)
print(s)
