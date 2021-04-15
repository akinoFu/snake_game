import pygame
from views.game_start_view import GameStartView
import tkinter
from tkinter import messagebox

class GameStartController():
    """ Controller to manage the game start screen """

    def run(self, window):
        """ Show the start screen and return the player name entered """
        displaying = True
        input_active = False
        text = ""

        view = GameStartView(window)
        view.display(input_active)

        while displaying:
            for event in pygame.event.get():
                # Window close
                if event.type == pygame.locals.QUIT:
                    displaying = False
                    return None

                # Catch a click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Click the input box
                    if view.input_box.collidepoint(event.pos):
                        input_active = True

                    # Click the start button
                    elif view.start_btn.collidepoint(event.pos):
                        if text.strip():
                            return text
                        else:
                            root = tkinter.Tk()
                            root.withdraw()
                            messagebox.showwarning("Warning","Enter your name")
                
                # Catch a key press
                if event.type == pygame.KEYDOWN:
                    if input_active:
                        if event.key == pygame.K_RETURN:
                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                
                # Show the screen
                view.display(input_active)

                # Show the entered text in the input box
                view.display_text(text)
