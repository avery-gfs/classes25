## All Stats

```py
class TeamStats:
    # Each team will have its own TeamStats object

    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.pointsScored = 0
        self.pointsAllowed = 0
        self.numGames = 0

    def addStats(self, game):
        self.numGames += 1

        if self.name == game["home_team"]:
            self.addStatsHome(game)
        else:
            self.addStatsAway(game)

    # ...
```

## All Stats

```py
class TeamStats:
    # ...
    def addStatsHome(self, game):
        # Update team stats (wins, losses, ties, pointsScored, pointsAllowed)
        # based on game info, knowing that this team was the home team

        pass  # Your code goes here

    def addStatsAway(self, game):
        # Update team stats (wins, losses, ties, pointsScored, pointsAllowed)
        # based on game info, knowing that this team was the away team

        pass  # Your code goes here

    def winPercent(self):
        # Calculate the win percentage

        return 0  # Your code goes here

    def pointsScoredPerGame(self):
        # Calculate points scored per game

        return 0  # Your code goes here

    def pointsAllowedPerGame(self):
        # Calculate points allowed per game

        return 0  # Your code goes here
```

## All Stats

```txt
stats["Philadlphia Eagles"] =
    TeamStats {
        name = "Philadlphia Eagles"
        wins = 0
        losses = 0
        ties = 0
        pointsScored = 0
        pointsAllowed = 0
        numGames = 0
    }
```

```py
game = { "away_team": "Dallas Cowboys", "away_score": 20, "home_team": "Philadelphia Eagles", "home_score": 24 }
stats["Philadlphia Eagles"].addHomeGame(game)
```

```txt
stats["Philadlphia Eagles"] =
    TeamStats {
        name = "Philadlphia Eagles"
        wins = 1
        losses = 0
        ties = 0
        pointsScored = 24
        pointsAllowed = 20
        numGames = 1
    }
```

## All Stats

```txt
stats["Philadlphia Eagles"] =
    TeamStats {
        name = "Philadlphia Eagles"
        wins = 1
        losses = 0
        ties = 0
        pointsScored = 24
        pointsAllowed = 20
        numGames = 1
    }
```

```py
game = { "away_team": "Denver Broncos", "away_score": 21, "home_team": "Philadelphia Eagles", "home_score": 17 }
stats["Philadlphia Eagles"].addHomeGame(game)
```

```txt
stats["Philadlphia Eagles"] =
    TeamStats {
        name = "Philadlphia Eagles"
        wins = 1
        losses = 1
        ties = 0
        pointsScored = 41
        pointsAllowed = 41
        numGames = 2
    }
```

## All Stats

```txt
stats["Philadlphia Eagles"] =
    TeamStats {
        name = "Philadlphia Eagles"
        wins = 1
        losses = 1
        ties = 0
        pointsScored = 41
        pointsAllowed = 41
        numGames = 2
    }
```

```py
stats["Philadlphia Eagles"].winPercent()            # 0.5
stats["Philadlphia Eagles"].pointsScoredPerGame()   # 20.5
stats["Philadlphia Eagles"].pointsAllowedPerGame()  # 20.5
```

---

## Analogy to Scrabble Problem

```py
bestWord = None  # Keep track of the highest scoring word
bestScore = 0  # Keep track of the score of bestWord

for word in words:
    score = 0

    for letter in word:
        score += letterPoints[letter]

    if score > bestScore:
        bestScore = score
        bestWord = word
```

```txt
puzzling
29
```

## Analogy to Scrabble Problem

```py
bestWords = {}  # Keep track of the highest scoring word for each letter
bestScores = {}  # Keep track of the scores for bestWords

for word in words:
    score = 0

    for letter in word:
        score += letterPoints[letter]

    firstLetter = word[0]
    bestScores.setdefault(firstLetter, 0) 

    if bestScores[firstLetter] < score:
        bestWords[firstLetter] = word
        bestScores[firstLetter] = score
```

```txt
c contemptuously 23
i inquisitively 28
d difficulty 22
t thoughtfully 25
r refreshments 20
h hjckrrh 26
a affectionately 25
w whiskers 18
...
```

## Analogy to Scrabble Problem

```py
bestWords = {}
bestScores = {}
```

```py
wins = {}
losses = {}
ties = {}
```

## `setdefault`

```py
votes = { "strawberry": 1, "chocolate": 1, "vanilla": 1 }
votes.setdefault("mint", 0)
votes.setdefault("vanilla", 0)
```

```py
{ 'strawberry': 1, 'chocolate': 1, 'vanilla': 1, 'mint': 0 }
```

