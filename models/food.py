import itertools
import pygame
import random
import pygame.locals


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load('apple.png')
        self.image = pygame.transform.scale(image, (40, 65))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = round(random.randrange(0, 1000) / 10.0) * 10.0
        self.rect.y = round(random.randrange(0, 1000) / 10.0) * 10.0


    def update(self):
        self.rect.y = round(random.randrange(0, 1000) / 10.0) * 10.0
        self.rect.x = round(random.randrange(0, 1000) / 10.0) * 10.0


class Poison(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load('poison.png')
        self.image = pygame.transform.scale(image, (40, 65))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = round(random.randrange(0, 1000) / 10.0) * 10.0
        self.rect.y = round(random.randrange(0, 1000) / 10.0) * 10.0


    def update(self):
        self.rect.y = round(random.randrange(0, 1000) / 10.0) * 10.0
        self.rect.x = round(random.randrange(0, 1000) / 10.0) * 10.0