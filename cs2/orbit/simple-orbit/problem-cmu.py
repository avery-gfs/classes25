import math
from cmu_graphics import *
app.width = 600 
app.height = 600

class Planet:
    def __init__(self, x, y, vx, vy, mass):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.ax = 0
        self.ay = 0

        radius = 2 * mass**0.3
        self.shape = Circle(self.x, self.y, radius, fill="orange")

    def updateAcceleration(self):
        pass

    def move(self):
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy

        self.shape.centerX = self.x
        self.shape.centerY = self.y

background = Rect(0, 0, 600, 600, fill='black')

sun = Planet(300, 300, 0, 0, 1000)
planet = Planet(100, 300, 0, -1.5, 20)

def onStep():
    planet.updateAcceleration()
    planet.move()

cmu_graphics.run()