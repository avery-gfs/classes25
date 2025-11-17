import json

with open("connections.json") as file:
    connections = json.load(file)


def hasPath(station, dest, found=set()):
    if station == dest:
        return True

    if station in found:
        return False

    print(station, dest)
    found.add(station)

    for neighbor in connections[station]:
        if hasPath(neighbor, dest, found):
            return True

    return False


print(hasPath("jarry", "broadway"))
