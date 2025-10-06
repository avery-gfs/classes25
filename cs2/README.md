<!-- circle rectangle square height duration instanceof -->

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
```

Linus:

> When we make an object in Python and assign it to a variable, we can use that
> variable name to access the fields and methods of the object. For example, if
> we made a new `Point` object `p = Point(5, 0)` then we can access `p.x`,
> `p.y`, `p.distanceTo(...)`, etc. **But** when we write methods for the `Point`
> class, we don't know ahead of time what our point variable going to be named,
> so we have to use the special placeholder name `self` instead.

Avery:

> `self` is a design flaw.

---

## More Dictionary Methods

- [`keys()`](https://www.w3schools.com/python/ref_dictionary_keys.asp)
- [`values()`](https://www.w3schools.com/python/ref_dictionary_values.asp)
- [`items()`](https://www.w3schools.com/python/ref_dictionary_items.asp)
- [`get(key, default)`](https://www.w3schools.com/python/ref_dictionary_get.asp)
- [`setDefault(key, default)`](https://www.w3schools.com/python/ref_dictionary_setdefault.asp)
- [`pop(value)`](https://www.w3schools.com/python/ref_dictionary_pop.asp)

https://docs.python.org/3/library/stdtypes.html#dict

https://www.w3schools.com/python/python_ref_dictionary.asp

## Get

```py
votes = { "strawberry": 7 }

votes.get("strawberry", 0) # 7
votes.get("banana", 0)     # 0
```

## Using Get

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

```py
votes = { "strawberry": 1 }

while True: # Loop forever
    flavor = input("Enter for your favorite flavor: ")

    # Increase the vote count for flavor by 1, using 0 as the default current
    # value if the flavor isn't in the votes dictionary yet
    votes[flavor] = votes.get(flavor, 0) + 1

    print(votes) # Print out vote data after each new vote
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
votes["strawberry"] # 1
```

## Add a value

```py
votes["mint"] = 1

# votes = { "strawberry": 1, "chocolate": 1, "vanilla": 1, "mint": 1 }
```

## Update a value

```py
votes["strawberry"] = 2

# votes = { "strawberry": 2, "chocolate": 1, "vanilla": 1, "mint": 1 }
```

A dictionary can only contain a single entry for a given key.

## Increment a value

```py
votes["chocolate"] += 1

# votes = { "strawberry": 2, "chocolate": 2, "vanilla": 1, "mint": 1 }
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

<div style="font-size: 9px !important; font-weight: bold;">

