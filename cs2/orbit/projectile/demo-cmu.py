import math 
from cmu_graphics import * 

class Projectile:
    def __init__(self, x, y, vx, vy, ax, ay):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        
        self.shape = Circle(x,y,10,fill = 'orange')

    def move(self):
        # Update position and velocty based on acceleration
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy

        self.shape.centerX = self.x 
        self.shape.centerY = self.y 
    
background = Rect(0, 0, 600, 600, fill='black')

proj = Projectile(50, 550, 10, -25, 0, 1)

def onStep():
    proj.move()

cmu_graphics.run()
