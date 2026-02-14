import json

with open("connections.json") as file:
    connections = json.load(file)


def showRoute(stations):
    return "\n│\n".join("• " + station for station in stations)


found = set()


def getRoute(station, dest):
    if station == dest:
        return [dest]

    if station in found:
        return None

    found.add(station)

    for neighbor in connections[station]:
        path = getRoute(neighbor, dest)

        if path != None:
            return [station] + path

    return None


route = getRoute("jarry", "namur")
print(showRoute(route))
