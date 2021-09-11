from Galactic_JaCoB.Scripts.Locations import *
from random import *
import unittest


class TestLocations(unittest.TestCase):
    def setUp(self):
        self.loc = Location(3,8,29)
        self.loc.ships.append('ghost')
        self.loc.ships.append('titanic')
        self.star = StarSystem('Goo',1,2,3,37,11,103,2,13,5)

    def test_TestLoc(self):
        self.assertEqual(str(self.loc),'3,8,29')
        self.assertEqual(str(self.star),'1,2,3')
        out = ','.join(self.loc.ships)
        self.assertEqual(out,'ghost,titanic')

    def tearDown(self):
        del self.loc
        del self.star


if __name__ == '__main__':
    unittest.main('Galactic_JaCoB.Tests.Test_Locations', verbosity = 2)
