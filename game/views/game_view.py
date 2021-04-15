import pygame
from models.player import Player

class GameView:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.window = pygame.display.set_mode((800, 800))
        self.window.fill((46,139,87))


    def display(self, snake, apple, poison, score):
        """ Show the game screen and objects """
        self.window.fill((46,139,87))

        # Snake
        for part in snake.full_body:
             self.window.blit(part.surface, (part.x, part.y))

        # Apple
        apples = pygame.sprite.Group()
        apples.add(apple)
        
        # Poison
        poisons = pygame.sprite.Group()
        poisons.add(poison)

        apples.draw(self.window)
        poisons.draw(self.window)

        # Score
        font = pygame.font.SysFont('Ariel Rounded MT', 50)
        score_text = font.render(str(score), True, (255,255,255))
        self.window.blit(score_text, (10, 10))
    
        pygame.display.flip()





