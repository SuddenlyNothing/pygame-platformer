import pygame
from level import Level

class LevelManager():

  def __init__(self) -> None:
    self.level = Level()

  def update(self) -> None:
    self.level.update()
