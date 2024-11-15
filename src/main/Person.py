from json import JSONEncoder, JSONDecoder
import json
import ast

class Person:
    def __init__(self, first_name : list[str], last_name : str, age : int):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__influenced = []
        self.__followed = []
    
    def celebrate_birthday(self):
        self.__age += 1
    
    def get_age(self):
        return self.__age
    
    def get_main_name(self):
        return self.__first_name[0]
    
    def get_first_name(self):
        return self.__first_name.copy()
    
    def get_last_name(self):
        return self.__last_name
    
    def get_influenced(self):
        return self.__influenced.copy()
    
    def get_followed(self):
        return self.__followed.copy()
    
    def follow(self, someone : 'Person'):
        string_person = str(someone)
        if string_person not in self.__followed:
            self.__followed.append(string_person)

    def influence(self, someone : 'Person'):
        string_person = str(someone)
        if string_person not in self.__influenced:
            self.__influenced.append(string_person)
    
    def influence_len(self):
        return len(self.__influenced)

    def stop_following(self, someone : 'Person'):
        self.__followed.remove(str(someone))
    
    def stop_influencing(self, someone : 'Person'):
        self.__influenced.remove(str(someone))
    
    def set_followed(self, l):
        self.__followed = l.copy()
    
    def set_influenced(self, l):
        self.__influenced = l.copy()
    
    def __str__(self):
        return '/'.join(self.__first_name) + '-' + self.__last_name + '-' + str(self.__age)

    def __eq__(self, other):
        if str(self) == str(other):   
            return True
        return False
    
    def change_last_name(self, new_last_name : str):
        self.__last_name = new_last_name
    
class PersonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class PersonDecoder(JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dict):
        person = Person(dict['_Person__first_name'], dict['_Person__last_name'], dict['_Person__age'])
        person.set_followed(ast.literal_eval(str(dict['_Person__followed'])))
        person.set_influenced(ast.literal_eval(str(dict['_Person__influenced'])))
        return person