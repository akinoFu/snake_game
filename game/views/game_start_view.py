import pygame

class GameStartView:
    def __init__(self, window):
        self._window = window
        self.width = window.get_width()
        self.height = window.get_width()
        self.surface = pygame.Surface((self.width, self.height))
        # Input box
        self.input_box = pygame.Rect(self.width * 0.1,      # x
                                     self.height * 0.5,     # y
                                     self.width * 0.8,      # width
                                     50                     # height
                                    )
        # Start button
        self.start_btn = pygame.Rect(self.width * 0.3,      # x
                                     self.height * 0.7,     # y
                                     self.width * 0.4,      # width
                                     100                    # height
                                    )
        # Font
        self.font = pygame.font.SysFont("Ariel Rounded MT", 32)
        # image
        self._img = pygame.image.load("game/assets/img/game_start.png")
    

    def display(self, active):
        """ Show the start display """
        self.surface.fill((6, 75, 40))

        # Game Over logo position
        img_rect = self._img.get_rect(center = (self.width/2, self.height/4))

        # Input box label
        label = self.font.render("Enter your name", True, (255,255,255))

        # Input box
        if active:
            color = (255,255,255)
        else:
            color = (204, 204, 204)
        pygame.draw.rect(self.surface, color, self.input_box)

        # Start button
        pygame.draw.rect(self.surface, (250, 128, 114), self.start_btn)
        text_start = self.font.render("START", True, (255, 255, 255))
        text_start_rect = text_start.get_rect(center=(self.start_btn.center))

        # Draw objects on the surface
        self._window.blit(self.surface, (0, 0))
        self._window.blit(self._img, img_rect)
        self._window.blit(label, (self.input_box.x,
                                self.input_box.y - self.input_box.height))
        self._window.blit(text_start, text_start_rect)

        pygame.display.flip()
    

    def display_text(self, text):
        """ Show the text entered """
        input_text = self.font.render(text, True, (1,1,1))
        self._window.blit(input_text, (self.input_box.x + 10,
                                       self.input_box.y + self.input_box.height * 0.5))
        pygame.display.flip()
