#!/usr/bin/env python3
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()

from level_manager import LevelManager

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1020, 600))
background_color = [18, 152, 196]

pygame.mixer.music.load("assets/music/music.ogg")
pygame.mixer.music.play(-1)

level_manager = LevelManager()

while True:
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
  screen.fill(background_color)

  level_manager.update(screen)

  pygame.display.flip()
  clock.tick(60)