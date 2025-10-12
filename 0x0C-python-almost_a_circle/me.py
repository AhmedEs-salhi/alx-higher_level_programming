#!/usr/bin/python3

with open("Rectangle.json", "r") as file:
    print(file.seek(1))
    character = ''
    line = ''
    while character != ']':
        character = file.read(1)
        print(character, end="")
        #line += character
        if character == '}':
            file.seek(file.tell() + 2)
