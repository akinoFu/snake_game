import pygame
from models.player import Player

class GameView:
    """ GameView class displays what is seen to the player """
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.window = pygame.display.set_mode((800, 800))


    def display(self, snake, apple, poison, score):
        """ Show the game screen and objects """
        self.window.fill((46,139,87))

        # Snake
        snake.group.draw(self.window)


        # Score
        font = pygame.font.SysFont('Ariel Rounded MT', 50)
        score_text = font.render("Score: " + str(score), True, (255,255,255))
        self.window.blit(score_text, (10, 10))
    
        pygame.display.flip()





