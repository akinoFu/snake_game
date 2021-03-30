import pygame

class GameOverView:
    def __init__(self, window):
        self._window = window
        self.start_btn_pos = [120, 400] # [x, y]
        self.end_btn_pos = [360, 400]   # [x, y]
        self.surface_pos = [200, 200]   # [x, y]
        self.button_size = [120, 100]   # [width, height]


    def display(self):
        gameover_surface = pygame.Surface((600, 600))
        gameover_surface.fill((255, 204, 204))
        
        title_font = pygame.font.SysFont('Ariel Rounded MT', 60)
        btn_font = pygame.font.SysFont('Ariel Rounded MT', 30)
        
        # Game Over Text
        text_game_over = title_font.render("You lost!", True, (1, 1, 1))
        
        # Restart button
        pygame.draw.rect(gameover_surface, (1, 1, 1), (self.start_btn_pos[0], self.start_btn_pos[1], self.button_size[0], self.button_size[1]))
        text_continue = btn_font.render("Restart", True, (255, 255, 255))

        # End button
        pygame.draw.rect(gameover_surface, (1, 1, 1), (self.end_btn_pos[0], self.end_btn_pos[1], self.button_size[0], self.button_size[1]))
        text_end = btn_font.render("End", True, (255, 255, 255))
        
        
        self._window.blit(gameover_surface, (self.surface_pos[0], self.surface_pos[1]))
        
        self._window.blit(text_game_over, (self.surface_pos[0] + 250, self.surface_pos[1] + 50))

        self._window.blit(text_continue, (self.surface_pos[0] + self.start_btn_pos[0] + self.button_size[0]/4
                                         , self.surface_pos[1] + self.start_btn_pos[1] + self.button_size[1]/4))

        self._window.blit(text_end, (self.surface_pos[0] + self.end_btn_pos[0] + self.button_size[0]/4
                                         , self.surface_pos[1] + self.end_btn_pos[1] + self.button_size[1]/4))
        pygame.display.flip()
