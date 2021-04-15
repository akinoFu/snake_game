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
        if self.rect.colliderect(snake.rect):
            self.rect.y = round(random.randrange(100, 650))
            self.rect.x = round(random.randrange(100, 650))
            return True
        return False
    # def apple_eaten(self, snake):
    #     """ Checks to see if snake head intercepts area of apple """
    #     if self.rect.x <= snake[0] <= self.rect.x + 40 and self.rect.y <= snake[1] <= self.rect.y + 65:
    #         self.rect.y = round(random.randrange(100, 650))
    #         self.rect.x = round(random.randrange(100, 650))
    #         return True
    #     return False

    def overlap_poison_with_apple(self, poison):
        """ Checks to see if poison position overlaps apple position and changes apple position if it does """
        if self.rect.colliderect(poison.rect):
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
            # If the apple is in the snake range
            if (snake['x_min'] <= self.rect.x <= snake['x_max'] and snake['y_min'] <= self.rect.y <= snake['y_max']) \
            or (snake['x_min'] <= self.rect.x + 40 <= snake['x_max'] and snake['y_min'] <= self.rect.y <= snake['y_max']) \
            or (snake['x_min'] <= self.rect.x <= snake['x_max'] and snake['y_min'] <= self.rect.y + 65 <= snake['y_max']) \
            or (snake['x_min'] <= self.rect.x + 40 <= snake['x_max'] and snake['y_min'] <= self.rect.y + 65 <= snake['y_max']):
            # checking the apple's coordinates to see if it overlaps with snake range
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
        if self.rect.x <= snake[0] <= self.rect.x + 40 and self.rect.y <= snake[1] <= self.rect.y + 65:
            return True
