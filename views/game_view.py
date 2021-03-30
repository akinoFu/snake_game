import pygame

class GameView:
    def __init__(self, snake):
        pygame.init()
        pygame.font.init()
        self.window = pygame.display.set_mode((1000, 1000))
        self.snake = snake
        self.window.fill((46,139,87))

    def display(self):
        self.window.fill((46,139,87))
        for part in self.snake.full_body:
             self.window.blit(part.surface, (part.x, part.y))

        pygame.display.flip()


if __name__ == "__main__":
    view = GameView()

    while True:
        view.display()
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                exit()