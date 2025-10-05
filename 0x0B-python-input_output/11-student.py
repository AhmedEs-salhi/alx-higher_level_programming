#!/usr/bin/python3
""" This is the module documentation"""


class Student:
    """ This is the class documentation """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        json_dict = {}

        if type(attr) is not list:
            return self.__dict__

        for key in attr:
            if key in self.__dict__:
                json_dict[key] = self.__dict__[key]
        return json_dict

    def reload_from_json(self, json):
        class_dict = self.__dict__
        for key in class_dict:
            if key in json:
                class_dict[key] = json[key]
