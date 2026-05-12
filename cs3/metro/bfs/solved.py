import json

with open("connections.json") as file:
    links = json.load(file)


def showRoute(stations):
    return "\n│\n".join("• " + station for station in stations)


def search(src, dest):
    queue = [src]
    parents = {src: None}

    while queue:
        station = queue.pop(0)

        if station == dest:
            path = []

            while dest:
                path.append(dest)
                dest = parents[dest]

            return path[::-1]

        for child in links[station]:
            if child not in parents:
                queue.append(child)
                parents[child] = station


route = search("jarry", "namur")
print(showRoute(route))
