#!/usr/bin/env python3
inherits_from = __import__("4-inherits_from").inherits_from

a = 1
print(isinstance(a, int), issubclass(int, int))
print(inherits_from(a, object))
