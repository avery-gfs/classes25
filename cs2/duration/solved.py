class Duration:
    def __init__(self, hours, minutes, seconds):
        self.totalSeconds = max(int(hours * 3600 + minutes * 60 + seconds), 0)

    def __str__(self):
        hours = self.totalSeconds // 3600
        minutes = (self.totalSeconds // 60) % 60
        seconds = self.totalSeconds % 60

        return f"{hours}h{minutes:02}m{seconds:02}s"

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

    @staticmethod
    def fromStr(durStr):
        hours = int(durStr[:-7])
        minutes = int(durStr[-6:-4])
        seconds = int(durStr[-3:-1])
        return Duration(hours, minutes, seconds)


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
