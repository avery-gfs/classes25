import re


class Duration:
    def __init__(self, hours, minutes, seconds):
        pass

    def __str__(self):
        return f""

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __neg__(self):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, n):
        pass

    def __truediv__(self, n):
        pass


print(str(Duration(1, 23, 4)))
print(str(Duration(0, 0, -100)))
print(str(Duration(-1, -1, -1)))

print(Duration(1, 23, 4) == Duration(1, 23, 4))
print(Duration(1, 23, 4) <= Duration(1, 23, 4))
print(Duration(1, 23, 4) < Duration(4, 0, 0))
print(Duration(1, 23, 4) > Duration(0, 50, 50))
print(Duration(1, 23, 4) <= Duration(1, 23, 4))
print(Duration(1, 23, 4) <= Duration(4, 0, 0))
print(Duration(1, 23, 4) >= Duration(0, 50, 50))
print(Duration(1, 23, 4) >= Duration(1, 23, 4))

print(Duration(1, 23, 4) + Duration(10, 0, 0))
print(Duration(1, 23, 4) + Duration(0, 10, 0))
print(Duration(1, 23, 4) + Duration(0, 0, 10))
print(Duration(1, 23, 4) + Duration(10, 57, 57))

print(-Duration(0, 0, 100) == Duration(0, 0, -100))

print(Duration(1, 23, 4) - Duration(1, 0, 0))
print(Duration(1, 23, 4) - Duration(0, 57, 0))
print(Duration(1, 23, 4) - Duration(0, 0, 57))
print(Duration(1, 23, 4) - Duration(1, 23, 5))
print(Duration(0, 0, 1) - Duration(1, 0, 0))

print(Duration(1, 23, 4) * 2)
print(Duration(1, 23, 4) * 10)

print(Duration(1, 23, 4) / 2)
print(Duration(1, 23, 4) / 10)
