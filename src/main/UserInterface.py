import Person
import json
import os

class UserInterface:
    def __init__(self):
        self.__people_pull = []

    def create_person(self):
        first_name = str(input("First name (if many, seperated by one space): "))
        last_name = str(input("Last name: "))
        age = int(input("Age: "))
        self.__people_pull.append(Person.Person(first_name.split(" "), last_name, age))
    
    def delate_person(self):
        self.__people_pull.remove()
        name = str(input("Main name: "))
        person = self.__find_person(name)
        self.__people_pull.remove(person)

    def __find_person(self, name : str):
        for p in self.__people_pull:
            if p.get_first_name()[0]==name:
                return p

    def create_link(self):
        name1 = str(input("Main name of the follower: "))
        name2 = str(input("Main name of the influencer: "))
        p1 = self.__find_person(name1)
        p2 = self.__find_person(name2)
        p1.follow(p2)
        p2.influence(p1)
    
    def delate_link(self):
        name1 = str(input("Main name of the follower: "))
        name2 = str(input("Main name of the influencer: "))
        p1 = self.__find_person(name1)
        p2 = self.__find_person(name2)
        p1.stop_following(p2)
        p2.stop_influencing(p1)

    def save(self):
        with open(os.path.abspath(__file__)[:-25] + "data.json", "w") as file:
            json.dump(self.__people_pull, file, cls=Person.PersonEncoder, indent=4)

    def load(self):
        with open(os.path.abspath(__file__)[:-25] + "data.json", "r") as file:
            loaded = json.load(file, cls=Person.PersonDecoder)
        self.__people_pull.extend(loaded)
    
    def __str__(self):
        return str(self.__people_pull)

ui = UserInterface()
# ui.create_person()
# ui.create_person()
# ui.create_link()
# ui.save()
ui.load()
print(ui)
ui.create_link()
ui.save()
# ui.create_person()
# ui.create_link()
# ui.save()