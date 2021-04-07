import itertools
import pygame
import random
import pygame.locals
from models.snake import Snake


class Apple(pygame.sprite.Sprite):
    """ Apple Class that defines Snake's food that helps it grow """
    def __init__(self):
        super().__init__()
        image = pygame.image.load('apple.png')
        self.image = pygame.transform.scale(image, (40, 65))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = round(random.randrange(100, 900) / 10.0) * 10.0
        self.rect.y = round(random.randrange(100, 900) / 10.0) * 10.0


    def overlap(self, snake):
        """ Checks to see if snake head intercepts area of apple """
        if self.rect.x <= snake[0] <= self.rect.x + 40 and self.rect.y <= snake[1] <= self.rect.y + 65:
            self.rect.y = round(random.randrange(100, 600))
            self.rect.x = round(random.randrange(100, 600))
            return True



class Poison(pygame.sprite.Sprite):
    """ Poison class that defines Snake's food that kills it """
    def __init__(self):
        super().__init__()
        image = pygame.image.load('poison.png')
        self.image = pygame.transform.scale(image, (40, 65))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = round(random.randrange(100, 600))
        self.rect.y = round(random.randrange(100, 600))


    def overlap(self, snake):
        """ Checks to see if snake's head overlaps with any part of poison's area """
        if self.rect.x <= snake[0] <= self.rect.x + 40 and self.rect.y <= snake[1] <= self.rect.y + 65:
            return True