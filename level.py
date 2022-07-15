import pygame
import globals
from tile import Tile
from player import Player
from os.path import exists

class Level():

  DEFAULT_LEVEL_PATH = "levels/level"

  TILE = 1
  PLAYER = 2

  def __init__(self, level: list = [], file_num: int = 1, prefix: str = DEFAULT_LEVEL_PATH) -> None:
    self.level = level
    self.file_num = file_num
    self.prefix = prefix
    self.tile_group = pygame.sprite.Group()
    self.tile_collision_group = pygame.sprite.Group()
    if level:
      self.load_level()
    else:
      self.load_level_file()

  def update(self) -> None:
    self.tile_group.draw(globals.SCREEN)
    self.tile_collision_group.draw(globals.SCREEN)
    self.tile_collision_group.update(self.tile_group.sprites())

  def load_level(self) -> None:
    self.clear_level()
    for y in range(len(self.level)):
      for x in range(len(self.level[y])):
        if self.level[y][x] == self.TILE:
          self.tile_group.add(
            Tile(Tile.WIDTH / 2 + x * Tile.WIDTH, Tile.HEIGHT / 2 + y * Tile.HEIGHT)
          )
        elif self.level[y][x] == self.PLAYER:
          self.tile_collision_group.add(
            Player(Tile.WIDTH / 2 + x * Tile.WIDTH, Tile.HEIGHT / 2 + y * Tile.HEIGHT + (Tile.HEIGHT - Player.HEIGHT) / 2)
          )
  
  def load_level_file(self) -> bool:
    filename = self.prefix + str(self.file_num)
    if not exists(filename):
      return False
    with open(filename, "r") as f:
      for line in f:
        line = line.replace("\n", "").split(" ")
        self.level.append([])
        for tile in line:
          tile = int(tile)
          if tile == self.TILE:
            self.level[-1].append(self.TILE)
          elif tile == self.PLAYER:
            self.level[-1].append(self.PLAYER)
          else:
            self.level[-1].append(0)
    self.load_level()
    return True

  def set_load_level_file(self, file_num: int = 1, prefix: str = DEFAULT_LEVEL_PATH) -> bool:
    self.file_num = file_num
    self.prefix = prefix
    return self.load_level_file()

  def load_next_level_file(self) -> bool:
    self.file_num += 1
    return self.load_level_file()
  
  def clear_level(self) -> None:
    self.tile_group.empty()
    self.tile_collision_group.empty()