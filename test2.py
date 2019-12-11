import pygame
from pytmx import load_pygame
import random


white = (255,255,255)


#create window
screenSize = (800,600)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("GameName")
screen.fill(white)


gameMap = load_pygame("map2.tmx")


#creates list of single tiles in first layer
images = []
for y in range(50):
    for x in range(50):
        image = gameMap.get_tile_image(x,y,0)
        images.append(image)


#displays tiles in locations
i = 0
for y in range(50):
    for x in range(50):
        screen.blit(images[i],(x*32,y*32))
        i += 1


#main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
