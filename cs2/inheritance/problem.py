import random
import os

# The game has 3 classes:
#   Regular Characters
#   Warriors
#   Wizards
# All characters can:
#   Attack
#   Take Damage
#   Display their health bar
# The wizard can resore mana
# The warrior can restore health
# The combat flow goes like this:
#  1. The player selects a class
#  2. The player and enemy health bars are displayed
#  3. The player can either attack, use their ability, do nothing or run
#  4. The enemy attacks the player
#  5. Repeat parts 2-4 until on of the following is true:
#       The player dies
#       The enemy dies
#       The player runs away


class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

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

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage!")

    def attack(self, other):
        damage = self.power * random.randint(1, 2)
        print(f"{self.name} attacks {other.name}")
        other.take_damage(damage)

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

    def show_special(self):
        print("2 - Defend (restore HP)")

    def do_special(self):
        self.defend()


class Wizard(Character):
    def __init__(self, name, health, power, mana):
        # same as above
        pass

    def __repr__(self):
        # call the parent repr method and add a line to show the wizards mana
        pass

    def attack(self, enemy):
        multiplier = 1 + (self.mana / 30)
        # add a check for mana, wizards can only attack with AT LEAST 5 mana
        # attack the enemy by self.power * a random number from 1 - 2 * multiplier
        pass

    def meditate(self):
        max_mana = 30
        if self.mana >= max_mana:
            print(f"{self.name} is already at full mana")
            return
        self.mana = min(self.mana + 10, max_mana)
        print(f"{self.name} restores mana. Now at {self.mana}")

    def show_special(self):
        print("2 - Meditate (restore mana)")

    def do_special(self):
        self.meditate()


def main():
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
        # print out the player and enemy stats with writing "print" only once
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
        print("You defeated the enemy!")
    if not player.is_alive():
        print("The enemy defeated you!")


if __name__ == "__main__":
    main()
