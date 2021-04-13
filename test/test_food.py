import pytest

from game.models.food import Apple, Poison
from game.models.snake import Snake


@pytest.fixture
def apple():
    return Apple()


@pytest.fixture
def poison():
    return Poison()


@pytest.fixture
def snake():
    return Snake()

def test_apple_init(apple):
    assert apple.rect.x in range(100, 650)
    assert apple.rect.y in range(100, 650)


def test_apple_eaten(apple, snake):
    apple.rect.x = 500
    apple.rect.y = 500
    snake = snake.head_position
    apple.apple_eaten(snake)

    assert apple.rect.x in range(100, 650)
    assert apple.rect.y in range(100, 650)


def test_overlap_with_poison(apple, poison):
    apple.rect.x = 100
    apple.rect.y = 200
    poison.rect.x = 100
    poison.rect.y = 200
    
    apple.overlap_poison_with_apple(poison)

    assert apple.rect.x == 180
    assert apple.rect.y == 295

def test_overlap_with_poison_greaterthan(apple, poison):
    apple.rect.x = 750
    apple.rect.y = 750
    poison.rect.x = 750
    poison.rect.y = 750
    
    apple.overlap_poison_with_apple(poison)

    assert apple.rect.x == 670
    assert apple.rect.y == 655


def test_overlap_snake_new_apple(apple, snake):
    apple.rect.x = 500
    apple.rect.y = 500
    snake = snake.range

    apple.overlap_snake_new_apple(snake)

    assert apple.rect.x in range(100, 650)
    assert apple.rect.y in range(100, 650)


def test_poison_init(poison):
    assert poison.rect.x in range(100, 650)
    assert poison.rect.y in range(100, 650)

def test_poison_eaten(poison, snake):
    poison.rect.x = 500
    poison.rect.y = 500
    snake = snake.head_position

    result = poison.poison_eaten(snake)

    assert result == True


