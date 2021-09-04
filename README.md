# Galactic_JaCoB
One game to learn them all. Languages, that is. I write this game to learn a new language. Just might finish it this time. (Python)

This process is painfully slow because I am working on it during my personal time. For example, I am typing this sentence during my lunch break. Some evenings I can carve out a few minutes to work on it, but most is done on Saturday afternoons. I can usually escape to the local library for a few hours on a Saturday afternoon. Definitely not the ideal circumstance for learning a new language.

Thoughts on structure:
    RAM is faster to access than DB (theoretically), but lists of objects aren't that easy to search
    So I'm thinking of using lists of tuples.  The first few values in each tuple become the searchable fields while the last value is the object.

    Global Lists Required:
        StarSystems, Players, ShipClasses,

    The global lists can be read at launch of a server from init files or a local DB. Haven't decided yet.

    I will need to eventually create a protocol for client-server comms. But we'll get there.

    Player choices will include such things as:
        Quit, build a ship, re-supply a ship (or group of ships), send a ship (or group of ships) somewhere else, view a starsystem currently owned or where ships currently are, view "known" map

    The ships, or rather the ships' crews, do all of the actual flying and fighting. This is an actual strategy game not one that only claims to be strategy. Building and Re-supplying ships and choosing where they go is as granular as it gets.

    When a new player drops in, the server chooses a StarSystem.  That StarSystem then undergoes an immediate "insurrection".  The remaining ships become the posession of the player as does the StarSystem.

    An "insurrection" is basically a way of resetting a StarSystem it can result in resources magically being added or disappearing. If the server deems that the new player would have too many or too few ships, adjustments are magically made.

    The size of the sector in which this is played must be large enough to feel almost endless.  Ideally, most players will never encounter the "edge" of the map.  So insurrections will have to occur either in StarSystems currently owned by an active player or within a central area.

    No information on a player is saved anywhere. There are no login credentials. Your username is stored locally. Nobody but you will ever see it and when you encounter another player, their name is one that the client randomly assigned to that other player for the duration of this gaming session.

    When a player quits, their possessions may or may not be "sanitized" and may or may not be handed over to an AI player or another player that just dropped into the game.

    You cannot keep anything from one game session to the next.  I will probably have to consider randomly terminating game sessions that have gone on for too long. Especially if they are getting close to the edge of the map.__
    
