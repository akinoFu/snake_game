import pygame

class GameView:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.window = pygame.display.set_mode((800, 800))
        self.window.fill((46,139,87))

    def display(self, snake):
        self.window.fill((46,139,87))
        for part in snake.full_body:
             self.window.blit(part.surface, (part.x, part.y))

        pygame.display.flip()


    def display_score(self, x, y):
        font = pygame.font.Font('freesansbold.ttf', 32)
        score = font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.window.blit(score, (x, y))


if __name__ == "__main__":
    view = GameView()

    while True:
        view.display()
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                exit()