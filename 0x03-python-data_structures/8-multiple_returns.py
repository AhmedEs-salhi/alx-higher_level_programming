#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    if len(sentence) != 0:
        b = sentence[0]
    else:
        b = None
    return a, b
