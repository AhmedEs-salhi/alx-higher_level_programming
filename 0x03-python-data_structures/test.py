#!/usr/bin/python3
def no_c(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == 'c' or string[i] == 'C':
            continue
        else:
            new_string += string[i]
    return new_string

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
