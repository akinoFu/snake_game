import random
import pygame

class Snake:
    def __init__(self):
        """ Snake Class that builds and moves the snake """
        self._size = 20
        self._head = SnakePart(500, 500, self._size, True)
        self.full_body = [self._head,
                          SnakePart(self._head.rect.x + self._size, self._head.rect.y, self._size),
                          SnakePart(self._head.rect.x + self._size * 2, self._head.rect.y, self._size),
                          SnakePart(self._head.rect.x + self._size * 3, self._head.rect.y, self._size)
                        ]
        self._group = pygame.sprite.Group()
        self.direction = "Left"

    @property
    def group(self):
        self._group.empty()
        for part in self.full_body:
            self._group.add(part)
        return self._group

    @property
    def head_position(self):
        """ Retur x and y of the head """
        return [self._head.rect.x, self._head.rect.y]

    @property
    def range(self):
        """ Return max and min coordinates of the whole body """
        x_min = 1000
        y_min = 1000
        x_max = 0
        y_max = 0
        for part in self.full_body:
            if part.rect.x < x_min:
                x_min = part.rect.x
            if part.rect.x > x_max:
                x_max = part.rect.x
            if part.rect.y < y_min:
                y_min = part.rect.y
            if part.rect.y > y_max:
                y_max = part.rect.y
        return {"x_min": x_min, "x_max": x_max + self._size, "y_min": y_min, "y_max": y_max + self._size}


    def move(self):
        """ Move the snake"""
        # Create new body
        new_body = list()
        
        # Add new body parts with new x and y
        l = len(self.full_body)
        for i, part in enumerate(reversed(self.full_body)):
            if i+1 < l:
                part = SnakePart(self.full_body[l-i-2].rect.x, self.full_body[l-i-2].rect.y, self._size)
                new_body.insert(0, part)

        # Add new head
        head_x = self._head.rect.x
        head_y = self._head.rect.y        
        if self.direction == "Up":
            head_y -= self._size
        elif self.direction == "Down":
            head_y += self._size
        elif self.direction == "Right":
            head_x += self._size
        elif self.direction == "Left":
            head_x -= self._size

        self._head = SnakePart(head_x, head_y, self._size, True, self.direction)
        new_body.insert(0, self._head)

        # Replace the full body with new body
        self.full_body = new_body


    def turn(self, direction):
        """ Change the direction """
        # Set new direction
        self.direction = direction
    
    def add_body(self):
        """ Make the snake longer """
        new_part = SnakePart(self.full_body[-1].rect.x + self._size,
                             self.full_body[-1].rect.y,
                             self._size)
        self.full_body.append(new_part)

    def check_hit_wall(self, window):
        """ Check if the snake hits one of the four sides """
        if self._head.rect.x < 0 \
               or self._head.rect.y < 0 \
               or self._head.rect.x > window.get_width() \
               or self._head.rect.y > window.get_height():
            return True
        return False


class SnakePart(pygame.sprite.Sprite):
    """ Each segment of the snake's body """
    def __init__(self, x, y, size, head=False, direction="Left"):
        super().__init__()
        # Load the image
        if head:
            image = pygame.image.load('game/assets/img/snake_head.png')
        else:
            image = pygame.image.load('game/assets/img/snake_body.png')
        
        # Resize the image
        self.image = pygame.transform.scale(image, (size, size))
        
        # Rotate the image depends on the direction
        if direction in ("Up","Down"):
            self.image = pygame.transform.rotate(self.image, 90)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