## `setdefault`

```py
wins.setdefault(homeTeam, 0)
wins.setdefault(awayTeam, 0)

losses.setdefault(homeTeam, 0)
losses.setdefault(awayTeam, 0)

ties.setdefault(homeTeam, 0)
ties.setdefault(awayTeam, 0)
```

## All Records

```txt
Philadelphia Eagles 8 2 0 0.800
Dallas Cowboys 3 5 1 0.333
Los Angeles Chargers 7 4 0 0.636
Kansas City Chiefs 5 5 0 0.500
New Orleans Saints 2 8 0 0.200
Arizona Cardinals 3 7 0 0.300
New York Jets 2 8 0 0.200
...
```

---

## Data Scraping

https://www.footballdb.com/games/index.html

```js
const rows = $$("tr")
  .filter((tr) => !tr.classList.contains("header"))
  .map((tr) =>
    [...tr.querySelectorAll("td")].map((td) => td.innerText).slice(1, 5).join(
      ",",
    )
  )
  .join("\n");

console.log(`away_team,away_score,home_team,home_score\n${rows}`);
```

## CSV Files

"Comma separated values"

```txt
away_team,away_score,home_team,home_score
Dallas Cowboys,20,Philadelphia Eagles,24
Kansas City Chiefs,21,Los Angeles Chargers,27
Arizona Cardinals,20,New Orleans Saints,13
Pittsburgh Steelers,34,New York Jets,32
Miami Dolphins,8,Indianapolis Colts,33
...
```

- Header row
- Records
- Like a spreadsheet
- Can import and export with spreadsheet programs

## Loading CSVs

```txt
away_team,away_score,home_team,home_score
Dallas Cowboys,20,Philadelphia Eagles,24
Kansas City Chiefs,21,Los Angeles Chargers,27
Arizona Cardinals,20,New Orleans Saints,13
Pittsburgh Steelers,34,New York Jets,32
Miami Dolphins,8,Indianapolis Colts,33
...
```

```py
import csv

# Read game data
with open("games.csv") as file:
    games = list(csv.DictReader(file))
```

<div style="font-size: 16px;">

```py
[
    { "away_team": "Dallas Cowboys", "away_score": "20", "home_team": "Philadelphia Eagles", "home_score": "24" },
    { "away_team": "Kansas City Chiefs", "away_score": "21", "home_team": "Los Angeles Chargers", "home_score": "27" },
    { "away_team": "Arizona Cardinals", "away_score": "20", "home_team": "New Orleans Saints", "home_score": "13" },
    { "away_team": "Pittsburgh Steelers", "away_score": "34", "home_team": "New York Jets", "home_score": "32" },
    { "away_team": "Miami Dolphins", "away_score": "8", "home_team": "Indianapolis Colts", "home_score": "33" },
    # ...
]
```

</div>

## Converting Numbers

```txt
away_team,away_score,home_team,home_score
Dallas Cowboys,20,Philadelphia Eagles,24
Kansas City Chiefs,21,Los Angeles Chargers,27
Arizona Cardinals,20,New Orleans Saints,13
Pittsburgh Steelers,34,New York Jets,32
Miami Dolphins,8,Indianapolis Colts,33
...
```

```py
import csv

# Read game data
with open("games.csv") as file:
    games = list(csv.DictReader(file))

# Convert scores from strings to numbers
for game in games:
    game["away_score"] = int(game["away_score"])
    game["home_score"] = int(game["home_score"])
```

<div style="font-size: 16px;">

```py
[
    { "away_team": "Dallas Cowboys", "away_score": 20, "home_team": "Philadelphia Eagles", "home_score": 24 },
    { "away_team": "Kansas City Chiefs", "away_score": 21, "home_team": "Los Angeles Chargers", "home_score": 27 },
    { "away_team": "Arizona Cardinals", "away_score": 20, "home_team": "New Orleans Saints", "home_score": 13 },
    { "away_team": "Pittsburgh Steelers", "away_score": 34, "home_team": "New York Jets", "home_score": 32 },
    { "away_team": "Miami Dolphins", "away_score": 8, "home_team": "Indianapolis Colts", "home_score": 33 },
    # ...
]
```

</div>

## Review Dictionaries

---

## Modulo and Floor Division

```py
n = 123456

print(n % 100)            # 56
print(n // 100 % 100)     # 34
print(n // 10000)         # 12
```

## Modulo and Floor Division for Height

```py
inches = 76

print(inches % 12)     # 4
print(inches // 12)    # 6
```

## Modulo and Floor Division for Duration

