#!/usr/bin/env python3
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()

from player import Player
from tile import Tile
from button import Button
from level_manager import LevelManager

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1020, 600))
background_color = [18, 152, 196]

tile_group = pygame.sprite.Group()
tile_collision_group = pygame.sprite.Group()
button_group = pygame.sprite.Group()
pygame.mixer.music.load("assets/music/music.ogg")
pygame.mixer.music.play(-1)

l1 = [
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0],
  [0, 2, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 1],
]

def load_level(level):
  for i in range(len(level)):
    for j in range(len(level[i])):
      match level[i][j]:
        case 1: # Tile
          tile_group.add(
            Tile(Tile.WIDTH / 2 + j * Tile.WIDTH, Tile.HEIGHT / 2 + i * Tile.HEIGHT)
          )
        case 2: # Player
          tile_collision_group.add(
            Player(Tile.WIDTH / 2 + j * Tile.WIDTH, Tile.HEIGHT / 2 + i * Tile.HEIGHT + (Tile.HEIGHT - Player.HEIGHT) / 2)
          )

load_level(l1)

level_manager = LevelManager()

while True:
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      tile_x = pos[0] // Tile.WIDTH
      tile_y = pos[1] // Tile.HEIGHT
      tile_group.add(
        Tile(Tile.WIDTH / 2 + tile_x * Tile.WIDTH, Tile.HEIGHT / 2 + tile_y * Tile.HEIGHT)
      )
  screen.fill(background_color)

  # tile_group.draw(screen)
  # tile_collision_group.draw(screen)
  # tile_collision_group.update(tile_group.sprites())

  # button_group.draw(screen)
  # button_group.update(screen, events)
  level_manager.update(screen)
  pygame.display.flip()
  clock.tick(60)