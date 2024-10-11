print("Test pysos")
import unittest

class TestPerson(unittest.TestCase):

    def test_celebrate_birtday(self):
        person = Person(first_name=["John", "Michael"], last_name="Doe", age=30)
        person.celebrate_birthday()
        assert person.__age__==30

    