```py
seconds = 7000

print(seconds % 60)        # 40
print(seconds // 60 % 60)  # 56
print(seconds // 3600)     # 1
```

## `abs`

```py
abs()
```

```py
abs(-5)
abs(0)
abs(5)
```

```txt
5
0
5
```

## Let's Write a Height Class

<div style="font-size: 20px">

```py
str(Height(5, 10))              # 5'10"

Height(5, 10) == Height(5, 10)  # True
Height(5, 10) <= Height(5, 10)  # True
Height(5, 10) < Height(6, 0)    # True
Height(5, 10) > Height(4, 11)   # True
Height(5, 10) <= Height(5, 10)  # True
Height(5, 10) <= Height(6, 0)   # True
Height(5, 10) >= Height(4, 11)  # True
Height(5, 10) >= Height(5, 10)  # True

Height(5, 10) + Height(1, 0)    # 6'10"
Height(5, 10) + Height(0, 1)    # 5'11"
Height(5, 10) + Height(0, 4)    # 6'02"
Height(5, 10) + Height(1, 4)    # 7'02"

Height(5, 10) - Height(1, 0)    # 4'10"
Height(5, 10) - Height(0, 1)    # 5'09"
Height(5, 10) - Height(0, 11)   # 4'11"
Height(5, 10) - Height(1, 11)   # 3'11"

Height(5, 10) * 2               # 11'08"
Height(5, 10) * 10              # 58'04"

Height(5, 10) / 2               # 2'11"
Height(5, 10) / 10              # 0'07"

-Height(5, 10)                  # -5'10"
```

</div>

---

## Fraction Class

```py
class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __repr__(self):
        return f"{self.num}/{self.den}"
```

```py
a = Fraction(7, 20)
print(a)
```

```txt
7/20
```

## `__mul__` by Int

```py
class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __repr__(self):
        return f"{self.num}/{self.den}"

    def __mul__(self, other):
        # Make `self * other` work
        return Fraction(self.num * other, self.den)
```

```py
a = Fraction(7, 20)
print(a * 3)  # Calls __mul__(a, 3)
```

```txt
21/20
```

## `__mul__` Arguments

The following two forms are equivalent

```py
a * 3
Fraction.__mul__(a, 3)
```

## `__mul__` by Fraction

```py
class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __repr__(self):
        return f"{self.num}/{self.den}"

    def __mul__(self, other):
        # Make `self * other` work
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)
```

```py
a = Fraction(7, 20)
b = Fraction(3, 2)
print(a * b)
```

```txt
21/40
```

## `isinstance`

```py
isinstance(3, int)                     # True
isinstance(3, Fraction)                # False
isinstance(Fraction(7, 20), int)       # False
isinstance(Fraction(7, 20), Fraction)  # True
```

## Generic `__mul__`

```py
class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __repr__(self):
        return f"{self.num}/{self.den}"

    def __mul__(self, other):
        # Make `self * other` work
        if isinstance(other, int):
            return Fraction(self.num * other, self.den)

        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)
```

```py
a = Fraction(7, 20)
print(a * 3)

b = Fraction(3, 2)
print(a * b)
```

```txt
21/20
21/40
```

## Other Math Methods

```py
def __add__(self, other):
    # ...

def __sub__(self, other):
    # ...

def __mul__(self, other):
    # ...

def __truediv__(self, other):
    # ...
```

## Addition Formula

<img src="assets/add-fractions-formula.png" height="320" />

```txt
self.num   other.num   self.num * other.den + other.num * self.den
──────── + ───────── = ───────────────────────────────────────────
self.den   other.den               self.den * other.den
```

## Simplification

```py
a = Fraction(5, 20)
```

```txt
5/20
```

```txt
1/4
```

```py
a = Fraction(3, 7)
b = Fraction(7, 6)
print(a * b)
```

```txt
1/2
```

## Greatest Common Factor (Divisor)

https://en.wikipedia.org/wiki/Euclidean_algorithm

```py
def gcd(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a
```

```py
gcd(5, 20)
gcd(12, 20)
gcd(12, 27)
```

```py
5
4
1
```

## `r` Methods

```py
a = Fraction(7, 20)
print(3 * a)
```

```txt
Traceback (most recent call last):
  File "/tmp/demo.py", line 19, in <module>
    print(3 * a)
          ~~^~~
TypeError: unsupported operand type(s) for *: 'int' and 'Fraction'
```

The following two forms are equivalent

```py
3 * a
Fraction.__rmul__(a, 3)
```

## `r` Method Implementation

"How can we rearrange the equation to put `self` on the left-hand side?"

