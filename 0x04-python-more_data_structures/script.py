#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    return list(map(lambda x: replace if x == search else x, my_list))

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)
