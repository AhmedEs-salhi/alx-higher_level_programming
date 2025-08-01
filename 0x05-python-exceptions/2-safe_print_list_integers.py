#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0
    temp_x = x
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
        except (TypeError, ValueError):
            continue
        else:
            if temp_x == 0:
                print()
                return nb_print
            temp_x -= 1
            nb_print += 1
    print()
    return nb_print
