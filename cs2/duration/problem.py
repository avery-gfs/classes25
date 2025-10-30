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

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, n):
        pass

    def __truediv__(self, n):
        pass

    @staticmethod
    def fromStr(durStr):
        pass


d = Duration(1, 23, 4)

print(str(d) == "1h23m04s")

print(d == Duration(1, 23, 4))
print(d <= Duration(1, 23, 4))
print(d < Duration(4, 0, 0))
print(d > Duration(0, 50, 50))
print(d <= Duration(1, 23, 4))
print(d <= Duration(4, 0, 0))
print(d >= Duration(0, 50, 50))
print(d >= Duration(1, 23, 4))

print(d + Duration(10, 0, 0) == Duration(11, 23, 4))
print(d + Duration(0, 10, 0) == Duration(1, 33, 4))
print(d + Duration(0, 0, 10) == Duration(1, 23, 14))
print(d + Duration(0, 57, 0) == Duration(2, 20, 4))
print(d + Duration(0, 0, 57) == Duration(1, 24, 1))
print(d + Duration(10, 57, 57) == Duration(12, 21, 1))

print(d - Duration(10, 0, 0) == Duration(0, 0, 0))
print(d - Duration(0, 57, 0) == Duration(0, 26, 4))
print(d - Duration(0, 0, 57) == Duration(1, 22, 7))
print(d - Duration(10, 57, 57) == Duration(0, 0, 0))

print(d * 2 == Duration(2, 46, 8))
print(d * 10 == Duration(13, 50, 40))

print(d / 2 == Duration(0, 41, 32))
print(d / 10 == Duration(0, 8, 18))

print(Duration.fromStr("1h23m04s") == Duration(1, 23, 4))
