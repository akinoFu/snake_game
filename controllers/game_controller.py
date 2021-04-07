import pygame
import itertools
import pygame.locals
from views.game_view import GameView
from models.snake import Snake
from models.food import Apple, Poison
from .game_over import GameOverController

class GameController():
    def __init__(self):
        self.snake = Snake()
        self.view = GameView(self.snake)
        self.apple = Apple()
        self.poison = Poison()


    def run(self):
        clock = pygame.time.Clock()
        running = True

        apples = pygame.sprite.Group()
        apples.add(self.apple)

        poison = pygame.sprite.Group()
        poison.add(self.poison)

        while running:
            clock.tick(30)

            self.view.display()
            
            overlap_apple = self.apple.overlap(self.snake.head_position)
            # if overlap_apple == True:
                # score += 1
            overlap_snake = self.poison.overlap(self.snake.head_position)
            if overlap_snake == True:
                gameover = GameOverController()
                game_continue = gameover.run(self.view.window)
                if game_continue:
                    self.snake = Snake()
                    self.view = GameView(self.snake)
                else:
                    running = False

            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.locals.K_RIGHT:
                        self.snake.turn("Right")
                    elif event.key == pygame.locals.K_LEFT:
                        self.snake.turn("Left")
                    elif event.key == pygame.locals.K_UP:
                        self.snake.turn("Up")
                    elif event.key == pygame.locals.K_DOWN:
                        self.snake.turn("Down")

            apples.draw(self.view.window)
            poison.draw(self.view.window)
            pygame.display.update()
            
            if self.snake.full_body[0].x < 0 \
               or self.snake.full_body[0].y < 0 \
               or self.snake.full_body[0].x > self.view.window.get_width() \
               or self.snake.full_body[0].y > self.view.window.get_height():
                    game_continue = gameover.run(self.view.window)
                    if game_continue:
                        self.snake = Snake()
                        self.view = GameView(self.snake)
                    else:
                        running = False

            self.snake.move()


if __name__ == "__main__":
    controller = GameController()
    controller.run()

