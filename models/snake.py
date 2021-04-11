import random
import pygame

class Player:
    x = 0
    y = 0
    speed = 32
    direction = 0

    # def update(self):
    #     if self.direction == 0:
    #         self.x = self.x + self.speed
    #     if self.direction == 1:
    #         self.x = self.x - self.speed
    #     if self.direction == 2:
    #         self.y = self.y - self.speed
    #     if self.direction == 3:
    #         self.y = self.y + self.speed

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

# def Your_score(score):
#     value = score_font.render("Your Score: " + str(score), True, yellow)
#     dis.blit(value, [0, 0])

class Snake:
    def __init__(self):
        self._size = 20
        self._head = SnakeHead(500, 500, self._size)
        self._body1 = SnakeBody(self._head.x + self._size, self._head.y, self._size)
        self._body2 = SnakeBody(self._body1.x + self._size, self._head.y, self._size)
        self._body3 = SnakeBody(self._body2.x + self._size, self._head.y, self._size)
        self._body4 = SnakeBody(self._body3.x + self._size, self._head.y, self._size)
        self._body5 = SnakeBody(self._body4.x + self._size, self._head.y, self._size)
        self._body6 = SnakeBody(self._body5.x + self._size, self._head.y, self._size)
        self.full_body = [self._head, self._body1, self._body2, self._body3, self._body4, self._body5, self._body6]
        self.direction = "Left"
        self.score = 0

    @property
    def head_position(self):
        return [self._head.x, self._head.y]


    @property
    def range(self):
        x_min = 1000
        y_min = 1000
        x_max = 0
        y_max = 0
        for part in self.full_body:
            if part.x < x_min:
                x_min = part.x
            if part.x > x_max:
                x_max = part.x
            if part.y < y_min:
                y_min = part.y
            if part.y > y_max:
                y_max = part.y
        return {"x_min": x_min, "x_max": x_max + self._size, "y_min": y_min, "y_max": y_max + self._size}

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
