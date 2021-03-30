import random
import pygame

class Snake:
    def __init__(self):
        self._size = 20
        self._head = SnakeHead(800, 800, self._size)
        self._body1 = SnakeBody(self._head.x + self._size, self._head.y, self._size)
        self._body2 = SnakeBody(self._body1.x + self._size, self._head.y, self._size)
        self._body3 = SnakeBody(self._body2.x + self._size, self._head.y, self._size)
        self._body4 = SnakeBody(self._body3.x + self._size, self._head.y, self._size)
        self._body5 = SnakeBody(self._body4.x + self._size, self._head.y, self._size)
        self._body6 = SnakeBody(self._body5.x + self._size, self._head.y, self._size)
        self.full_body = [self._head, self._body1, self._body2, self._body3, self._body4, self._body5, self._body6]
        self.direction = "Left"
        self.score = 0

    def move(self):
        self._body6.x = self._body5.x
        self._body6.y = self._body5.y
        self._body5.x = self._body4.x
        self._body5.y = self._body4.y
        self._body4.x = self._body3.x
        self._body4.y = self._body3.y
        self._body3.x = self._body2.x
        self._body3.y = self._body2.y
        self._body2.x = self._body1.x
        self._body2.y = self._body1.y
        self._body1.x = self._head.x
        self._body1.y = self._head.y

        if self.direction == "Up":
            self._head.y -= self._size
        elif self.direction == "Down":
            self._head.y += self._size
        elif self.direction == "Right":
            self._head.x += self._size
        elif self.direction == "Left":
            self._head.x -= self._size
    
    def turn(self, direction):
        """ Change the direction """
        # Set new direction
        self.direction = direction
        # Rotate the head
        self._head.rotate(self.direction)


class SnakePart:
    def __init__(self, x, y, size):
        self._size = size
        self.x = x
        self.y = y
        self.surface = pygame.Surface((self._size, self._size))
        

class SnakeHead(SnakePart):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.rotate("Left")
    
    def rotate(self, direction):
        """ Change the position of the eyes according to the direction """
        self.surface.fill((255, 241, 0))
        if direction == "Left":
            pygame.draw.circle(self.surface, (1, 1, 1),(self._size/2,5), 4)
            pygame.draw.circle(self.surface, (1, 1, 1),(self._size/2,15), 4)
        elif direction == "Right":
            pygame.draw.circle(self.surface, (1, 1, 1),(self._size/2,5), 4)
            pygame.draw.circle(self.surface, (1, 1, 1),(self._size/2,15), 4)
        elif direction == "Up":
            pygame.draw.circle(self.surface, (1, 1, 1),(5, self._size/2), 4)
            pygame.draw.circle(self.surface, (1, 1, 1),(15, self._size/2), 4)
        else:
            pygame.draw.circle(self.surface, (1, 1, 1),(5, self._size/2), 4)
            pygame.draw.circle(self.surface, (1, 1, 1),(15, self._size/2), 4)


class SnakeBody(SnakePart):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.surface.fill((255, 241, 0))
