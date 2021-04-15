import pygame
import itertools
import pygame.locals
from models.snake import Snake
from models.food import Apple, Poison
from models.player import Player
from views.game_view import GameView
from .game_over import GameOverController
from .game_start import GameStartController


class GameController():
    def __init__(self):
        self.snake = Snake()
        self.view = GameView()
        self.apple = Apple()
        self.poison = Poison()
        self.player = Player()
        self.gameover = GameOverController()
        self.gamestart= GameStartController()


    def run(self):
        """ Run the game """
        clock = pygame.time.Clock()
        running = True

        # Show start screen and get the player's name
        players_name = self.gamestart.run(self.view.window)
        if not players_name:
            running = False
        else:
            self.player.name = players_name

        while running:
            clock.tick(20)

            # Show the game screen
            self.view.display(self.snake, self.apple, self.poison, self.player.score)

            eaten_apple = self.apple.apple_eaten(self.snake._head)
            if eaten_apple:
                self.snake.add_body()
                self.player.add_point()
            
            check_poison_overlap_apple = self.apple.overlap_poison_with_apple(self.poison)
            overlap_double_check_apple = self.apple.overlap_snake_new_apple(self.snake.range)

            if overlap_double_check_apple == False:
                overlap_double_check_apple = overlap_double_check_apple(self.apple.overlap_snake_new_apple(self.snake.range))
                
            overlap_snake = self.poison.poison_eaten(self.snake.head_position)
            if overlap_snake == True:
                # Ask the player to continue
                if not self._game_restart():
                    running = False

            # When the snake hits the wall
            if self.snake.check_hit_wall(self.view.window):
                # Ask the player to continue
                if not self._game_restart():
                    running = False

            # Catch the event
            for event in pygame.event.get():
                # If the window is closed 
                if event.type == pygame.locals.QUIT:
                    running = False

                # If the direction keys are typed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.locals.K_RIGHT:
                        self.snake.turn("Right")
                    elif event.key == pygame.locals.K_LEFT:
                        self.snake.turn("Left")
                    elif event.key == pygame.locals.K_UP:
                        self.snake.turn("Up")
                    elif event.key == pygame.locals.K_DOWN:
                        self.snake.turn("Down")

            # Move the snake
            self.snake.move()

            pygame.display.update()


    def _game_restart(self):
        """
        Send the score to the server, and ask the player to continue
        """
        # Send the score to the server
        self.player.post_score()
        # Show the gameover screen
        game_continue = self.gameover.run(self.view.window, self.player)
        # If restarting the game, recreate snake and gameview
        if game_continue:
            self.snake = Snake()
            self.view = GameView()
            return True
        else:
            return False
