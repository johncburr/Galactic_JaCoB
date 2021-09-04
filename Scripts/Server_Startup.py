""" Executing these steps should get the host server up and running.

"""

# Note: the following is pretty much psuedocode as I think this through
Map = []
starfile = open('data/stars.dat','r')
planetfile = open('data/planets.dat','r')
for line in starfile:
    parms = line.split(',')
    newStar = StarSystem(parms)
    newStar.planets.append(planetfile.readline())
    Map.append([parms[1],parms[2],parms[3],newStar])
starfile.close()
planetfile.close()

Players = []

ShipClasses = []
shipfile = open('data/ships.dat','r')
weaponfile = open('data/weapons.dat','r')
for line in shipfile:
    parms = line.split(',')
    newShip = ShipClass(parms[1:])
    weapCount = int(parms[0])
    while weapCount > 0:
        newShip.weapons.append(weapons.readline())
        weapCount -= 1
shipfile.close()
weaponfile.close()
# ...and the psuedocode get less code and more psuedo
for system in Map:
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
