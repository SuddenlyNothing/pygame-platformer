import pygame
from tile import Tile
from player import Player
from os.path import exists

class LevelManager():
  
  TILE = 1
  PLAYER = 2

  def __init__(self, level: int = 1, prefix: str = "levels/level") -> None:
    self.prefix = prefix
    self.level = level

    self.tile_group = pygame.sprite.Group()
    self.tile_collision_group = pygame.sprite.Group()
    self.load_level()

  def load_level(self) -> bool:
    filename = self.prefix + str(self.level)
    if not exists(filename):
      return False
    with open(filename, "r") as f:
      y = 0
      for line in f:
        line = line.replace("\n", "").split(" ")
        x = 0
        for tile in line:
          tile = int(tile)
          match tile:
            case self.TILE:
              self.tile_group.add(
                Tile(Tile.WIDTH / 2 + x * Tile.WIDTH, Tile.HEIGHT / 2 + y * Tile.HEIGHT)
              )
            case self.PLAYER:
              self.tile_collision_group.add(
                Player(Tile.WIDTH / 2 + x * Tile.WIDTH, Tile.HEIGHT / 2 + y * Tile.HEIGHT + (Tile.HEIGHT - Player.HEIGHT) / 2)
              )
          x += 1
        y += 1
    return True
  
  def set_level(self, level: int = 1) -> bool:
    self.level = level
    return self.load_level()
  
  def next_level(self) -> bool:
    return self.set_level(self.level + 1)

  def update(self, screen: pygame.Surface) -> None:
    self.tile_group.draw(screen)
    self.tile_collision_group.draw(screen)
    self.tile_collision_group.update(self.tile_group.sprites())
