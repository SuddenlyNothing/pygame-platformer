import pygame

class LevelEditor():

  LEVEL_WIDTH = 1020 // 20
  LEVEL_HEIGHT = 600 // 20

  def __init__(self, level: list = []) -> None:
    self.level = level
    self.draw_group = pygame.sprite.Group()

  def save_level(self, prefix: str) -> None:
    pass
  
  def update(self) -> None:
    pass