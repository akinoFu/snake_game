import pygame
import webbrowser
from views.game_over_view import GameOverView


class GameOverController():
    """ Controller to manage the game over screen """

    def run(self, window, player, post_result):
        """ Show the game over screen """
        view = GameOverView(window)

        displaying = True
        while displaying:
            view.display(player, post_result)
            
            for event in pygame.event.get():
                # Window close button
                if event.type == pygame.locals.QUIT:
                    displaying = False
                    return False

                # Mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Click the link to scoreboard
                    if view.scoreboard_rect.collidepoint(event.pos):
                        webbrowser.open('http://127.0.0.1:5000/') 

                    # Click continue button
                    if view.btn_continue.collidepoint(event.pos):
                        window.fill((46,139,87))
                        displaying = False
                        return True

                    # Click end button
                    if view.btn_end.collidepoint(event.pos):
                        displaying = False
                        return False
                
                # Mouseover the score board
                if view.scoreboard_rect.collidepoint(pygame.mouse.get_pos()):
                    view.link_active = True
                else:
                    view.link_active = False

                # Mouseover the continue button
                if view.btn_continue.collidepoint(pygame.mouse.get_pos()):
                    view.btn_continue_active = True
                else:
                    view.btn_continue_active = False
            
                # Mouseover the end button
                if view.btn_end.collidepoint(pygame.mouse.get_pos()):
                    view.btn_end_active = True
                else:
                    view.btn_end_active = False
