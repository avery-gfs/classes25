import json

with open("connections.json") as file:
    connections = json.load(file)


def showRoute(stations):
    return "\n│\n".join("• " + station for station in stations)


found = set()


def getRoute(station, dest):
    pass


route = getRoute("jarry", "namur")
print(showRoute(route))
