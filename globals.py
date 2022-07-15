import pygame

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = [18, 152, 196]
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
EVENTS = []

def update_events():
  global EVENTS
  EVENTS = pygame.event.get()
