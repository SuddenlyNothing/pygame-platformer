import pygame

class Tile(pygame.sprite.Sprite):

  WIDTH = 20
  HEIGHT = 20

  _color = [100, 100, 100]

  def __init__(self, x: float, y: float) -> None:
    super().__init__()
    self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.image.fill(self._color)