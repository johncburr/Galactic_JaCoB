class Location:
    """There are two location types: StarSystems and Hyperspace.

    These will have a set of coordinates in 3D space. Hyperspace will
    need to be located outside of "map" of the game.  Beyond the
    x, y, and z, each location will also need a list of
    ships.

    This class is purely designed to be inherited.
    """
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.ships = []

Hyperspace = Location(0,0,0)

class StarSystem(Location):
    """These are the structure in which the game is played.

    Each StarSystem will have:
        1-3 stars.  (Most will have only 1)
        1-15 useful planets (Purely for flavor)
        Rates for production of various resources

    """
    def __init__(self,
