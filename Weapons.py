import re
import random

class Weapon:
    """Used during server init to build the various types of weapons.

        Each weapon 'fires' itself and handles its own data including
        decrementing cooldown and depleting munitions supplies.

        When it does fire, it responds with a tuple.  The first value
        represents how successful the shot was based on it's own odds
        of scoring a hit.  Positive values represent how much it missed
        by while negative values indicate the margin by which it
        succeeded.  The second value is the amount of damage it does.
        This tuple can be passed to the target which can adjust the
        first value based on its ships ability to evade and if it is
        a hit, it will subtract the second value from its current
        hull points.  If this gets to zero or below, then the ship
        handles its own destruction.

        
        """

    def __init__(self, name, size, cooldown, tohit, damage, ammo):
        self.name = name
        self.size = size
        self.cool_max = cooldown
        self.cool_current = 0
        self.tohit = tohit
        self.rolls, self.die, self.modifier = re.split('[dD ]'
                                                       ,damage)
        self.ammo = ammo
        self.ammo_max = ammo

    def __str__(self):
        out = self.name + ':'
        out += ' sz=' + str(self.size)
        out += ' cl=' + str(self.cool_current) + '/' + str(self.cool_max)
        out += ' dg=' + self.rolls + 'D' + self.die + self.modifier
        if(self.ammo_max > 0):
            out += ' am=' + str(self.ammo) + '/' + str(self.ammo_max)
        return(out)

    def fire(self):
        result = (1000,0)
        if(self.cool_current > 0):
            self.cool_current -= 1
        elif(self.ammo_max == 0 or self.ammo > 0):
            success = random.randint(1,100) - self.tohit
            dmg = 0
            for d in range(1,self.rolls):
                dmg += random.randint(1,self.die)
            dmg += self.modifier
            self.cool_current = self.cool_max
            if(self.ammo_max > 0):
                self.ammo -= 1
            result = (success,dmg)
        return(result)

    def reload(self,rounds):
        self.ammo += rounds
        remains = self.ammo - self.ammo_max
        if(remains > 0):
            self.ammo = self.ammo_max
        return(remains)


