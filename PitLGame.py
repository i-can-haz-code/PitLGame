#!/usr/bin/env python3


""" 

This is the main body of the application/game logic. Classes are stored over in lib


"""

import time, os, random
import pygame
from lib.main import Player
#from lib.main import pygame



WIDTH = 800
HEIGHT = 600
FPS = 30
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)



# Setting up assets
game_folder = os.path.dirname("__file__")
# img_folder = os.path.join(game_folder, "img") <-- Use this when we make an image





pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game!")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)



running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    #Draw / Render
    screen.fill(blue)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
