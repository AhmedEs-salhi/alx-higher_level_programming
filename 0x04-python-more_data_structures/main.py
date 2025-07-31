#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_dictionary = {i: a_dictionary[i] for i in a_dictionary if a_dictionary != value}
    return a_dictionary

a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
new_dict = complex_delete(a_dictionary, 'C')
print(new_dict)
print(a_dictionary)
