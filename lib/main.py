#!/usr/bin/env python3

""" This is the main library to be used for the PythonistoLearn Game project

So far it provides a Player class, and in comments a mock pygame class. This is intended
for developers who do not wish to install pygame. To use the mock class for development
comment out the pygame import and uncomment the pygame class below.

"""


__credits__ = 'u/Spectrumss, u/i_can_haz_code'

import time, random, os
import pygame


"""
# plz keep this mock class so people can work on stuff requireing pygame without actually
# installing it.

class pygame(object):
	def __init__(self):
		self.display = ''
		pass
	def init():
		pass
	class mixer(object):
		def __init__(self):
			pass
		def init():
			pass

	class sprite():
		def __init__(self):
			pass
		class Sprite(object):
			def __init__(self,object):
				pass

"""
WIDTH = 800
HEIGHT = 600
FPS = 30
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

class Player(pygame.sprite.Sprite):
	""" 
	Basic player class.  
	"""
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
		handle updating player position
		"""
		self.speedx = 0
		self.speedy = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speedx = -7
		if keystate[pygame.K_RIGHT]:
			self.speedx = 7
		if keystate[pygame.K_RIGHT]:
			if keystate[pygame.K_LEFT]:
				self.speedx = 0
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







