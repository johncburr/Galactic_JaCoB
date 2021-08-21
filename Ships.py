

class ShipClass:
    """This sets basic parameters for each type of ship.

    Such creation is only intended to occur when configuring a server
    and should be accomplished by reading an encrypted data file or
    something.  I will have to explore my options later, but once all
    of the ShipClasses are defined, then ships can be created during
    normal gameplay.
    """

    def __init__(self
                 ,name
                 ,hull
                 ,acceleration
                 ,jump_range
                 ,cargo
                 ,crew_min
                 ,passengers
                 ):
        self.name = name
        self.hull_max = hull
        self.acceleration = acceleration
        self.jump_range = jump_range
        self.crew_max = crew_min * 3
        self.crew_min = crew_min
        self.cargo_max = cargo
        self.passenger_max = passengers
        self.weapons = []
 
    def add_weapon(self
                   ,Weapon
                   ):
        self.weapons.append(Weapon)

    def remove_weapon(self
                      ,weapon
                      ):
        """If I have to use this method, then I oopsed somewhere."""
        self.weapons.remove(Weapon)


class Ship:
    """Every ship will be one of these."""

    def __init__(self
                 ,DesignClass
                 ,name
                 ,Owner
                 ,Location
                 ):
        self.design_class = DesignClass.name
        self.name = name
        self.Owner = Owner
        self.Location = Location
        self.crew_current = DesignClass.crew_min * 2
        self.cargo_current = 0
        self.passengers_current = 0
        self.weapons.extend(DesignClass.weapons[])
        self.Destination = Location
        self.Hull = DesignClass.hull_max
        self.jump_range = DesignClass.jump_range
