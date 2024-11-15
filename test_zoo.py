import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def testcase_invalid_age(self): 
        self.assertEqual(self.zoo.get_ticket_price(-1), 'Incorrect Input')

    def testcase_age_between_0_and_12(self):
        self.assertEqual(self.zoo.get_ticket_price(4), 50)

    def testcase_age_between_13_and_20(self):
        self.assertEqual(self.zoo.get_ticket_price(19), 100)

    def testcase_age_between_21_and_60(self):
        self.assertEqual(self.zoo.get_ticket_price(24), 150)
        self.assertEqual(self.zoo.get_ticket_price(45), 150)

    def testcase_age_greater_than_60(self):
        self.assertEqual(self.zoo.get_ticket_price(70), 100)

if __name__ == '__main__':
    unittest.main()