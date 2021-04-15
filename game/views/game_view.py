import pygame
from models.player import Player

class GameView:
    """ GameView class displays what is seen to the player """
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.window = pygame.display.set_mode((800, 800))
        self.surface = pygame.Surface((800,800))
        


    def display(self, snake, apple, poison, score):
        """ Show the game screen and objects """
        self.surface.fill((46,139,87))

        # Snake
        for part in snake.full_body:
            pygame.draw.rect(self.surface, (255, 241, 0), part.rect)
    
        # Snake's eyes
        pygame.draw.circle(self.surface, (1, 1, 1), snake.eyes_pos[0], 4)
        pygame.draw.circle(self.surface, (1, 1, 1), snake.eyes_pos[1], 4)
        self.window.blit(self.surface.convert(), (0, 0))

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
        score_text = font.render("Score: " + str(score), True, (255,255,255))
        self.window.blit(score_text, (10, 10))
    
        pygame.display.flip()





