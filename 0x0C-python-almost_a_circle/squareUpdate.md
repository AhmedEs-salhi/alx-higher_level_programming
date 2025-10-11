# Square update:
## Function Prototype
`def update(self, *args, **kwargs)`

I could divide this function into two functions with two prototypes: 

`def update(self, *args)` &  `def update(self, **kwargs)`

Then I could combine them all together.

## First Problem `def update(self, *args)`

The problem about this task is that we have a gap between the `update()` function arguments (4 arguments) 
and the `Square` class attributes (5 arguments)

```python
from models.rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, id, size, x, y):
        super().__init__(id, size, size, x, y)
    def __str__(self):
        return self.__dict__
s = Square(1, 2, 3, 4)
print(s)
```
This code snippet will output:
```commandline
~$ python3 test.py
~$ {'_Rectangle__width': 1, '_Rectangle__height': 2, '_Rectangle__x': 2, '_Rectangle__y': 3, 'id': 4}
```
### Constructing the solution

So the `size` variable will either have the `width` value or the `height` value
then the `*args[2]` will be affected to the `x` variable while the last one is for `y` variable

But there is some cases where `len(args) < 2`, here we could execute a different procedure depend on the length of the `args` variable

In my point of view I will compare the `len(args)` every time to know exactly what I would do.

### Comparing the `len(args)`

First of all the `len(args)` should not be 0 which means `args` should not be empty

- if `len(args) < 2`: Only assign `args[0]` to the `id` variable
```python
def update(self, *args):
    args_length = len(args)
    attributes_dict = self.__dict__
    if args_length < 2:
        attributes_dict["id"] = args[0]
```
- Otherwise, things will get a little bit complicated but, let's figure things out. 
    
    Let's loop along the `self.__dict__` dictionary putting

