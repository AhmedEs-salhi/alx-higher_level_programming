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
        with open(file_name, "w", encoding="utf-8") as json_file:
            if list_objs is None:
                json.dump([], json_file)
                return
            list_dictionary = [obj.to_dictionary() for obj in list_objs]
            cls.to_json_string(list_dictionary)
            json.dump(list_dictionary, json_file)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **a_dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1, 0)
        else:
            dummy = cls(1, 0, 0)
        dummy.update(**a_dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        file_name = "{}.json".format(cls.__name__)
        json_list = []

        try:
            with open(file_name, "r", encoding="utf-8") as json_file:
                json_list = json_file.read()
        except FileNotFoundError:
            return []
        else:
            json_list = cls.from_json_string(json_list)
            return [cls.create(**a_dictionary) for a_dictionary in json_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        key_list = ["id", "width", "height", "x", "y"]
        if cls.__name__ == 'Square':
            key_list = ["id", "size", "x", "y"]

        file_name = "{}.csv".format(cls.__name__)
        with open(file_name, "w", encoding="utf-8") as csv_file:
            csv_file.writelines(", ".join(key_list))
            length = len(key_list)
            for obj in list_objs:
                counter = 0
                csv_file.write("\n")
                temp_dict = obj.to_dictionary()
                for key in key_list:
                    csv_file.write("{}".format(temp_dict[key]))
                    if counter < length - 1:
                        csv_file.write(", ")
                        counter += 1

    @classmethod
    def load_from_file_csv(cls):
        file_name = "{}.csv".format(cls.__name__)
        instances_list = []
        with open(file_name, "r", encoding="utf-8") as csv_file:
            header = csv_file.readline().split(", ")
            header[-1] = 'y'
            for line in csv_file:
                data = line.split(", ")
                data = [int(elm) for elm in data]
                new_dict = dict(zip(header, data))
                instances_list.append(cls.create(**new_dict))
        return instances_list
