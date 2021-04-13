import pytest

from game.models.food import Apple, Poison
from game.models.snake import Snake

@pytest.fixture
def apple():
    return Apple()

@pytest.fixture
def snake():
    return Snake()

@pytest.fixture
def poison():
    return Poison()

def test_apple_init(apple):
    assert apple.rect.x in range(100, 650)
    assert apple.rect.y in range(100, 650)


def test_overlap_with_poison(apple, poison):
    apple.rect.x = 100
    apple.rect.y = 200
    poison.rect.x = 100
    poison.rect.y = 200
    assert apple.rect.x == 180
    assert apple.rect.y == 295


def test_poison_init(poison):
    assert poison.rect.x in range(100, 650)
    assert poison.rect.y in range(100, 650)


def test_poison_eaten(poison, snake):
    pass