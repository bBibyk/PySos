class Person:
    def __init__(self, first_name : list[str], last_name : str, age : int):
        self.__first_name__ = first_name
        self.__last_name__ = last_name
        self.__age__ = age
        self.__influence__ = []
        self.__folow__ = []
    
    def celebrate_birthday(self):
        self.__age__ += 1
    
    def get_age(self):
        return self.__age__
    
    def get_main_name(self):
        return self.__first_name__[0]
    
    def get_first_name(self):
        return self.__first_name__.copy()
    
    def get_last_name(self):
        return self.__last_name__
    
