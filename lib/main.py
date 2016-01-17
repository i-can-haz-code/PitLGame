#!/usr/bin/env python3

""" This is the main library to be used for the PythonistoLearn Game project

So far it provides a Player class, and in comments a mock pygame class. This is intended
for developers who do not wish to install pygame. To use the mock class for development
comment out the pygame import and uncomment the pygame class below.

"""



"""
Adding the height, width and fps
"""
WIDTH = 800
HEIGHT = 800
FPS = 60


"""
making some useful colours using RGB
Add any colours you make here, so we can use them again
"""

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


__credits__ = 'u/Spectrumss, u/i_can_haz_code'



import time
import random
import os
import pygame




class Player(pygame.sprite.Sprite):

        def __init__(self):
                """ 
                Set up the class.
                """
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.Surface((50, 40))
                self.image.fill(green)
                self.image.set_colorkey(black)
                self.rect = self.image.get_rect()
                self.rect.center = (WIDTH /2, HEIGHT / 2)
                self.speedy = 0
                self.speedx = 0

        def update(self):
                """
                handle updating player position and character controller
                """
                self.speedx = 0
                self.speedy = 0
                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_LEFT]:
                        self.speedx = -7
                if keystate[pygame.K_RIGHT]:
                        self.speedx = 7
                if keystate[pygame.K_DOWN]:
                        self.speedy = 7
                if keystate[pygame.K_UP]:
                        self.speedy = -7
                self.rect.y += self.speedy
                self.rect.x += self.speedx
                if self.rect.right > WIDTH:
                                        self.rect.right = WIDTH
                if self.rect.left < 0:
                                        self.rect.left = 0


"""
initiating pygame and setting up the screen and player.
"""

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

"""
doing the game loop
"""

running = True

while running:
    # Ticking the clock - basically the fps
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()

    #Draw / Render
    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.flip()
    

pygame.quit()







