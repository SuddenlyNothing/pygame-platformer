#!/usr/bin/env python3
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()

import globals
from level import Level

level = Level()

while True:
  globals.update_events()
  for event in globals.EVENTS:
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
  globals.SCREEN.fill(globals.BACKGROUND_COLOR)

  level.update()

  pygame.display.flip()
  globals.CLOCK.tick(60)