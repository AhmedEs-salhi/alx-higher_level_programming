#!/usr/bin/python3
def add_tuple(t=(), u=()):
    if len(t) > 0:
        a = t[0]
    else:
        a = 0
    if len(t) > 1:
        b = t[1]
    else:
        b = 0
    if len(u) > 0:
        c = u[0]
    else:
        c = 0
    if len(u) > 1:
        d = u[1]
    else:
        d = 0
    return (a + c, b + d)
