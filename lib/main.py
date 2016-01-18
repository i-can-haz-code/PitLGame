#!/usr/bin/env python3

""" 
This is the main library to be used for the PythonistoLearn Game project

So far it provides a Player class. 

"""





__credits__ = 'u/Spectrumss, u/i_can_haz_code'



import time, random, os
import pygame




class Player(pygame.sprite.Sprite):

        def __init__(self):
                """ 
                Set up the class.
                """
                self.WIDTH = 800
                self.HEIGHT = 800
                self.black = (0, 0, 0)
                self.green = (0, 255, 0)
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.Surface((50, 40))
                self.image.fill(self.green)
                self.image.set_colorkey(self.black)
                self.rect = self.image.get_rect()
                self.rect.center = (self.WIDTH /2, self.HEIGHT / 2)
                self.speedy = 0
                self.speedx = 0

        def update(self):
                """
                handle updating player position and character controller
                """
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
                if self.rect.right > self.WIDTH:
                    self.rect.right = self.WIDTH
                if self.rect.left < 0:
                    self.rect.left = 0
                if self.rect.bottom >= self.HEIGHT-200:
                    self.rect.bottom = self.HEIGHT-200
                if self.rect.top < 0:
                    self.rect.top = 0
                











