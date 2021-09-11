import random


class Location:
    """There are two location types: StarSystems and Hyperspace.

    These will have a set of coordinates in 3D space. Hyperspace will
    need to be located outside of the "map" of the game.  Beyond the
    x, y, and z, each location will also need a list of
    ships.

    I have assembled 597018 unique names for stars.  According to my
    calculations, I need to make a map that is 700 x 375 x 150 light
    years.  Each location in that grid can contain 0 to 3 stars, but
    most need to be empty and 3 stars needs to be exceedingly rare.

>>> Hyperspace = Location(-1000, 34, 62)
>>> str(Hyperspace)
'-1000,34,62'
>>> Hyperspace.ships.append('Ship1')
>>> for ship in Hyperspace.ships: print(str(ship))
Ship1
    """
    def __init__(self
                 ,x
                 ,y
                 ,z):
        self.x = x
        self.y = y
        self.z = z
        self.ships = []

    def __str__(self):
        return(','.join((repr(self.x), repr(self.y), repr(self.z))))

    # Hyperspace = Location(-1,-1,-1)


class StarSystem(Location):
    """These form the structure in which the game is played.

    Each StarSystem will have:
        1-3 stars.  (Most will have only 1)
        Rates for production of various resources
        Any number of ships
        A maximum of one owner
        It was a pain to come up with star names.  Not doing planets.

>>> x = []
>>> x.append(StarSystem('BugCheese', 308, 1221, -47, 32490, 1, 98993, 3, 12, 24))
>>> x[0].ships.append('Firefly')
>>> x[0].planets.append('Pew Pew')
>>> x[0].planets.append('Huzzah')
>>> print(repr(x[0]))
BugCheese: 308,1221,-47
BugCheese
Pepl= ..., Mnrl= 1, Enrg= 98993
>>> for ship in x[0].ships: print(str(ship))
Firefly
    """
    def __init__(self
                 ,name
                 ,x
                 ,y
                 ,z): # all else is random
        Location.__init__(self, x ,y ,z)
        self.name = name
        self.people_lo = people
        self.people = random.randint(people, people * 7919)
        self.people_hi = people * 7919
        self.minerals = minerals
        self.minerals_hi = minerals * 1973
        self.energy = energy
        self.energy_hi = energy * 2029
        self.people_rate = people_rate
        self.mineral_rate = mineral_rate
        self.energy_rate = energy_rate
        self.stars = [self.name,]
        self.planets = []

    def __repr__(self):
        me = ''.join((self.name, ': ', str(self)))
        starlist = ', '.join(self.stars)
        resources = ', '.join(('= '.join(('Pepl', str(self.people)))
                              ,'= '.join(('Mnrl', str(self.minerals)))
                              ,'= '.join(('Enrg', str(self.energy)))))
        return('\n'.join((me,starlist,planetlist,resources)))



if(__name__ == '__main__'):
    import doctest
    doctest.testmod()
    import unittest
    unittest.main('Galactic_JaCoB.Tests.Test_Locations', verbosity = 1)
