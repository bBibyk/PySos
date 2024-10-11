print("Test pysos")
import unittest

from PySos.src.main import Person

class TestPerson(unittest.TestCase):

    def test_celebrate_birtday(self):
        john = Person(first_name=["John", "Michael"], last_name="Doe", age=30)
        john.celebrate_birthday()

        #Test
        self.assertEqual(john.__age__, 31)

    def test_person_follow(self):
        john = Person(first_name=["John"], last_name="Doe", age=30)
        jane = Person(first_name=["Jane"], last_name="Smith", age=25)
        
        john.follow(jane)
        
        #Tests
        self.assertIn(jane, john.__follow__) #Verifying if jane appears in john's followed list 
        self.assertEqual(len(john.__follow__), 1) 
        self.assertEqual(john.__follow__[0].__first_name__, ["Jane"]) 