```py
def __rmul__(self, other):
    # Make `other * self` work
    return self * other

def __radd__(self, other):
    # Make `other + self` work
    return self + other

def __rtruediv__(self, other):
    # Make `other / self` work
    return self.inverse() * other

def __rsub__(self, other):
    # Make `other - self` work
    return -1 * self + other
```

---

## Player Class

```py
class Player:
    def __init__(self, name):
        self.name = name

        # Baskets count starts at 0
        self.baskets = 0

        # Shots count starts at 0
        self.shots = 0

    def __repr__(self):
        # Example: "Avery 9/10"
        return f"{self.name} {self.baskets}/{self.shots}"
```

```py
avery = Player("Avery")
avery.baskets = 2
avery.shots = 3
print(avery)
```

```txt
Avery 2/3
```

## Team Class

```py
team = Team()

team.addPlayer("alex")
team.addPlayer("marcus")
team.addPlayer("chuck")

team.addBasket("marcus")
team.addBasket("marcus")

team.addMiss("marcus")
team.addMiss("alex")
team.addMiss("chuck")

team.removePlayer("chuck")

print(team)
```

```txt
alex 0/1
marcus 2/3
--------------------
2 players 2/4 total
```

## Team Class (continued)

```py
class Team:
    def __init__(self):
        # List of player objects, starts empty
        self.players = []

    def addPlayer(self, name):
        # Make a new player with the given name and add to team
        self.players.append(Player(name))

    def addBasket(self, name):
        # Find the player matching name and update basket and shot count
        for player in self.players:
            # Find the player with the matching name
            if player.name == name:
                # Update both shots and baskets for successful shot
                player.baskets += 1
                player.shots += 1

    def addMiss(self, name):
        # Find the player matching name and update shot count
        for player in self.players:
            # Find the player with the matching name
            if player.name == name:
                # Only update shots for unsuccessful shot
                player.shots += 1

    # ...
```

## Team Class (continued)

```py
class Team:
    # ...

    def removePlayer(self, name):
        # Make a list to store the filtered players
        newPlayers = []

        for player in self.players:
            # Add player to the new list if player's name isn't the one
            # we're trying to remove
            if player.name != name:
                newPlayers.append(player)

        # Swap in new players list
        self.players = newPlayers

    # ...
```

## Team Class (continued)

```py
class Team:
    # ...

    def __repr__(self):
        # Number of players
        numPlayers = len(self.players)

        # Use to count total baskets
        totalBaskets = 0

        # Use to count total shots
        totalShots = 0

        # Use to build string representation
        result = ""

        for player in self.players:
            # Calls player __repr__ method and add newline
            result += f"{player}\n"
            # Add players stats to totals
            totalBaskets += player.baskets
            totalShots += player.shots

        # Add divider line
        result += "-" * 20
        # Add row with summary information
        result += f"\n{numPlayers} players {totalBaskets}/{totalShots} total"
        return result
```

## To Do App

Interactve demo

```py
todo = TodoList()

todo.add("do homework")
todo.add("feed dog")
todo.add("water plants")
todo.finish("feed dog")
todo.remove("do homework")

print(todo)
```

```txt
Should print:

[x] feed dog
[ ] water plants
--------------------
2 tasks, 1 undone
```

## To Do Code

```py
class Task:
    def __init__(self, name):
        # ...

    def __repr__(self):
        # ...

class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, name):
        # ...

    def finish(self, name):
        # ...

    def remove(self, name):
        # ...

    def __repr__(self):
        # ...
```

## Filtering a List

- Make an empty list
- Iterate over the items in the original list
- Choose which items to add to the new list
- Swap out the new list for the old one

---

## Functions Review

https://www.w3schools.com/python/python_functions.asp

```py
def greeting(name, school):
  return f"Hello {name} from {school}!"

print(greeting("Avery", "gfs")) # "Hello Avery from gfs!"
```

Early returns

```py
def smallest(a, b):
  if a < b:
    return a

  return b

print(smallest(3, 4))
```

## Object Oriented Programming

Objects are **data** + **functionality**.

```py
nums = [1, 2, 3, 4]
print(nums)          # [1, 2, 3, 4]
print(nums[0])       # [1]

nums.append(5)
print(nums)          # [1, 2, 3, 4, 5]

print(nums.index(2)) # 1
```

We use classes to make objects.

## Init

https://www.w3schools.com/python/python_classes.asp

```py
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
```

```py
r = Rectangle(3, 4)
print(r.width)  # 3
print(r.height) # 4
```

<img src="assets/init-meme.png" height="200" />

## Terms

