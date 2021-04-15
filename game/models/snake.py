import random
import pygame

class Snake:
    def __init__(self):
        """ Snake Class that builds and moves the snake """
        self._size = 20
        self._head = SnakePart(500, 500, self._size)
        self.full_body = [self._head,
                          SnakePart(self._head.x + self._size, self._head.y, self._size),
                          SnakePart(self._head.x + self._size * 2, self._head.y, self._size),
                          SnakePart(self._head.x + self._size * 3, self._head.y, self._size)
                        ]
        self.direction = "Left"

    @property
    def head_position(self):
        """ Retur x and y of the head """
        return [self._head.x, self._head.y]

    @property
    def range(self):
        """ Return max and min coordinates of the whole body """
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

    @property
    def eyes_pos(self):
        """ Return list of tuples that represent eyes' coordinates """
        if self.direction == "Left":
            return [(self._head.x + 5, self._head.y + 5),
                    (self._head.x + 5, self._head.y + 15)]
        elif self.direction == "Right":
            return [(self._head.x + 15, self._head.y + 5),
                    (self._head.x + 15, self._head.y + 15)]
        elif self.direction == "Up":
            return [(self._head.x + 5, self._head.y + 5),
                    (self._head.x + 15, self._head.y + 5)]
        else:
            return [(self._head.x + 5, self._head.y + 15),
                    (self._head.x + 15, self._head.y + 15)]

    def move(self):
        """ Move the snake"""
        # Create new body
        new_body = list()
        
        # Add new body parts with new x and y
        l = len(self.full_body)
        for i, part in enumerate(reversed(self.full_body)):
            if i+1 < l:
                part = SnakePart(self.full_body[l-i-2].x, self.full_body[l-i-2].y, self._size)
                new_body.insert(0, part)

        # Add new head
        head_x = self._head.x
        head_y = self._head.y        
        if self.direction == "Up":
            head_y -= self._size
        elif self.direction == "Down":
            head_y += self._size
        elif self.direction == "Right":
            head_x += self._size
        elif self.direction == "Left":
            head_x -= self._size

        self._head = SnakePart(head_x, head_y, self._size)
        new_body.insert(0, self._head)

        # Replace the full body with new body
        self.full_body = new_body

    def turn(self, direction):
        """ Change the direction """
        # Set new direction
        self.direction = direction
    
    def add_body(self):
        """ Make the snake longer """
        new_part = SnakePart(self.full_body[-1].x + self._size,
                             self.full_body[-1].y,
                             self._size)
        self.full_body.append(new_part)

    def check_hit_wall(self, window):
        """ Check if the snake hits one of the four sides """
        if self._head.x < 0 \
               or self._head.y < 0 \
               or self._head.x > window.get_width() \
               or self._head.y > window.get_height():
            return True
        return False


class SnakePart:
    """ Each segment of the snake's body """
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, size, size)

