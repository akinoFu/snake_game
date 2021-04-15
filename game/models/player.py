import pygame
import requests


class Player():
    """ Player class that keeps track of name and score of each player """
    def __init__(self, name='test', score=0):
        self.name = name
        self.score = score


    def add_point(self):
        """ adding point to score when apple is eaten """
        self.score += 1

    def post_score(self):
        """ posts score at the end of each game """
        API_URL = "http://localhost:5000/api"
        r = requests.post(f"{API_URL}/score", json={"name": self.name, "score": self.score})

