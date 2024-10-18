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
        self.__followed.append(someone)

    def influence(self, someone : 'Person'):
        self.__influenced.append(someone)
       

    def stop_following(self, someone : 'Person'):
        self.__followed.remove(someone)
    
    def stop_influencing(self, someone : 'Person'):
        self.__influenced.remove(someone)
    
    def __eq__(self, other):
        if self is other:   
            return True
        return False
    
    def __dir__(self):
        dictionnary = {
            "first_name" : self.__first_name,
            "last_nale" : self.__last_name,
            "age" : self.__age,
            "influenced" : self.__influenced,
            "followed" : self.__followed
        }
    
    def change_last_name(self, new_last_name : str):
        self.__last_name = new_last_name