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


print("test str() :", str(Duration(1, 23, 4)) == "1h23m04s")

print("test == :", Duration(1, 23, 4) == Duration(1, 23, 4))
print("test <= :", Duration(1, 23, 4) <= Duration(1, 23, 4))
print("test < :", Duration(1, 23, 4) < Duration(4, 0, 0))
print("test > :", Duration(1, 23, 4) > Duration(0, 50, 50))
print("test <= :", Duration(1, 23, 4) <= Duration(1, 23, 4))
print("test <= :", Duration(1, 23, 4) <= Duration(4, 0, 0))
print("test >= :", Duration(1, 23, 4) >= Duration(0, 50, 50))
print("test >= :", Duration(1, 23, 4) >= Duration(1, 23, 4))

print("test + :", Duration(1, 23, 4) + Duration(10, 0, 0) == Duration(11, 23, 4))
print("test + :", Duration(1, 23, 4) + Duration(0, 10, 0) == Duration(1, 33, 4))
print("test + :", Duration(1, 23, 4) + Duration(0, 0, 10) == Duration(1, 23, 14))
print("test + :", Duration(1, 23, 4) + Duration(10, 57, 57) == Duration(12, 21, 1))

print("test - :", Duration(1, 23, 4) - Duration(1, 0, 0) == Duration(0, 23, 4))
print("test - :", Duration(1, 23, 4) - Duration(0, 57, 0) == Duration(0, 26, 4))
print("test - :", Duration(1, 23, 4) - Duration(0, 0, 57) == Duration(1, 22, 7))

print("test * :", Duration(1, 23, 4) * 2 == Duration(2, 46, 8))
print("test * :", Duration(1, 23, 4) * 10 == Duration(13, 50, 40))

print("test / :", Duration(1, 23, 4) / 2 == Duration(0, 41, 32))
print("test / :", Duration(1, 23, 4) / 10 == Duration(0, 8, 18))

print("test negative :", str(Duration(0, 0, -100)) == "-0h01m40s")
print("test negative :", str(Duration(-1, -1, -1)) == "-1h01m01s")
print("test negative :", -Duration(0, 0, 100) == Duration(0, 0, -100))
print("test negative :", Duration(1, 23, 4) - Duration(1, 23, 5) == Duration(0, 0, -1))
print("test negative :", Duration(0, 0, 1) - Duration(1, 0, 0) == Duration(0, -59, -59))
