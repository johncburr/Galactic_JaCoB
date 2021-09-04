

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
                 ,passengers):
        self.name = name
        self.hull_max = hull
        self.acceleration = acceleration
        self.jump_range = jump_range
        self.crew_min = crew_min
        self.cargo_max = cargo
        self.passenger_max = passengers
        self.weapons = []

    def __str__(self):
        out = ''.join((self.name, '-', 'Hull:', repr(self.hull)
                      , ' Accl:', repr(self.acceleration)
                      , ' Rnge:', repr(self.jump_range)
                      , ' Crew:', repr(self.crew_min * 2)))
        if(self.cargo > 0):
            out = ''.join((out, ' Crgo:', repr(self.cargo)))
        if(self.passengers > 0):
            out = ''.join((out, ' Pass:', repr(self.passengers)))
        weap = '\n'.join(weapon.name for weapon in self.weapons)
        return('\n'.join((out,name)))


class Ship:
    """Every ship will be one of these."""

    def __init__(self
                 ,design_class
                 ,name
                 ,owner
                 ,location
                 ):
        self.design_class = design_class.name
        self.name = name
        self.owner = owner
        self.location = location
        self.crew_max = design_class.crew_min * 3
        self.crew_current = design_class.crew_min * 2
        self.crew_min = design_class.crew_min
        self.cargo_max = design_class.cargo_max
        self.cargo_current = 0
        self.passenger_max = design_class.passenger_max
        self.passengers_current = 0
        self.weapons.extend(design_class.weapons)
        self.destination = location
        self.hull_current = design_class.hull_max
        self.hull_max = design_class.hull_max
        self.jump_range = design_class.jump_range
        self.target = None
        self.transit = 0
        self.acceleration = design_class.acceleration

    def __str__(self):
        out = ''.join((self.name, ':'
                       , ' Clss=', self.design_class
                       , ' Ownr=', self.owner.name
                       , ' Rang=', repr(self.range)
                       , ' Lctn=', self.location.name
                       , ' Dest=', self.destination.name
                       , '(', repr(self.transit), ')'
                       , '\nHull=', repr(self.hull_current)
                       , '/', repr(self.hull_max)
                       , ' Crew=', repr(self.crew_current)
                       , '/', repr(self.crew_min * 2)))
        if(self.cargo_max > 0):
            out = ''.join((out, ' Crgo=', repr(self.cargo_current)
                           , '/', repr(self.cargo_max)))
        if(self.passenger_max > 0):
            out = ''.join((' Pass=', repr(self.passengers_current)
                           , '/' + repr(self.passenger_max)))
        weap = '\n'.join((weapon.name for weapon in self.weapons))
        return('\n'.join((out,weap)))

    def make_jump(self
                  ,distance):
        self.location = Hyperspace
        self.transit = distance
        Hyperspace.ships.append(self)

    def arrive(self):
        self.location = self.destination
        self.location.add_ship(self)
        Hyperspace.ships.remove(self)
        self.transit = 0

    def fight(self):
        for weapon in self.weapons:
            self.target.take_damage(weapon.fire())

    def take_damage(self
                    ,dmg):
        if(dmg[0] + self.acceleration * 3 <= 0):
            self.hull_current -= dmg[1]
        if self.hull_current <= 0:
            self.owner.ships.remove(self)
            self.location.ships.remove(self)

    def repair(self
               ,amount):
        self.hull_current += amount
        if self.hull_current > self.hull_max:
            self.hull_current = self.hull_max

