import pygame
from views.game_start_view import GameStartView
import tkinter
from tkinter import messagebox

class GameStartController():
    """ Controller to manage the game start screen """

    def run(self, window):
        
        displaying = True
        input_active = False
        text = ""

        view = GameStartView(window)
        view.display(input_active)
        
        # font = pygame.font.SysFont("Ariel Rounded MT", 32)

        while displaying:
            for event in pygame.event.get():
                
                if event.type == pygame.locals.QUIT:
                    displaying = False
                    return None

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
                
                if event.type == pygame.KEYDOWN:
                    if input_active:
                        if event.key == pygame.K_RETURN:
                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                
                view.display(input_active)
                view.display_text(text)
