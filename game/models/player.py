import pygame
import requests


class Player():
    def __init__(self, name='test', score=0):
        self.name = name
        self.score = score


    def add_point(self):
        self.score += 1

    def post_score(self):
        API_URL = "http://localhost:5000/api"
        r = requests.post(f"{API_URL}/score", json={"name": self.name, "score": self.score})

