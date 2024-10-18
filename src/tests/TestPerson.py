print("Test Person")
import unittest 
import sys
import os

# Ajouter dynamiquement le chemin vers le répertoire 'src/main'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))

from Person import Person
class TestPerson(unittest.TestCase):
    def setUp(self):
        self.john = Person(first_name=["John"], last_name="Doe", age=30)
        self.jane = Person(first_name=["Jane"], last_name="Smith", age=25)
        self.james = Person(first_name=["James"], last_name="Arthur", age=25)

    def test_celebrate_birthday(self):
        self.john.celebrate_birthday()
        self.assertEqual(self.john.get_age(), 31)

    def test_person_follow(self):
        self.john.follow(self.jane)
        followed = self.john.get_followed()
        
        #Test : follow
        # Verifying if jane exists in john's followed list
        self.assertIn(self.jane, followed)
        self.assertEqual(len(followed), 1)
        self.assertEqual(followed[0].get_first_name(), ["Jane"])

    def test_person_influence(self):
        self.james.influence(self.jane)
        influenced=self.james.get_influenced()

        #Test : influence 
        # Verifying if jane exists in james' influenced list
        self.assertIn(self.jane, influenced)
        self.assertEqual(len(influenced), 1)
        self.assertEqual(influenced[0].get_first_name(), ["Jane"])

    def test_person_stop_following(self):
        self.john.follow(self.jane)
        self.john.follow(self.james)
        followed = self.john.get_followed()
       
        #At first before stop following, verifying existence of all followed people 
        self.assertIn(self.jane, followed)
        self.assertIn(self.james, followed)

        self.john.stop_following(self.jane)
        #Verifying that john only keeps following james
        self.assertEqual(self.john.get_followed()[0].get_first_name(), ["James"])

        self.john.stop_following(self.james)
        #Verifying that john no longer follows james => john doesnt follow anyone
        self.assertEqual(len(self.john.get_followed()), 0)

def test_person_stop_influencing(self):
        self.jane.influence(self.james)
        influenced = self.jane.get_influenced()

        # Verifying that james is in jane's influenced list
        self.assertIn(self.james, influenced)

        self.jane.stop_influencing(self.james)
        # Verifying that james is no longer in jane's influenced list
        self.assertNotIn(self.james, self.jane.get_influenced())
        self.assertEqual(len(self.jane.get_influenced()), 0)  


if __name__ == '__main__':
    unittest.main()