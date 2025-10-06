class Duration:
    def __init__(self, hours, minutes, seconds):
        pass

    def __repr__(self):
        return ""

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass


d = Duration(2, 20, 30)

print(d)
print(d + Duration(1, 40, 40))
print(d - Duration(1, 40, 40))
