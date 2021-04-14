import pytest
from game.models.player import Player
from game.models.snake import Snake

@pytest.fixture
def snake():
    return Snake()

@pytest.fixture
def add_point():
    return Player()


def test_player_init(add_point):
    """ Test the constructor of Player class """
    assert name._name == name
    assert score == score