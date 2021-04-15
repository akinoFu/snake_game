import pytest

from game.models.player import Player

@pytest.fixture
def player():
    return Player()


def test_player(player, name):
    """ Test the constructor of Player class """
    player(name, score)
    assert player.name == name
    assert player.score == 0


def test_add_point(player):
    player.add_point()
    assert player.score == 1