- **Objects**: Structures that combine data and functionality (methods)
- **Methods**: Functions that are attached to a value
- **Classes**: The categories that objects belong to
- **Instance**: An object is an "instance" of a class if the object belongs to
  that class category
- **Fields**: Variables that are stored inside an object

## Repr

```py
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __repr__(self):
    return f"Rectangle({self.width}, {self.height})"
```

```py
r = Rectangle(3, 4)
print(r) # Rectangle(3, 4)
```

## Methods

```py
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __repr__(self):
    return f"Rectangle({self.width}, {self.height})"

  def area(self):
    return self.width * self.height

  def perimeter(self):
    return 2 * (self.width + self.height)
```

```py
r = Rectangle(3, 4)
print(r.area())      # 12
print(r.perimeter()) # 14
```

Why use methods vs extra fields?

## Mutation

```py
r = Rectangle(3, 4)
r.width = 5
print(r.area()) # ??
```

## Self

```py
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __repr__(self):
    return f"Rectangle({self.width}, {self.height})"

  def area(self):
    return self.width * self.height

  def perimeter(self):
    return 2 * (self.width + self.height)
```

The `self` variable helps us keep track of which data and functionality is
inside of the objects of our class (that is, which variables and functions are
fields and methods).

---

## More Dictionary Methods

