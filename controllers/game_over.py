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
                    if (view.start_btn_pos[0] + view.surface_pos[0]) <= x <= (view.start_btn_pos[0] + view.surface_pos[0] + view.button_size[0]) \
                       and (view.start_btn_pos[1] + view.surface_pos[1]) <= y <= (view.start_btn_pos[1] + view.surface_pos[1] + view.button_size[1]):
                        window.fill((46,139,87))
                        displaying = False
                        return True

                    elif (view.end_btn_pos[0] + view.surface_pos[0]) <= x <= (view.end_btn_pos[0] + view.surface_pos[0] + view.button_size[0]) \
                       and (view.end_btn_pos[1] + view.surface_pos[1]) <= y <= (view.end_btn_pos[1] + view.surface_pos[1] + view.button_size[1]):
                        displaying = False
                        return False