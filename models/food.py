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
        self.rect.x = round(random.randrange(100, 600))
        self.rect.y = round(random.randrange(100, 600))


    def overlap_snake_poison(self, snake, poison):
        """ Checks to see if snake head intercepts area of apple and if poison collides with apple, if this happens, it changes coordinates of apple """
        if self.rect.x <= snake[0] <= self.rect.x + 40 and self.rect.y <= snake[1] <= self.rect.y + 65:
            self.rect.y = round(random.randrange(100, 600))
            self.rect.x = round(random.randrange(100, 600))
        if self.rect.colliderect(poison.rect):
            if self.rect.x + 80 < 750:
                self.rect.x += 80
            else:
                self.rect.x -= 95
            if self.rect.y + 95 < 750:
                self.rect.y += 95
            else:
                self.rect.y -= 95
        return True


    def overlap_snake_apple(self, snake):
        """ Checks to see if whole snake overlaps apple's coordinates, if it does, it changes apples coordinates """
        if self.rect.x <= snake['x_min'] and snake['x_max'] <= self.rect.x + 40 and self.rect.y <= snake['y_min'] and snake['y_max'] <= self.rect.y + 65:
            print('in snake overlap')
            if self.rect.x + 80 < 750:
                self.rect.x += 80
            else:
                self.rect.x -= 80
            if self.rect.y + 95 < 750:
                self.rect.y += 95
            else:
                self.rect.y -= 95



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