import pygame

class GameOverView:
    def __init__(self, window):
        self._window = window
        self.width = window.get_width()
        self.height = window.get_height()
        self.surface = pygame.Surface((self.width, self.height))
        
        # buttons
        btn_size = [self.width * 0.25, self.height * 0.2]    # [width, height]
        self.btn_continue = pygame.Rect(self.width * 0.2,   # x
                                        self.height * 0.7,  # y
                                        btn_size[0],        # width
                                        btn_size[1]         # height
                                    )
        self.btn_end = pygame.Rect(self.width * 0.55,        # x
                                   self.height * 0.7,       # y
                                   btn_size[0],             # width
                                   btn_size[1]              # height
                                )
        # image
        self._img = pygame.image.load("game/assets/img/game_over.png")

        # score board
        self.link_active = False
        # self.link_font = pygame.font.SysFont('Ariel Rounded MT', 40)
        # self.link_font_underline = self.link_font.set_underline

        self.scoreboard_text = None
        self.scoreboard_rect = None


    def display(self, player):
        """ Show the game over display """
        self.surface.fill((218, 197, 45))
        score_font = pygame.font.SysFont('Ariel Rounded MT', 70)
        btn_font = pygame.font.SysFont('Ariel Rounded MT', 40)
        link_font = pygame.font.SysFont('Ariel Rounded MT', 30)

        # Game Over position
        img_rect = self._img.get_rect(center = (self.width/2, self.height/3))
        
        # Score
        text_score = score_font.render(f"{player.name}'s score: {player.score}", True, (255, 255, 255))
        text_score_rect = text_score.get_rect(center=(self.width * 0.5, self.height * 0.58))

        # Scoreboard
        if self.link_active:
            font_color = (255,0,0)
        else:
            font_color = (0,0,255)
        self.scoreboard_text = link_font.render("Go to the Scoreboard", True, font_color)
        self.scoreboard_rect = self.scoreboard_text.get_rect(center=(self.width * 0.5, self.height * 0.65))

        # Restart button
        pygame.draw.rect(self.surface, (1, 1, 1), self.btn_continue)
        text_continue = btn_font.render("Restart", True, (255, 255, 255))
        text_cotinue_rect = text_continue.get_rect(center=(self.btn_continue.center))

        # End button
        pygame.draw.rect(self.surface, (1, 1, 1), self.btn_end)
        text_end = btn_font.render("End", True, (255, 255, 255))
        text_end_rect = text_end.get_rect(center=(self.btn_end.center))
        
        # Draw objects on the surface
        self._window.blit(self.surface, (0, 0))
        self._window.blit(self._img, img_rect)

        self._window.blit(self.scoreboard_text, self.scoreboard_rect)

        self._window.blit(text_score, text_score_rect)
        self._window.blit(text_continue, text_cotinue_rect)
        self._window.blit(text_end, text_end_rect)

        pygame.display.flip()


