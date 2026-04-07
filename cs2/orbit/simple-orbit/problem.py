import math
import pygame

pygame.init()
# Screen is 600x600 pixels
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()


class Planet:
    def __init__(self, x, y, vx, vy, mass):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass

    def draw(self):
        # Scale formula is kinda arbitrary, for aesthetics
        radius = 2 * self.mass**0.3
        pygame.draw.circle(screen, "#ff9c7a", (self.x, self.y), radius)

    def updateAcceleration(self):
        pass

    def move(self):
        # Update position and velocty based on acceleration
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy


sun = Planet(300, 300, 0, 0, 1000)
planet = Planet(100, 300, 0, -1.5, 20)

running = True

while running:
    # Pygame makes us reinvent the wheel (game loop)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background to clear screen
    screen.fill("#111111")

    sun.draw()

    planet.updateAcceleration()
    planet.move()
    planet.draw()

    # Limit to 50 fps
    clock.tick(50)
    # Redraw game canvas
    pygame.display.flip()
