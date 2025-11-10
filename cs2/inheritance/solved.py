import random
import os


class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage!")

    def attack(self, other):
        damage = self.power * random.randint(1, 2)
        print(f"{self.name} attacks {other.name}!")
        other.take_damage(damage)

    def __repr__(self):
        bar_length = 20
        filled = int((self.health / 100) * bar_length)
        empty = bar_length - filled
        bar = "█" * filled + "░" * empty
        percentage = max(0, int(self.health))

        if self.health > 50:
            color = "\033[92m"
        elif self.health > 25:
            color = "\033[93m"
        else:
            color = "\033[91m"
        reset = "\033[0m"

        return f"{self.name:10} {color}[{bar}]{reset} {percentage}/100 HP"

    def is_alive(self):
        return self.health > 0


# DONT MODIFY ABOVE THIS LINE


class Warrior(Character):
    def __init__(self, name, health, power, armor):
        super().__init__(name, health, power)
        self.armor = armor

    def defend(self):
        reduced = int(self.armor * random.randint(1, 2))
        print(f"{self.name} restores {reduced} HP!")
        self.health += reduced

    def show_special(self):
        print("2 - Defend (restore HP)")

    def do_special(self):
        self.defend()


class Wizard(Character):
    def __init__(self, name, health, power, mana):
        super().__init__(name, health, power)
        self.mana = mana

    def attack(self, enemy):
        super().attack(enemy)
        print(f"{self.name} attacks {enemy}!")
        self.mana -= 5
        print(f"{self.name} has {self.mana} left")

    def meditate(self):
        print(f"{self.name} restores 10 mana")
        self.mana += 10

    def show_special(self):
        print("2 - meditate (restore mana)")

    def do_special(self):
        self.meditate()


# DONT TOUCH ANYHTHING BELOW THIS COMMENT


def main():
    os.system("clear")
    print("Choose your hero!")
    print("1. Warrior")
    print("2. Wizard")

    choice = input("> ")

    if choice == "1":
        player = Warrior("Thorin", 100, 12, 8)
    else:
        player = Wizard("Gandalf", 100, 10, 30)

    enemy = Character("Troll", 100, 9)

    while player.is_alive() and enemy.is_alive():
        for i in [player, enemy]:
            print(i)

        print("\nYour Turn")
        print("1 - attack")

        player.show_special()

        print("3 - do nothing")
        print("4 - quit")

        choice = input("> ")

        match choice:
            case "1":
                player.attack(enemy)
            case "2":
                player.do_special()
            case "3":
                print(f"{player.name} does nothing")
            case "4":
                print("you fled the battle")
                break
            case _:
                print("invalid option")

        if enemy.is_alive():
            enemy.attack(player)

        print("\n")

    if not enemy.is_alive():
        print(f"You defeated the enemy!")

    if not player.is_alive():
        print(f"The enemy defeated you!")


if __name__ == "__main__":
    main()
