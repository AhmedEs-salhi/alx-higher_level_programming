#!/usr/bin/python3
""" This is the module documentation"""
import json


class Base:
    """ This is the class documentation """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ This is to_json_string method documentation """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return '[]'

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = '{}.json'.format(cls.__name__)
        list_dictionary = [obj.to_json_string(obj.to_dictionary()) for obj in list_objs]

        with open(file_name, "w", encoding="utf-8") as json_file:
            if type(list_objs) is None:
                json.dump([], json_file)
            else:
                json.dump(list_dictionary, json_file)