- [`keys()`](https://www.w3schools.com/python/ref_dictionary_keys.asp)
- [`values()`](https://www.w3schools.com/python/ref_dictionary_values.asp)
- [`items()`](https://www.w3schools.com/python/ref_dictionary_items.asp)
- [`get(key, default)`](https://www.w3schools.com/python/ref_dictionary_get.asp)
- [`setdefault(key, default)`](https://www.w3schools.com/python/ref_dictionary_setdefault.asp)
- [`pop(value)`](https://www.w3schools.com/python/ref_dictionary_pop.asp)

https://docs.python.org/3/library/stdtypes.html#dict

https://www.w3schools.com/python/python_ref_dictionary.asp

## `setdefault`

```py
votes = { "strawberry": 1, "chocolate": 1, "vanilla": 1 }
votes.setdefault("mint", 0)
votes.setdefault("vanilla", 0)
```

```py
{ 'strawberry': 1, 'chocolate': 1, 'vanilla': 1, 'mint': 0 }
```

## Using `setdefault`

```py
votes = { "strawberry": 1 }

while True:
  flavor = input("Enter for your favorite flavor: ")

  if flavor in votes:
      votes[flavor] += 1
  else:
      votes[flavor] = 1

  print(votes)
```

```py
votes = { "strawberry": 1 }

while True:
    flavor = input("Enter for your favorite flavor: ")
    votes.setdefault(flavor, 0)
    votes[flavor] += 1
    print(votes)
```

## `get`

```py
votes = { "strawberry": 7 }

votes.get("strawberry", 0) # 7
votes.get("banana", 0)     # 0
```

## Using `get`

```py
votes = { "strawberry": 1 }

while True:
  flavor = input("Enter for your favorite flavor: ")

  if flavor in votes:
      votes[flavor] += 1
  else:
      votes[flavor] = 1

  print(votes)
```

```py
votes = { "strawberry": 1 }

while True:
    flavor = input("Enter for your favorite flavor: ")
    votes[flavor] = votes.get(flavor, 0) + 1
    print(votes)
```

## Scrabble Best Alphabet

Use more dictionaries!

`bestWords`

```ptls
{
  'c': 'contemptuously',
  'i': 'inquisitively',
  'd': 'difficulty',
  't': 'thoughtfully',
  'r': 'refreshments',
  ...
}
```

`bestScores`

```ptls
{
  'c': 23,
  'i': 28,
  'd': 22,
  't': 25,
  'r': 20,
  ...
}
```

## Challenge: Scrabble Lookup

```txt
Enter letters: football
['football', 'tablespoonful']
tablespoonful
20
```

---

## Dictionaries

A dictionary is a collection of key/value pairs that allows us to look up the
value associated with each key.

https://runestone.academy/ns/books/published/fopp/Dictionaries/toctree.html?mode=browsing

```py
votes = { "strawberry": 1, "chocolate": 1, "vanilla": 1 }
```

## Look up a value

```py
votes = { "strawberry": 1, "chocolate": 1, "vanilla": 1 }
```

```py
votes["strawberry"] # 1
```

## Add a value

```py
votes = { "strawberry": 1, "chocolate": 1, "vanilla": 1 }
votes["mint"] = 1
```

```py
{ "strawberry": 1, "chocolate": 1, "vanilla": 1, "mint": 1 }
```

## Update a value

```py
votes = { "strawberry": 1, "chocolate": 1, "vanilla": 1 }
votes["strawberry"] = 2
```

```py
{ "strawberry": 2, "chocolate": 1, "vanilla": 1 }
```

A dictionary can only contain a single entry for a given key.

## Increment a value

```py
votes = { "strawberry": 1, "chocolate": 1, "vanilla": 1 }
votes["chocolate"] += 1
```

```py
{ "strawberry": 1, "chocolate": 2, "vanilla": 1 }
```

## Iterate over keys

```py
for flavor in votes:
    print(flavor, votes[flavor])

# Prints:
#
# strawberry 2
# chocolate 2
# vanilla 1
# mint 1
```

## Check membership

```py
"mint" in votes # True
"pineapple" in votes # False
```

## Ice cream flavor voting

```py
votes = { "strawberry": 1 }

while True: # Loop forever
  flavor = input("Enter for your favorite flavor: ")

  if flavor in votes:
      votes[flavor] += 1 # Increase vote count by one
  else:
      votes[flavor] = 1 # Set initial vote count to one

  print(votes) # Print out vote data after each new vote
```

## Scrabble

![](scrabble.webp)

## Scrabble Points

```txt
a:  1, b:  3, c:  3, d:  2, e:  1, f:  4, g:  2, h:  4,
i:  1, j:  8, k:  5, l:  1, m:  3, n:  1, o:  1, p:  3,
q: 10, r:  1, s:  1, t:  1, u:  1, v:  4, w:  4, x:  8,
y:  4, z: 10
```

## Alice in Wonderland

```txt
chapter i down the rabbit hole alice was beginning to get very tired
of sitting by her sister on the bank and of having nothing to do once
or twice she had peeped into the book her sister was reading but it
had no pictures or conversations in it and what is the use of a book
thought alice without pictures or conversations so she was
considering in her own mind as well as she could for the hot day made
her feel very sleepy and stupid whether the pleasure of making a
daisy chain would be worth the trouble of getting up and picking the
daisies when suddenly a white rabbit with pink eyes ran close by her
there was nothing so very remarkable in that nor did alice think it
so very much out of the way to hear the rabbit say to itself oh dear
oh dear i shall be late when she thought it over afterwards it...
```

## Scrabble Best Word

You can use a `for` loop to loop over the characters in a string.

```py
word = "chapter"

for c in word:
  print(c)

# Prints:
#
# c
# h
# a
# p
# t
# e
# r
```

---

## Inverted

<img width="450" src="images/bird.png" />
<img width="450" src="images/inverted/inverted.png" />

## Greenish

<img width="450" src="images/bird.png" />
<img width="450" src="images/greenish/greenish.png" />

## Challenge: Scaled

<img width="300" src="images/bird.png" />
<img width="600" src="images/bird.png" />

## Challenge: Ascii

<div style="font-size: 11px !important; font-weight: bold;">

````````````````````````````````````````txt
 ```````````````````````````````````````--~~---'''``'~~~:~-```   ```````````````
```````````````````````````````````'-+eOEEEEEEEEOOOOEEEEEEEOec+~`` `````````    ``````
``````````````````````````````'~<cOEEEEEEEEEEEEEEEEEEOEEEEEEEEEEOc~````````````````````
````````````````````````````-+eOEEEEEEEEOEEOOEOOOOOOOOOOOOEEEEEEEEEO<-````````````````     `
``````````````````````````:cOOOOEEEEEEEEEEOeOOOEOOOOOOOOEEOOOOEEEEEEEEe:``````````````````````
```````````````````````':ceeOEEEEEEOOOOOOOOOOOOOOOeeeeceOOOOOOOEEEEEEEEEO-````````````````````
``````````````````````~ceOOEEEEEEEEEEOeeOOec<+::::~~~~:::+ceeOOOOOOOOOEEEE:```````  ``    ``
````````````````````'+OEEEEEEEEEEEEEOOOOO<:~--''-'''''''''-::+ceOOOOOOOOOOO-``````
```````````````````-eEEEEEEEEEEEEEEOOOOe+~---''''''''''''''''''-~+ceOOOOOOO+``````
``````````````````~OEEEEEEEEEEEEEEEOOec+~-----'''''''``'''```''''''-~<eeOEE<'``````
`````````````````:OEEEEEEEEEEEEEEEOOe<+::~~-~~--''''''`````````''''''--~+cOc:``````` `
````````````````:EEEEEEEEEEEEEEEEOOec<+++::~~~--''`'''````````'''''''-----:OE~```````` ``
```````````````+EEEEEEEEEEEEEEEEEOOec<<<+::~~~~---''``````````'''''''-----~+O+````````````
`````````````-eEEEEEEEEEEEEEEEEEEEOec<++::~~~~~~---'''``''````''''--------~~<<'```````````
````````````:OEEEEEEEEEEEEEEEEEEEOc<+:::~~~~~~~~--'-'```'''''`''''------~~~~+<-````````````
```````````+EEEEEEEEEEEEEEEEEEEOe<++:::~~~~~~~~~--'---'``````''''-------~~~:+cc+'`````````
`````````'<EEEEEOec<<cOEEEOOOOec<<++:::~~~~:::++++<ccc<<:--''''''-------~~:++cee~````````
`````````<EEEEOcceeee+-~<eeeccc<<+++::~~~~:+cccc<<<<+<+<eOec+:~----------~:+<<:'```````
````````:EEEEc~:++<<eEO:-:cecccc<+::::~:::+<<<++++:::~~-~cOOOec+:~-~~~~-~~~:++-'````
`````'`'cEEEE+--:::~-<Ec:+<OOcc<<::~~~~~:+c++<<ceeecc<cc+~~<cccc<:~~~~~~~~~::-```
```````-eEEEEc'-::~-'-ce+<cOOec+++:~~----+c:+<ceceOe<'`:Oe<:+cc<+~:::++<cceeec'``
```````~OEEEEE~-+~~~:cEO+~+eOe<++<:~~--''~+----<<+cee~``:cee<<:-'-:<ceOOEEOOOE~
```````-cEEEEEc~+'~~~:c+`'~<ecc<+<<::~--'~:``''~+<<<+~~~~::::~~'`'+OOeeecc++c+`
``````'`-<EEEEE+<-``'~cc'':+cccc<cc<+:~---+````'''-~~~~~~-'-----'':cOe<:-<Oc-
'````````':eEEEe:<<+-~<<::+<<<<<cccc<+:~~-+-'```''-~~~~~-''''-~~''-:<eec`~e-
``'`'`````'+OeOEc~+<:~--~+<<+++<<ccc<<+::~:+-''''''``````''''-~-'`-::+<+:~`
```````-+cOEOc<cEO:~-----:<<<<++<<cc<<+:::~<:---'````````-------``-++:+e:
`''-:<eOEEOEEO<+cEEOeceOe+c<<<+++<<cc<++::::c~~-''`````'~~~~~~-'``-:c<++`
<ceOEEOOOOOOOEe+:+<eeeeEecc<<<<++++<<<+::~~~:c~--'''--~::~--:~-'``-~:++:`
OOOOOOOOOOOOOOEe+:~--':OOccc<<++++++<<++:~~~~~c+---~~-:<+:~~::-'`'-~::+-            ``
OOOOOOOOOOOOOOeOe+~--'~OOeecc<+++::++++++++:~~~<<~~-'`~eOEEOOOc+:::+++~           `'`
OOOOOOOOOOOOOOe-ee+~-'~OOOeecc<++:::::++::++++:-+e:-'''-:<eEEEEOecc<<~         `''`
OOOOOOOOOOOOOOO~`ec:---eOOOOeec<+:::::::~~~~~:<ccOOe<:~-~~:eEEEEe<<c-        `'`
OOOOOOOOOOOOOOOe``c<~--<OOEEOOec<+:::::~~-----~:<eOEEEOeec<cOEEOc<<'     ``''`
OOOOOOOOOOOOOOOO< 'e+~-:OOEEEEOec<++::::~~~~~::+++ceOOOOc++:eOOec<'``'--''`
OOOOOOOOOOOOOOOOO- -e+~~eeOEEEEOOe<++++:::::~~--~~~~:+<eOOeeOEEOe<++~'`
OOOOEOOOOOOOOOOOOe` -e+:<eeOEEEEEOec<<<++++:~~~~::++:::::+<cOEEe`
OOOOEOOOOOOOOOOOOE+  ~e++eeOEEEEEEEOeec<++::::~:::+<ceeOeecccee~
OOOOOEOOOOOOOOOOOOO-  ~e<eOOEEEEEEEEEOOec<+:~----'''-~:+<ceccc+
OOOOOEOOOOOOOOOOOOEc   ~eeOOOEEEEEEEEEEEEOec+:~---''--~~~:+ce:`
OOOOOEOOOOOOOOOOOOOO-   ~eOOOEEEEEEEEEEEEEEEOec<+:::::::++++'
OOOOOOOOOOOOOOOOOOOE<````~OOOEEEEEEEEEEEEEEEEEEEEOOOOeccc+'
OOOOOOEOOOOOOOOOOOOOO'````:OOEEEEEEEEEEEEEEEEOe<++:+<<+:'`
OOOOOOEOOOOOOOOOOOOOE:```'-cEEEEEEEEEEEEEOc:-``
OOOOOOEOOOOOOOOOOOOOE<``'-~+eEEEEEEEEEO<~````````````
OOOOOOEEOOOOOOOOOOOOOO-''-~+eOEEEEOe<~```````````````
OOOOOOEEOOOOOOOOOOOOOO+-~~:+cOOEOO-````````````````````
OOOOOOEEOOOOOOOOOOOOOEc''-~+<cOEOE:``-c~````````````````
OOOOOOOEOOOOOOOOOOOOOOO'``'-~<OEOE<`<EE-```````````````````
OOOOOOOEOOOOOOOOOOOOOOO~```':eEOEEeeEEc`````````````````````
OOOOOOOEOOOOOOOOOOOOOOE:``~cOEOEEEEEEE-`````````````````````````
OOOOOOEEOOOOOOOOOOOOOOE<:eeeOOEEEEEEEc``````````````````````````
OOOOOOOEOOOOOOOOOOOOOOOOEOeOOEEEEEEEE~````````````````````````````
OOOOOOEEOOOOOOOOOOOOOOOOOeeOEEEEEEEEe`````````````````````````````` `
'cOOOOEEEOOOOOOOOOOOOOOOOeeeEEEEEEEE:``````````````````````````````````
````````````````````````````````````````

</div>

<img width="300" src="images/ascii/dali.webp" style="position: absolute; top: 0; right: 0;" />

---

## Image Coordinates

![](assets/pixel-coordinates.png)

- Zero-indexed
- [Top-left origin](https://dsp.stackexchange.com/questions/35925/why-do-we-use-the-top-left-corner-as-the-origin-in-image-processing)

## Pixels

![](images/bird.png)

## Subpixels

<img height="300" src="assets/Pixel_geometry_01_Pengo.jpg" />
<img height="300" src="assets/Cone-fundamentals-with-srgb-spectrum.svg" />

## Color Channels

![](assets/Rgb-raster-image.png)

- `(r, g, b)` notation
- https://rgbcolorpicker.com/

## Color Intuition

![](assets/the_dress.jpg)

## Impossible Colors

<img height="550" src="assets/eclipse-shrink.svg" />

## Colors Worksheet

<img height="450" src="assets/checker_shadow_illusion.png" />

## PIL / Pillow

https://pillow.readthedocs.io/en/stable/reference/Image.html

```py
from PIL import Image

# Load input image
im = Image.open("bird.png")

# Make blank output image with same dimension as the original
output = Image.new(im.mode, (im.width, im.height))

for y in range(im.height):
  for x in range(im.width):
    (r, g, b) = im.getpixel((x, y))

    # Your code goes here

    output.putpixel((x, y), (r, g, b))

# Save output image
output.save("grayscale.png")
```

## Tuples

```py
(r, g, b) = im.getpixel((x, y))
```

```py
color = im.getpixel((x, y))

# ...

(r, g, b) = color
```

## Max Red Demo

```py
r = 255
```

## Simple Grayscale

<img width="450" src="images/bird.png" />
<img width="450" src="images/grayscale/grayscale.png" />

- https://en.wikipedia.org/wiki/Grayscale
- `r`, `g`, and `b` are all equal
- $$l = \frac{r + g + b}{3}$$

## Better Grayscale

<img width="450" src="images/bird.png" />
<img width="450" src="images/better-grayscale/better-grayscale.png" />

- Relative / perceptual luminance
- https://brandonrohrer.com/convert_rgb_to_grayscale.html

Linear approximation for gamma-compressed channel values:

$$l = 0.299 \cdot r + 0.587 \cdot g + 0.114 \cdot b$$

## Black and White

<img width="450" src="images/bird.png" />
<img width="450" src="images/black-white/black-white.png" />

- Black `(0, 0, 0)`
- White `(255, 255, 255)`

---

## Images Preview

## Python Review

---

## Demo Projects

- Orbits
- Images
- Football

## What is CS2

- Practical, project based, applications
- Data focused

## Grading policy

[Link](../shared/grading.md)

## Python setup

Idle:

- [Idle](https://www.python.org/downloads/)

VSCode:

- [VSCode](https://code.visualstudio.com/)
- [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Review

- Define a variable
- Print out `Hello <name>` based on the value in the variable `name`
- Get a name string from the user as input and print out `Hello <name>`
- Get input from the user
- Convert a string to a number

## Dog Years