`````````````````````````txt
OEEEEEEEEEEEEEEEEEEEEOOc+:~~~-''''''''''`'````````'--~:<eOOEOOOOOOOOOOOOEEe-
EEEEEEEEEEEEEEEEEEEOOec+:~~~~--''''`````````````````````'~+<eOEEEEEOOOOOOOO<
EEEEEEEEEEEEEEEEEOOOec<+::~~~~-'''''````````````````````````-~+eOEEEOEEEOOec`
EEEEEEEEEEEEEEEEEOeeccc<:::::~~--''````````````     ```````````':ceeOEEEEOe<`
EEEEEEEEEEEEEEEOOOeecccc<+::+:~--'`````````````        ``````````'-':<OEEEO+
EEEEEEEEEEEEEEEOOOeeeccc<<+:+:---''`````````           ````````````'''-+OEEc:`
EEEEEEEEEEEEEEEEOOOeOec<++++:~~~-'''`````````             `````````````'-eEOEe'
EEEEEEEEEEEEEEEOOOeecc<<<+++:::~---'`````              `  ``````````````'~OEEE:
EEEEEEEEEEEEEOOeeccc<<+++++:::~~---'''```````          `````````````````''+OOE<`
EEEEEEEEEEEEOeeccccc<<+<++:+::~~--''''``````````       `````````````````''~eEOc:
EEEEEEEEEEOOeeccccc+<++<+::++:~~--''''````         `````````````````````'--<EOe:
EEEEEEEEOOOeeecc<<<++<+++++:++:~------~~'``         ```````````````'''''--~<OOc~`
EEOEOOOOOOOeeecc<++++<++<<c<ccccccceOOecc+:'```` ```   `````````````'''-~~:+Oeee<~`
OEOOOOOOOOeecccc<+<<+++<ceOOOOOOOOOOeeeeeeeOc<+~````````````````````'''-~:++ee<<eec'
OOEOOOOOOOeecc<<c<<+<<cceeeecc<<+::~-----~:eEEEOc<:-````````````````''-~~:++cc+cceO-
OOEEEOOOOeecc<++<<+<ceecceecccccccc<<+:--'-:eOOOOOOe<~'''```````````''-~~++<Oecce:`
OOEEEOOeeecc<<++++<+eecccceeeeeOOOOOOOee<:-'-+cOOeeec<+~''`'''``'``''''--:+cOEEO:``
OOEEEOOecec<+++:~::~e<+<<ceeOOOOOeee<:~+cEOc:''~cOeeeec:'''-''''''''`'''-~:cc:~-`
OOEEEOeecee<++::~~''e~~++<<<<ee+cEEEcO~  'eEEe+~~cOeec+~--~--------~~~~~~~:`
eOOEOOeeceec<+::~~--c'`-''--~cOc:+eOEO:```:eeOOecce<+~---~:::+<ccceeeeOeccc`
eeOOOOOeeOOecc<+~~-~c'````'-':eOe<+++~'''-'~eeOOec<:'```-:+ceOOOEEEEEEEEEEO:`
eeOOOOOOeOOeec<+::~~e-`````''''~+cecc<+:::~~~-~~+~:~'```':eEEOOOOOOOOOeceOE<
eeOeeOOOOOOOeec<++:~e~```````'````'''--~~-~~'`'--'--'` `-cEOOOOOeec<+:::<Oe-
eeeeeeeOOOOOOeec<+::c+'''``````''---'--~~:~'``'``'---```-:+cOOe<+~:eOe<<e+`
OeeeeeeeOOOOOeeec<<++c---''`````'-~~::~--```````'--~-'``'~~:eOOcO< `eEEc'
OeeeeeeeOOOOOeec<<<+:c+---'''`````       ```````'-~--` `'~--~<OOOc--eEc`
OeeeeeeeeOOOOeeec<<<++e~~--''`````      ```''''`'---'  `-:~~+++<+~:+:`
OeOeeeeeeeeOOecccc<<<+e<~~-~-'```````  ```''-'''---'`  `~:+:::<eeec-
Oeeeeeeeeeeeeeec<<+++:+O:~~~-''`````````-~::~-~~~-'`````~:+<<~-+eO~
Oeeeeeeeeeeeeeec<++:::~+O:---'''```'''-~:+~--~::~-'`` ``-:~cec<<<c`
OOeeeeeccceeeeec<++:::~~+O+--''''--~~~:<+~-''-:~-'``  `'-~~::++++:
OOOeeeccccceeeeccc++:::~~+O<----~~~-'-ce<+:~-~:~-'` ```'~~~~~~~~:'
OOOeeecccccccceeeecc<++~~~:Oc~~~~'```'eEOOOOOeee+~-````'~~~~~~:+~
OOOOeeccccc<c<cccccceec<:~-~ee:'''````~eOEEEEEEEOe<<+:::+::::+c~                   ``
EEOOOeeccc<<<<<<+++++<ceec+~~OO<~-''''''-:cOEEEEEEOOOeee++++<c-                 `-'
EEEOOeecc<<+<+++::~~---~<eOOeOEEOe<~-'''''~<OEEEEEEEOec<+<ce<`               `~~`
EEEEOOecc<<<<+++:~~---''-~+ceEEEEEEOe<++++:+OEEEEEEEec<ccee+              `-~'
EEEEEOOeccc<<<<++:~~---~~:+<ceOEEEEEEEEOOecceOEEEEEOecccee-            `'-'`
EEEEEOOOeeecc<<<++:::::+<<+<+<cOEEEEOOOe<+c+<OEOOOOecccec`        ``''-`
EEEEEEEOOeeecccc<<<+::~--'-~~~'-+<ceOEEOe<:~~cOEEOec<ce+    `'-~~~-'`
EEEEEEEEOOOOeeeccc<<+:~----~++:~---~:<eOEEEEOOEEEEEOOOOccc<+:-`
EEEEEEEEEOOOOeeccc<c<+::::::+<<<+::~--~~:<ceOEEEEEEOe-''``
EEEEEEEEEEEEOOOec<+<<<+~:++<<<ceOOOOeec++++<ceEEEEEc`
EEEEEEEEEEEEEEOOec<+:::~---~~~~:+<ceeOEEEOeeeeceeee`
EEEEEEEEEEEEEEEEOOec<:~-'''''````'-~:+<ceOOOec<cce'
EEEEEEEEEEEEEEEEEEOOec<+~--'''``''-----~+cccceeOe'
EEEEEEEEEEEEEEEEEEEEEOeec+:~~-----~~-~~~:++<eOO<`
EEEEEEEEEEEEEEEEEEEEEEEEOOec<<::++++:+++:~:eOc'
EEEEEEEEEEEEEEEEEEEEEEEEEEEOOOOOeeccccc<<<c:`
EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEOOOOe<-
EEEEEEEEEEEEEEEEEEEEEEEOec+:---~+<<<+:-`
EEEEEEEEEEEEEEEEEEEOc:-``
EEEEEEEEEEEEEEEEe+-```  `
EEEEEEEEEEEEOc+-````````
EEEEEEEEEEEE+``````````
EEEEEEOEEEEE+``````````
EEEEEEEEEEEEc``````````
OEEEEEEEEEEEe'```~<~````
OEEEEEEEEEEEe`':eEB+`````
EEEEEEEEEEEEc+OEEEe``````
EEEEEEEEEEEEEEEEEE-```````
EEEEEEEEEEEEEEEEE+`````````
EEEEEEEEEEEEEEEEc``````````
EEEEEEEEEEEEEEEO-```````````
`````````````````````````

</div>

<img width="300" src="images/ascii/dali.jpg" style="position: absolute; top: 0; right: 0;" />

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
