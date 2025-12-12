import re


class Duration:
    def __init__(self, hours, minutes, seconds):
        self.totalSeconds = int(hours * 3600 + minutes * 60 + seconds)

        self.hours = abs(self.totalSeconds) // 3600
        self.minutes = abs(self.totalSeconds) // 60 % 60
        self.seconds = abs(self.totalSeconds) % 60

        if self.totalSeconds < 0:
            self.hours *= -1
            self.minutes *= -1
            self.seconds *= -1

    def __str__(self):
        sign = "-" if self.totalSeconds < 0 else ""
        return f"{sign}{abs(self.hours)}h{abs(self.minutes):02}m{abs(self.seconds):02}s"

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

    def __neg__(self):
        return Duration(0, 0, -self.totalSeconds)

    def __add__(self, other):
        return Duration(0, 0, self.totalSeconds + other.totalSeconds)

    def __sub__(self, other):
        return Duration(0, 0, self.totalSeconds - other.totalSeconds)

    def __mul__(self, n):
        return Duration(0, 0, self.totalSeconds * n)

    def __truediv__(self, n):
        return Duration(0, 0, self.totalSeconds / n)


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
