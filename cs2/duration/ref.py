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


class Height:
    def __init__(self, feet, inches):
        totalInches = max(int(feet * 12 + inches), 0)

        self.feet = totalInches // 12
        self.inches = totalInches % 12

    def __str__(self):
        return f"{self.feet}'{self.inches:02}\""

    def __eq__(self, other):
        return self.feet == other.feet and self.inches == other.inches

    def __lt__(self, other):
        return self.feet < other.feet and self.inches < other.inches

    def __gt__(self, other):
        return self.feet > other.feet and self.inches > other.inches

    def __le__(self, other):
        return self.feet <= other.feet and self.inches <= other.inches

    def __ge__(self, other):
        return self.feet >= other.feet and self.inches >= other.inches

    def __add__(self, other):
        return Height(self.feet + other.feet, self.inches + other.inches)

    def __sub__(self, other):
        return Height(self.feet - other.feet, self.inches - other.inches)

    def __mul__(self, n):
        return Height(self.feet * n, self.inches * n)

    def __truediv__(self, n):
        return Height(self.feet / n, self.inches / n)


class Height:
    def __init__(self, feet, inches):
        self.totalInches = max(int(feet * 12 + inches), 0)

    def __str__(self):
        feet = self.totalInches // 12
        inches = self.totalInches % 12

        return f"{feet}'{inches:02}\""

    def __eq__(self, other):
        return self.totalInches == other.totalInches

    def __lt__(self, other):
        return self.totalInches < other.totalInches

    def __gt__(self, other):
        return self.totalInches > other.totalInches

    def __le__(self, other):
        return self.totalInches <= other.totalInches

    def __ge__(self, other):
        return self.totalInches >= other.totalInches

    def __add__(self, other):
        return Height(0, self.totalInches + other.totalInches)

    def __sub__(self, other):
        return Height(0, self.totalInches - other.totalInches)

    def __mul__(self, n):
        return Height(0, self.totalInches * n)

    def __truediv__(self, n):
        return Height(0, self.totalInches / n)


h = Height(5, 10)

str(h)  # 5'10"

h == Height(5, 10)  # True
h <= Height(5, 10)  # True
h < Height(6, 0)  # True
h > Height(4, 11)  # True
h <= Height(5, 19)  # True
h <= Height(6, 0)  # True
h >= Height(4, 11)  # True
h >= Height(5, 10)  # True

h + Height(1, 0)  # 6'10"
h + Height(0, 1)  # 5'11"
h + Height(0, 4)  # 6'02"
h + Height(1, 4)  # 7'02"

h - Height(1, 0)  # 4'10"
h - Height(0, 1)  # 5'09"
h - Height(0, 11)  # 4'11"
h - Height(1, 11)  # 3'11"

h * 2  # 11'08"
h * 10  # 58'04"
h / 2  # 2'11"
h / 10  # 0'07"
