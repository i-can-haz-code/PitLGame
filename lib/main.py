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
                bp = back_pack()

        def update(self):
                """
                handle updating player position and character controller
                """
                self.speedy = 0
                self.speedx = 0
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
                
class back_pack(object):
    """ 
    This class provides a backpack in which items can be placed.
    """
    def __init__(self,max_count=10):
        """
        This is an init method. It defines max_count and initializes holding
        """
        self.max_count = max_count
        self.holding = []

    def check_count(self):
        """
        This method checks to ensure that max_count is greater than len(self.holding)
        """
        if len(self.holding) > self.max_count:
            self.holding.pop()
            raise(ValueError)

    def add_item(self,item):
        """
        This method tries to add an item to the backpack. If it goes over the max_count
        The item is not added, and a message is shown
        """
        try:
            self.holding.append(item)
            self.check_count()
            return(True)
        except ValueError:
            print('Item {} could not be added. Sorry '.format(item))
            return(False)

    def remove_item(self,item):
        """
        Removes an item from the backpack.
        """
        try:
            self.holding.remove(item)
        except:
            print('{} not in backpack'.format(item))
    def list_items(self):
        """
        I mean... read the method name... it just prints the items
        """
        for item in self.holding:
            print(item)






