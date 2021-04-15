import pytest

from game.models.player import Player

@pytest.fixture
def player():
    return Player()


def test_player(player):
    """ Test the constructor of Player class """
    assert player.name == "test"
    assert player.score == 0


def test_add_point(player):
    """ Test add_point method """
    player.add_point()
    assert player.score == 1
