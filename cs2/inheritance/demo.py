class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} is {self.age} years old"

    def have_birthday(self):
        self.age += 1
        print(f"{self.name} grew up and is now {self.age}")


class Dog(Animal):
    def __init__(self, name, age, breed):
        self.breed = breed
        super().__init__(name, age)

    def __repr__(self):
        return f"{self.name} is a {self.breed} and is {self.age}"

    def bark(self):
        print(f"{self.name} is barking")


class Bird(Animal):
    def __init__(self, name, age, color):
        self.color = color
        super().__init__(name, age)

    def eat(self):
        print(f"{self.name} is eating")


woodpecker = Bird("bob", 3, "blue")
woodpecker.eat()  # bob is eating
print(woodpecker)  # bob is 3 years old


peanut = Dog("peanut", 2, "Bernadoodle")
print(peanut)  # peanut is a Bernadoodle and is 2
peanut.bark()  # peanut is barking


peanut.have_birthday()  # peanut grew up and is now 3
print(peanut)  # peanut is a Bernadoodle and is 3


woodpecker.have_birthday()  # bob grew up and is now 4
print(woodpecker)  # bob is 4 years old


print(isinstance(peanut, Dog))  # True
print(isinstance(woodpecker, Dog))  # False
print(isinstance(peanut, Animal))  # True
