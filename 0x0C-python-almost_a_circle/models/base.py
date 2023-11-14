#!/usr/bin/python3

"""Defines a base model class"""

import json
import os
import csv


class Base:
    """reperesent the base module"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize class base
        as the new model
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json format of list_dictionaries"""
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string
        representation of list_objs to a file"""

        name = cls.__name__ + '.json'
        with open(name, mode='w') as f:
            if list_obs is None:
                f.write('[]')
            else:
                list_dicts = [ob.to_dictionary() for ob in list_obs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the JSON
        string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance from a 
        dictionary of attributes"""
        if cls.__name__ == 'Rectangle':
            new = cls(1, 1)
        elif cls.__name__ == 'Square':
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of class"""
        name = cls.__name__ + ".json"
        list_dic = []
        list_inst = []

        if os.path.exists(name):
            with open(name, mode='r') as f:
                string = f.read()
                list_dic = cls.from_json_string(string)
                for i in list_dic:
                    list_inst.append(cls.create(**i))
        return list_inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """write the JSON string representation"""
        name = cls.__name__ + '.csv'
        with open(name, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """return a list of class"""
        name = cls.__name__ + '.csv'
        try:
            with open(name, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                dicts_list = csv.DictReader(f, fieldnames=fieldnames)
                dicts_list = [dict([k, int(v)] for k, v in d.items())
                              for d in dicts_list]
                return [cls.create(**d) for d in dicts_list]
        except IOError:
            return []
