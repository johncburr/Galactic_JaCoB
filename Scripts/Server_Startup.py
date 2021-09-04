""" Executing these steps should get the host server up and running.

"""
import Locations
import Weapons

Map = []
ShipClasses = []
WeaponTypes = []
Players = []

starfile = open('../data/stars.dat','r')
for line in starfile:
	raw = line.split(',')
	name = raw[0]
	x = int(raw[1])
	y = int(raw[2])
	z = int(raw[3])
	people = int(raw[4])
	minerals = int(raw[5])
	energy = int(raw[6])
	people_rate = float(raw[7])
	mineral_rate = int(raw[8])
	energy_rate = int(raw[9])
	star = StarSystem(name
                          ,x
                          ,y
                          ,z
                          ,people
                          ,minerals
                          ,energy
                          ,people_rate
			  ,mineral_rate
                          ,energy_rate)
	Map.append([x, y, z, star])
starfile.close()

weapfile = open('../data/WeaponTypes.dat','r')
for line in weapfile:
    raw = line.split(',')
    name = raw[0]
    cooldown = int(raw[1])
    to_hit = int(raw[2])
    damage = raw[3]
    ammo = int(raw[4])
    weap = Weapon(name
                  ,cooldown
                  ,to_hit
                  ,damage
                  ,ammo)
    WeaponTypes.append([name,weap])
weapfile.close()

shipfile = open('../data/ships.dat','r')
for line in shipfile:
    shipraw = line.split(',')
    name = shipraw[0]
    hull = int(shipraw[1])
    acceleration = int(shipraw[2])
    jump_range = int(shipraw[3])
    cargo = int(shipraw[4])
    crew_min = int(shipraw[5])
    passengers = int(shipraw[6])
    newShip = ShipClass(name
                        ,hull
                        ,acceleration
                        ,jump_range
                        ,cargo
                        ,crew_min
                        ,passengers)
    ShipClasses.append(newShip)
shipfile.close()

# Note: the following is pretty much psuedocode as I think this through
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
