#!/usr/bin/python3

def append_after(filename, search_string="", new_string=""):
    with open(filename, "a+") as file:
        for line in file:
            print(line)
            #file.seek(len(line))
            #if search_string in line:
                #file.writelines(new_string)
