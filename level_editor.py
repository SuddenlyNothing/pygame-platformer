import pygame
import globals

class LevelEditor():

  LEVEL_WIDTH = globals.SCREEN_WIDTH // globals.TILE_WIDTH
  LEVEL_HEIGHT = globals.SCREEN_HEIGHT // globals.TILE_HEIGHT

  def __init__(self, level: list = []) -> None:
    self.level = level
    self.draw_group = pygame.sprite.Group()

  def save_level(self, prefix: str) -> None:
    pass
  
  def update(self) -> None:
    pass