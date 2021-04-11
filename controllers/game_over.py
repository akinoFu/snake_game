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
                    
                    x, y = pygame.mouse.get_pos()

                    if view.button_cotinue["x_start"] <= x <= view.button_cotinue["x_end"] \
                       and view.button_cotinue["y_start"] <= y <= view.button_cotinue["y_end"] :
                        window.fill((46,139,87))
                        displaying = False
                        return True


                    elif view.button_end["x_start"] <= x <= view.button_end["x_end"] \
                       and view.button_end["y_start"] <= y <= view.button_end["y_end"] :
                        displaying = False
                        return False