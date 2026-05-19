import pytest
import pygame
from src.ship import Ship

class DummySettings:
    def __init__(self):
        self.ship_speed = 5

class DummyScreen:
    def get_rect(self):
        return pygame.Rect(0, 0, 800, 600)

@pytest.fixture
def ship(monkeypatch):
    pygame.init()

    monkeypatch.setattr(pygame.image, "load", lambda x: pygame.Surface((50, 50)))

    screen = DummyScreen()
    settings = DummySettings()
    return Ship(screen, settings)

def test_move_right(ship):
    initial_x = ship.x
    ship.moving_right = True

    ship.update()

    assert ship.x == initial_x + ship.settings.ship_speed

def test_move_left(ship):
    initial_x = ship.x
    ship.moving_left = True

    ship.update()

    assert ship.x == initial_x - ship.settings.ship_speed

def test_stop_at_right_edge(ship):
    ship.rect.right = ship.screen_rect.right
    ship.moving_right = True

    ship.update()

    assert ship.rect.right <= ship.screen_rect.right

def test_stop_at_left_edge(ship):
    ship.rect.left = 0
    ship.moving_left = True

    ship.update()

    assert ship.rect.left >= 0