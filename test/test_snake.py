import pytest
from game.models.snake import Snake, SnakePart

@pytest.fixture
def snake():
    return Snake()

def test_snake_init(snake):
    """ Test the constructor of Snake class """
    assert snake._size == 20
    assert len(snake.full_body) == 4
    assert snake.direction == "Left"

def test_move_left(snake):
    """ Test move method (Left) """
    snake.move()
    assert snake._head.rect.x == 480
    assert snake._head.rect.y == 500
    assert snake.full_body[1].rect.x == 500
    assert snake.full_body[1].rect.y == 500
    assert snake.full_body[2].rect.x == 520
    assert snake.full_body[2].rect.y == 500
    assert snake.full_body[3].rect.x == 540
    assert snake.full_body[3].rect.y == 500

def test_move_up(snake):
    """ Test move method (Up) """
    snake.direction = "Up"
    snake.move()
    assert snake._head.rect.x == 500
    assert snake._head.rect.y == 480
    assert snake.full_body[1].rect.x == 500
    assert snake.full_body[1].rect.y == 500
    assert snake.full_body[2].rect.x == 520
    assert snake.full_body[2].rect.y == 500
    assert snake.full_body[3].rect.x == 540
    assert snake.full_body[3].rect.y == 500

def test_move_down(snake):
    """ Test move method (Down) """
    snake.direction = "Down"
    snake.move()
    assert snake._head.rect.x == 500
    assert snake._head.rect.y == 520
    assert snake.full_body[1].rect.x == 500
    assert snake.full_body[1].rect.y == 500
    assert snake.full_body[2].rect.x == 520
    assert snake.full_body[2].rect.y == 500
    assert snake.full_body[3].rect.x == 540
    assert snake.full_body[3].rect.y == 500


def test_move_right(snake):
    """ Test move method (Right) """
    snake.direction = "Right"
    snake.move()
    assert snake._head.rect.x == 520
    assert snake._head.rect.y == 500
    assert snake.full_body[1].rect.x == 500
    assert snake.full_body[1].rect.y == 500
    assert snake.full_body[2].rect.x == 520
    assert snake.full_body[2].rect.y == 500
    assert snake.full_body[3].rect.x == 540
    assert snake.full_body[3].rect.y == 500

def test_turn_Up(snake):
    """ Test turn method (Up) """
    snake.turn("Up")
    assert snake.direction == "Up"

def test_add_body(snake):
    """ Test add_body method """
    snake.add_body()
    assert len(snake.full_body) == 5
    assert snake.full_body[4].rect.x == snake.full_body[3].rect.x + snake._size
    assert snake.full_body[4].rect.y == snake.full_body[3].rect.y


