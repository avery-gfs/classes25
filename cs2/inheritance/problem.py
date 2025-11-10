import random
import os


class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def __repr__(self):
        return f"{self.name} | {self.health} HP | {self.power} power"

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage!")

    def attack(self, other):
        damage = self.power * random.randint(1, 2)
        print(f"{self.name} attacks {other.name}")
        other.take_damage(damage)

    def show_health(self):  # theres no need to try and understand this method
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

        print(f"{self.name:10} {color}[{bar}]{reset} {percentage}/100 HP")

    def is_alive(self):
        return self.health > 0


# DONT MODIFY ABOVE THIS LINE


class Warrior(Character):
    def __init__(self, name, health, power, armor):
        self.armor = armor
        # initialize name,health, and power WITHOUT writing them out like with armor

    def defend(self):
        # increase the warriors health by armor time and random number bewtwen 1 and 2
        # hint: the syntax for getting the random number is random.randint(1,2)
        pass


class Wizard(Character):
    def __init__(self, name, health, power, mana):
        pass

    # override the parent __repr__ method with a wizard specific one that shows name and mana

    def attack(self, enemy):
        # use super() to write an attack method that damages the enemy and lowers the wizards mana by 5
        pass

    def meditate(self):
        print(f"{self.name} restores 10 mana")
        self.mana += 10


def main():  # theres also no need to understand most of this method, just try to understand the isinstance use here
    os.system("clear")
    print("Choose your hero!")
    print("1. Warrior")
    print("2. Wizard")

    choice = input("> ")

    if choice == "1":
        player = Warrior("Thorin", 45, 12, 8)
    else:
        player = Wizard("Gandalf", 35, 10, 30)

    enemy = Character("Troll", 60, 5)

    while player.is_alive() and enemy.is_alive():
        # call show_health on the player and the enemy using a for loop and only writing one call
        print("\nYour Turn")
        print("1 - attack")
        if isinstance(player, Warrior):
            print("2 - Defend (restore HP)")
        elif isinstance(player, Wizard):
            print("2 - meditate (restore mana)")
        print("3 - do nothing")
        print("4 - quit")

        choice = input("> ")

        match choice:
            case "1":
                player.attack(enemy)
            case "2":
                if isinstance(player, Warrior):
                    player.defend()
                elif isinstance(player, Wizard):
                    player.meditate()
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
