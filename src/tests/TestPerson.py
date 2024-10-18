print("Test Person")
import unittest 
import sys
import os

# Ajouter dynamiquement le chemin vers le répertoire 'src/main'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))

from Person import Person
class TestPerson(unittest.TestCase):

    def test_celebrate_birthday(self):
        john = Person(first_name=["John", "Michael"], last_name="Doe", age=30)
        john.celebrate_birthday()

        self.assertEqual(john.get_age(), 31)

    def test_person_follow(self):
        john = Person(first_name=["John"], last_name="Doe", age=30)
        jane = Person(first_name=["Jane"], last_name="Smith", age=25)
        
        john.follow(jane)
        followed = john.get_followed()
        
        # Verifying if jane exists in john's followed list
        self.assertIn(jane, followed)
        self.assertEqual(len(followed), 1)
        self.assertEqual(followed[0].get_first_name(), ["Jane"])

if __name__ == '__main__':
    unittest.main()