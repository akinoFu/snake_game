import pygame

class GameOverView:
    def __init__(self, window):
        self._window = window
        self._win_w = window.get_width()
        self._win_h = window.get_height()
        self.width = self._win_w * 0.8
        self.height = self._win_h * 0.8
        self.surface = pygame.Surface((self.width, self.height))

        self.surface_pos = [self._win_w * 0.1, self._win_h * 0.1]                # [x, y]  
        self._button_size = [self.width * 0.2, self.height * 0.2]                # [width, height]
        self._img = pygame.image.load("game_over.png")
        


    def display(self):
        self.surface.fill((218, 197, 45))

        btn_font = pygame.font.SysFont('Ariel Rounded MT', 30)

        # Game Over position
        img_rect = self._img.get_rect(center = (self._win_w/2, self._win_h/3))
        
        # Restart button
        start_rect_pos = [self.width * 0.2, self.height * 0.7]
        continue_rect = pygame.draw.rect(self.surface, (1, 1, 1), (start_rect_pos[0], start_rect_pos[1], self._button_size[0], self._button_size[1]))
        text_continue = btn_font.render("Restart", True, (255, 255, 255))
        text_cotinue_rect = text_continue.get_rect(center=(continue_rect.center[0] + self._win_w * 0.1,
                                                           continue_rect.center[1] + self._win_h * 0.1))

        # End button
        end_rect_pos = [self.width * 0.6, self.height * 0.7]
        end_rect = pygame.draw.rect(self.surface, (1, 1, 1), (end_rect_pos[0], end_rect_pos[1], self._button_size[0], self._button_size[1]))
        text_end = btn_font.render("End", True, (255, 255, 255))
        text_end_rect = text_end.get_rect(center=(end_rect.center[0] + self._win_w * 0.1,
                                                  end_rect.center[1] + self._win_h * 0.1))
        
        self._window.blit(self.surface, (self.surface_pos[0], self.surface_pos[1]))
        self._window.blit(self._img, img_rect)
        self._window.blit(text_continue, text_cotinue_rect)
        self._window.blit(text_end, text_end_rect)

        pygame.display.flip()
