""" This contains all functions/scripts or whatever necessary to set up
    a new player who just dropped in to the game.

>>> system =
>>> player = 
>>> start_insurrection(system,player)
>>> print system.owner

>>> print player.systems

>>> print player.ships

"""
def start_insurrection(system,player):
    system.owner = player
    player.systems.append([system.x, system.y, system.z, system])
    for ship in system.ships: # you get all of them for now.
        ship.owner = player
        player.ships.append(ship)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
