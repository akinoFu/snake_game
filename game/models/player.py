import pygame

class Player():
    def __init__(self, name='test', score=0):
        self.name = name
        self.score = score
        self.X = 10
        self.Y = 10


    def add_point(self):
        self.score += 1

