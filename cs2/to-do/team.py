class Player:
    def __init__(self, name):
        self.name = name

        # Baskets count starts at 0
        self.baskets = 0

        # Shots count starts at 0
        self.shots = 0

    def __repr__(self):
        # Example: "Avery 9/10"
        return f"{self.name} {self.baskets}/{self.shots}"


class Team:
    def __init__(self):
        # List of player objects, starts empty
        self.players = []

    def addPlayer(self, name):
        # Make a new player with the given name and add to team
        self.players.append(Player(name))

    def addBasket(self, name):
        # Find the player matching name and update basket and shot count
        for player in self.players:
            # Find the player with the matching name
            if player.name == name:
                # Update both shots and baskets for successful shot
                player.baskets += 1
                player.shots += 1

    def addMiss(self, name):
        # Find the player matching name and update shot count
        for player in self.players:
            # Find the player with the matching name
            if player.name == name:
                # Only update shots for unsuccessful shot
                player.shots += 1

    def __repr__(self):
        # Number of players
        numPlayers = len(self.players)

        # Use to count total baskets
        totalBaskets = 0

        # Use to count total shots
        totalShots = 0

        # Use to build string representation
        result = ""

        for player in self.players:
            # Calls player __repr__ method and add newline
            result += f"{player}\n"
            # Add players stats to totals
            totalBaskets += player.baskets
            totalShots += player.shots

        # Add divider line
        result += "-" * 20
        # Add row with summary information
        result += f"\n{numPlayers} players {totalBaskets}/{totalShots} total"
        return result


team = Team()

team.addPlayer("alex")
team.addPlayer("marcus")

team.addBasket("marcus")
team.addBasket("marcus")

team.addMiss("marcus")
team.addMiss("alex")

print(team)

# Prints:
#
# alex 0/1
# marcus 2/3
# --------------------
# 2 players 2/4 total
