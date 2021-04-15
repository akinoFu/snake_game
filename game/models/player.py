import pygame

class Player():
    def __init__(self, name='test', score=0):
        self.name = name
        self.score = score


    def add_point(self):
        self.score += 1

