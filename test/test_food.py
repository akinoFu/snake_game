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
    """ tests to see if apple x and y are set in init"""
    assert apple.rect.x in range(100, 650)
    assert apple.rect.y in range(100, 650)


def test_apple_eaten(apple, snake):
    """ tests to see if apple x and y have been changed since apple has been eaten by snake """
    apple.rect.x = 500
    apple.rect.y = 500
    snake = snake.head_position
    result = apple.apple_eaten(snake)
    assert result == True



def test_overlap_with_poison(apple, poison):
    """ tests to see when apple and poison overlap, that apple's x and y change """
    apple.rect.x = 100
    apple.rect.y = 200
    poison.rect.x = 100
    poison.rect.y = 200
    
    apple.overlap_poison_with_apple(poison)

    assert apple.rect.x == 180
    assert apple.rect.y == 295

def test_overlap_with_poison_greaterthan(apple, poison):
    """ tests to see when apple and poison overlap, that apple's x and y change (greater than or = to 750) """
    apple.rect.x = 750
    apple.rect.y = 750
    poison.rect.x = 750
    poison.rect.y = 750
    
    apple.overlap_poison_with_apple(poison)

    assert apple.rect.x == 670
    assert apple.rect.y == 655


def test_overlap_snake_new_apple(apple, snake):
    """ tests to see apple is in range when new apple"""
    apple.rect.x = 500
    apple.rect.y = 500
    snake = snake.range

    apple.overlap_snake_new_apple(snake)

    assert apple.rect.x in range(100, 650)
    assert apple.rect.y in range(100, 650)


def test_poison_init(poison):
    """ tests to see if poison x and y are set correctly """
    assert poison.rect.x in range(100, 650)
    assert poison.rect.y in range(100, 650)

def test_poison_eaten(poison, snake):
    """ tests to see if poison has been eaten by snake """
    poison.rect.x = 500
    poison.rect.y = 500
    snake = snake.head_position

    result = poison.poison_eaten(snake)

    assert result == True


