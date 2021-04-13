import pygame
from views.game_over_view import GameOverView

class GameOverController():
    """ Controller to manage the game over screen """

    def run(self, window):
        view = GameOverView(window)
        view.display()

        displaying = True
        while displaying:
            for event in pygame.event.get():
                
                if event.type == pygame.locals.QUIT:
                    displaying = False
                    return False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if view.btn_continue.collidepoint(event.pos):
                        window.fill((46,139,87))
                        displaying = False
                        return True

                    if view.btn_end.collidepoint(event.pos):
                        displaying = False