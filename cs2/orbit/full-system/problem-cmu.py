import math 
from cmu_graphics import * 
class Planet:
    def __init__(self, x, y, vx, vy, mass):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.ax = 0
        self.ay = 0
        radius = 2 * self.mass**0.3 
        self.shape = Circle(x,y,radius,fill = 'orange')

    def updateAcceleration(self):
        # Calculate acceleration from gravity equation
        self.ax = 0
        self.ay = 0
        for planet in planets:
            if planet == self:
                continue
            dx = planet.x - self.x 
            dy = planet.y - self.y 
            r = math.sqrt(dx**2 + dy **2)
            self.ax += (dx * planet.mass) / r**3
            self.ay += (dy * planet.mass) / r**3

    def move(self):
        # Update position and velocty based on acceleration
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy

        self.shape.centerX = self.x 
        self.shape.centerY = self.y

background = Rect(0, 0, 600, 600, fill='black')

planets = [
    Planet(300, 300, 0.012, -0.0432, 1000),
    Planet(300, 400, -2.4, 0, 5),
    Planet(550, 300, 0, 2, 20),
    Planet(565, 300, 0, 3.2, 1),
]

# L1 Lagrange Point

# planets = [
#     Planet(300, 300, 0, 0, 1000),
#     Planet(550, 300, 0, 2, 20),
#     Planet(??, ??, ??, ??, 0.1),
# ]

def onStep():
    for planet in planets:
        planet.updateAcceleration()
        planet.move()

cmu_graphics.run()