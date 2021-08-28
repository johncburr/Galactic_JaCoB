

class Location:
    """There are two location types: StarSystems and Hyperspace.

    These will have a set of coordinates in 3D space. Hyperspace will
    need to be located outside of "map" of the game.  Beyond the
    x, y, and z, each location will also need a list of
    ships.

    This class is purely designed to be inherited.
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
        return(','.join((repr(x), repr(y), repr(z))))

    # Hyperspace = Location(-1,-1,-1)


class StarSystem(Location):
    """These form the structure in which the game is played.

    Each StarSystem will have:
        1-3 stars.  (Most will have only 1)
        1-15 planets (Purely for flavor)
        Rates for production of various resources

    """
    def __init__(self
                 ,name
                 ,x
                 ,y
                 ,z
                 ,people    # The people available to play in space
                 ,minerals  # The minerals available for space-related stuff
                 ,energy    # The energy available for space-related stuff
                 ,people_rate
                 ,mineral_rate
                 ,energy_rate):
        Location.__init__(self,x,y,z)
        self.name = name
        self.people_lo = people
        self.people_current = random.randint(people, people * 7919 * 13)
        self.people_hi = people * 7919 * 13
        self.minerals = minerals
        self.minerals_hi = minerals * 1973
        self.energy = energy
        self.energy_hi = energy * 2029
        self.people_rate = people_rate
        self.mineral_rate = mineral_rate
        self.energy_rate = energy_rate
        stars = [self.name,]
        planets = []

    def __repr__(self):
        me = ''.join((self.name, ': ', str(self)))
        starlist = ','.join(stars)
        planetlist = ','.joint(planets)
        resources = ','.join(('= '.join(('Pepl', self.people))
                              ,'= '.join(('Mnrl', self.minerals))
                              ,'= '.join(('Enrg', self.energy))))
        return('\n'.join((me,starlist,planetlist,resources)))

