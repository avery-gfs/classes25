# Challenge: make __repr__ work correctly for negative durations


class Duration:
    def __init__(self, hours, minutes, seconds):
        self.seconds = hours * 3600 + minutes * 60 + seconds

    def __repr__(self):
        hours = self.seconds // 3600
        minutes = (self.seconds - hours * 3600) // 60
        seconds = self.seconds - hours * 3600 - minutes * 60
        return f"{hours}h{minutes}m{seconds}s"

    def __add__(self, other):
        return Duration(0, 0, self.seconds + other.seconds)

    def __sub__(self, other):
        return Duration(0, 0, self.seconds - other.seconds)


d = Duration(2, 20, 30)

print(d)
print(d + Duration(1, 40, 40))
print(d - Duration(2, 40, 40))


class Height:
    def __init__(self, feet, inches):
        self.inches = feet * 12 + inches

    def __repr__(self):
        feet = self.inches // 12
        inches = self.inches - feet * 12
        return f"{feet}'{inches}\""

    def __add__(self, other):
        return Height(0, self.inches + other.inches)

    def __sub__(self, other):
        return Height(0, self.inches - other.inches)


h = Height(5, 6)

print(h)  # 5'6"
print(h + Height(1, 4))  # 6'10"
print(h - Height(1, 4))  # 4'2"
print(h + Height(1, 10))  # 7'4"
print(h - Height(1, 10))  # 3'8"
print(h - Height(7, 8))  # -3'10"
