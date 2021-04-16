import pygame
import random
import pygame.locals


class Apple(pygame.sprite.Sprite):
    """ Apple Class that defines Snake's food that helps it grow """
    def __init__(self):
        super().__init__()
        image = pygame.image.load("game/assets/img/apple.png")
        self.image = pygame.transform.scale(image, (40, 65))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = round(random.randrange(100, 650))
        self.rect.y = round(random.randrange(100, 650))



    def apple_eaten(self, snake):
        """ Checks to see if snake head intercepts area of apple """
        if pygame.sprite.spritecollide(self, snake, dokill=True):
            self.rect.y = round(random.randrange(100, 650))
            self.rect.x = round(random.randrange(100, 650))
            return True
        return False


    def overlap_poison_with_apple(self, poisons, group):
        """ Checks to see if poison position overlaps apple position and changes apple position if it does """
        if pygame.sprite.spritecollide(self, group, dokill=True):
            if self.rect.x + 80 < 750:
                self.rect.x += 80
            else:
                self.rect.x -= 80
            if self.rect.y + 95 < 750:
                self.rect.y += 95
            else:
                self.rect.y -= 95


    def overlap_snake_new_apple(self, snake):
        """ Checks to see if snake overlaps apple's coordinates, if it does, it changes apple's coordinates """
        overlapping = True
        while overlapping:
            # If the new apple collides with snake
            if pygame.sprite.spritecollide(self, snake, dokill=True):
            # changing apple's coordinates 
                self.rect.y = round(random.randrange(100, 650))
                self.rect.x = round(random.randrange(100, 650))
            else:
                overlapping = False


class Poison(pygame.sprite.Sprite):
    """ Poison class that defines Snake's food that kills it """
    def __init__(self):
        super().__init__()
        image = pygame.image.load('game/assets/img/poison.png')
        self.image = pygame.transform.scale(image, (40, 65))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = round(random.randrange(100, 650))
        self.rect.y = round(random.randrange(100, 650))


    def poison_eaten(self, snake):
        """ Checks to see if snake's head overlaps with any part of poison's area """
        if pygame.sprite.spritecollide(self, snake, dokill=True):
            return True
