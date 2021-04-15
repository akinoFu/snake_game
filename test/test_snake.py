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

def test_head_position(snake):
    """ Test head_position property """
    assert snake.head_position == [500, 500]


def test_range(snake):
    """ Test range property """
    assert snake.range == {"x_min": 500,
                           "x_max": 580,
                           "y_min": 500,
                           "y_max": 520
                          }

def test_move_left(snake):
    """ Test move method (Left) """
    snake.move()
    assert snake._head.x == 480
    assert snake._head.y == 500
    assert snake.full_body[1].x == 500
    assert snake.full_body[1].y == 500
    assert snake.full_body[2].x == 520
    assert snake.full_body[2].y == 500
    assert snake.full_body[3].x == 540
    assert snake.full_body[3].y == 500

def test_move_up(snake):
    """ Test move method (Up) """
    snake.direction = "Up"
    snake.move()
    assert snake._head.x == 500
    assert snake._head.y == 480
    assert snake.full_body[1].x == 500
    assert snake.full_body[1].y == 500
    assert snake.full_body[2].x == 520
    assert snake.full_body[2].y == 500
    assert snake.full_body[3].x == 540
    assert snake.full_body[3].y == 500

def test_move_down(snake):
    """ Test move method (Down) """
    snake.direction = "Down"
    snake.move()
    assert snake._head.x == 500
    assert snake._head.y == 520
    assert snake.full_body[1].x == 500
    assert snake.full_body[1].y == 500
    assert snake.full_body[2].x == 520
    assert snake.full_body[2].y == 500
    assert snake.full_body[3].x == 540
    assert snake.full_body[3].y == 500


def test_move_right(snake):
    """ Test move method (Right) """
    snake.direction = "Right"
    snake.move()
    assert snake._head.x == 520
    assert snake._head.y == 500
    assert snake.full_body[1].x == 500
    assert snake.full_body[1].y == 500
    assert snake.full_body[2].x == 520
    assert snake.full_body[2].y == 500
    assert snake.full_body[3].x == 540
    assert snake.full_body[3].y == 500

def test_turn_Up(snake):
    """ Test turn method (Up) """
    snake.turn("Up")
    assert snake.direction == "Up"

def test_add_body(snake):
    """ Test add_body method """
    snake.add_body()
    assert len(snake.full_body) == 5
    assert snake.full_body[4].x == snake.full_body[3].x + snake._size
    assert snake.full_body[4].y == snake.full_body[3].y


