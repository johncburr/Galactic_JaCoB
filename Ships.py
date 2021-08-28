

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
        self.jump_range = jump_range
        self.crew_min = crew_min
        self.cargo_max = cargo
        self.passenger_max = passengers
        self.weapons = []

    def __str__(self):
        out = self.name + ':'
        out += ' Hull:' + repr(self.hull)
        out += ' Accl:' + repr(self.acceleration)
        out += ' Rnge:' + repr(self.jump_range)
        out += ' Crew:' + repr(self.crew_min * 2)
        if(self.cargo > 0):
            out =+ ' Crgo:' + repr(self.cargo)
        if(self.passengers > 0):
            out += ' Pass:' + repr(self.passengers) + '\n'
        for weapon in self.weapons:
            out += weapon.name + '\n'
        return(out)

    def add_weapon(self
                   ,Weapon
                   ):
        self.weapons.append(Weapon)


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
        self.crew_max = DesignClass.crew_min * 3
        self.crew_current = DesignClass.crew_min * 2
        self.crew_min = DesignClass.crew_min
        self.cargo_max = DesignClass.cargo_max
        self.cargo_current = 0
        self.passenger_max = DesignClass.passenger_max
        self.passengers_current = 0
        self.weapons.extend(DesignClass.weapons)
        self.Destination = Location
        self.hull_current = DesignClass.hull_max
        self.hull_max = DesignClass.hull_max
        self.jump_range = DesignClass.jump_range
        self.target = None
        self.transit = 0

    def __str__(self):
        out = self.name += ':'
        out += ' Clss:' + self.design_class
        out += ' Ownr:' + self.Owner.name
        out += ' Rang:' + repr(self.range)
        out += ' Lctn:' + self.Location.name
        out += (' Dest:' + self.Destination.name
                + '(' repr(self.transit) + ')')
        out += ('\nHull:' + repr(self.hull_current)
                + '/' + repr(self.hull_max))
        out += (' Crew:' + repr(self.crew_current)
                + '/' + repr(self.crew_min * 2))
        if(self.cargo_max > 0):
            out += (' Crgo:' + repr(self.cargo_current)
                    + '/' + repr(self.cargo_max))
        if(self.passenger_max > 0):
            out += (' Pass:' + repr(self.passengers_current)
                    + '/' + repr(self.passenger_max))
        out += '\n'
        return(out)

    def set_course(self
                   ,Destination
                   ):
        self.Destination = Destination

    def make_jump(self
                  ,distance
                  ):
        self.Location = Hyperspace
        self.transit = distance
        Hyperspace.ships.append(self)

    def arrive(self):
        self.Location = self.Destination
        self.Location.add_ship(self)
        Hyperspace.ships.remove(self)
        self.transit = 0

    def set_target(self):
        targ = random.choice()

    def fight(self):
        for Weapon in self.weapons:
            Weapon.fire(self.Target)


    def take_damage(self
                    ,amount
                    ):
        self.hull_current -= amount
        if self.hull_current <= 0:
            self.Owner.ships.remove(self)
            self.Location.ships.remove(self)

    def repair(self
               ,amount
               ):
        self.hull_current += amount
        if self.hull_current > self.hull_max:
            self.hull_current = self.hull_max

