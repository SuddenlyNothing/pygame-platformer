import pygame
import globals

class Button(pygame.sprite.Sprite):

  NORMAL = 1
  HOVER = 2
  PRESS = 3

  _FONT_NAME = pygame.font.match_font('comic sans ms')
  _FONT = pygame.font.Font(_FONT_NAME, 16)
  _NORMAL_COLOR = [240, 240, 240]
  _HOVER_COLOR = [255, 255, 255]
  _PRESS_COLOR = [230, 230, 230]

  _NORMAL_FONT_COLOR = [30, 30, 30]
  _HOVER_FONT_COLOR = [40, 40, 40]
  _PRESS_FONT_COLOR = [0, 0, 0]

  def __init__(self, x: float, y: float, width: int, height: int, text: str, *signals: list) -> None:
    super().__init__()
    self.image = pygame.Surface([width, height])
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.image.fill(self._NORMAL_COLOR)
    self.text = text
    self.state = self.NORMAL
    self.text_color = self._NORMAL_FONT_COLOR
    self.pressing = False
    self.signals = signals

  def draw_text(self, screen: pygame.Surface = globals.SCREEN) -> None:
    text_surface = self._FONT.render(self.text, True, self.text_color)
    text_rect = text_surface.get_rect()
    text_rect.center = self.rect.center
    screen.blit(text_surface, text_rect)

  def set_state(self, state):
    self.state = state
    if state == self.NORMAL:
        self.image.fill(self._NORMAL_COLOR)
        self.text_color = self._NORMAL_FONT_COLOR
    elif state == self.HOVER:
        self.image.fill(self._HOVER_COLOR)
        self.text_color = self._HOVER_FONT_COLOR
    elif state == self.PRESS:
        self.image.fill(self._PRESS_COLOR)
        self.text_color = self._PRESS_FONT_COLOR

  def pressed(self):
    for signal in self.signals:
      call_func = getattr(signal[0], signal[1])
      call_func()
  
  def is_colliding(self, mouse_pos: list) -> bool:
    return self.rect.collidepoint(mouse_pos[0], mouse_pos[1])

  def update(self, screen: pygame.Surface = globals.SCREEN, events: list = globals.EVENTS):
    self.draw_text(screen)
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if self.is_colliding(mouse_pos):
          self.set_state(self.PRESS)
          self.pressing = True
      elif event.type == pygame.MOUSEBUTTONUP:
        mouse_pos = pygame.mouse.get_pos()
        if self.is_colliding(mouse_pos) and self.pressing:
          self.pressed()
          self.set_state(self.HOVER)
        self.pressing = False
      elif event.type == pygame.MOUSEMOTION:
        mouse_pos = pygame.mouse.get_pos()
        if self.state == self.NORMAL:
          if self.is_colliding(mouse_pos):
            if pygame.mouse.get_pressed() and self.pressing:
              self.set_state(self.PRESS)
            else:
              self.set_state(self.HOVER)
        elif self.state == self.HOVER:
          if not self.is_colliding(mouse_pos):
            self.set_state(self.NORMAL)
        elif self.state == self.PRESS:
            if not self.is_colliding(mouse_pos):
              self.set_state(self.NORMAL)
