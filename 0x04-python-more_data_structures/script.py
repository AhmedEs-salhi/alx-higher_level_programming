#!/usr/bin/python3
def complex_delet(a_dictionary, value):  
    a_dictionary = dict(filter(lambda item: item[1] != 'C', a_dictionary.items()))
    return a_dictionary

a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
print("Before {}".format(a_dictionary))
new_dict = complex_delet(a_dictionary, 'C')
print(new_dict)
print("After {}".format(a_dictionary))
