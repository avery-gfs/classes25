import re


class Duration:
    def __init__(self, hours, minutes, seconds):
        self.totalSeconds = int(hours * 3600 + minutes * 60 + seconds)
        absSeconds = abs(self.totalSeconds)
        self.hours = absSeconds // 3600
        self.minutes = absSeconds // 60 % 60
        self.seconds = absSeconds % 60

    def __str__(self):
        if self.totalSeconds < 0:
            return f"-{self.hours}h{self.minutes:02}m{self.seconds:02}s"

        return f"{self.hours}h{self.minutes:02}m{self.seconds:02}s"

    def __eq__(self, other):
        return self.totalSeconds == other.totalSeconds

    def __lt__(self, other):
        return self.totalSeconds < other.totalSeconds

    def __gt__(self, other):
        return self.totalSeconds > other.totalSeconds

    def __le__(self, other):
        return self.totalSeconds <= other.totalSeconds

    def __ge__(self, other):
        return self.totalSeconds >= other.totalSeconds

    def __add__(self, other):
        return Duration(0, 0, self.totalSeconds + other.totalSeconds)

    def __sub__(self, other):
        return Duration(0, 0, self.totalSeconds - other.totalSeconds)

    def __mul__(self, n):
        return Duration(0, 0, self.totalSeconds * n)

    def __truediv__(self, n):
        return Duration(0, 0, self.totalSeconds / n)

    def __neg__(self):
        return Duration(0, 0, -self.totalSeconds)


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
