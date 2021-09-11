""" Executing these steps should get the host server up and running.

"""
import Locations
import Weapons
import Ships

StarMap = []
WeaponTypes = []
ShipClasses = []
Players = []

starfile = open('../Data/Starnames.dat','r')
for line in starfile:
        good = false
        while not good:
                x = random.randint(1,700)
                y = random.randint(1,375)
                z = random.randint(1,150)
                good = somehow check to see if location with 3 stars already exists there
        if there is already a location there:
                add this star to the stars in the location
        else:
                StarMap.append(StarSystem(name, x, y, z))
starfile.close()

weapfile = open('../Data/WeaponTypes.dat','r')
for line in weapfile:
        WeaponTypes.append(map(Weapon,line.split(',')))
weapfile.close()

shipfile = open('../Data/ships.dat','r')
for line in shipfile:
        ShipClasses.append(map(ShipClass,line.split(',')))
shipfile.close()

# Note: the following is pretty much psuedocode as I think this through
"""
for system in StarMap:
    Generate a random number of random ships and append to system[3].ships

Generate some number of AI players and give them systems with their ships
    (no insurrections here)

Begin the primary game loop
    Jump ships to hyperspace as needed
    Listen for new clients joining the game
        when one does, insurrection
    Listen for client commands
        follow them
    Find all systems with ships of differing owners
        resolve some number of rounds of combat for each of the systems
    decrement time in hyperspace for all ships there.
    arrive ships to systems whose time in hyperspace has reached 0
    update who conrols stars
    increment resources at all stars in control of a player
"""
