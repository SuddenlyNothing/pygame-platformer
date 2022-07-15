import pygame
from timer import Timer

class Player(pygame.sprite.Sprite):

  WIDTH = 10
  HEIGHT = 50

  jump_key = pygame.K_SPACE
  left = pygame.K_a
  right = pygame.K_d

  _GRAVITY = 0.25
  _JUMP_FORCE = 5
  _MAX_FALL_SPEED = 5
  _COLOR = [0, 0, 0]
  _ACCELERATION = 0.5
  _MAX_SPEED = 3
  _FRICTION = 0.25
  _COYOTE_TIME = 0.15
  _BUFFER_TIME = 0.15

  _JUMP_SFX = pygame.mixer.Sound("assets/sfx/jump.wav")

  def __init__(self, x: float, y: float) -> None:
    super().__init__()
    self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.image.fill(self._COLOR)
    self.velocity = pygame.Vector2(0, 0)
    self.jump_pressed = False
    self.jump_press = False
    self.is_on_floor = True
    self.x_input = 0
    self.floor_detect = pygame.Rect(x - self.WIDTH / 2, y - self.HEIGHT / 2 + 1, self.WIDTH, self.HEIGHT)
    self.jump_buffer_timer = Timer(self._BUFFER_TIME)
    self.coyote_timer = Timer(self._COYOTE_TIME)

  def destroy(self) -> None:
    self.kill()
    del self

  def set_rect_x(self, x: float) -> None:
    self.rect.centerx = x
    self.floor_detect.centerx = x

  def set_rect_y(self, y: float) -> None:
    self.rect.centery = y
    self.floor_detect.centery = y + 1

  def move_rect(self, x: float, y: float) -> None:
    self.rect.center += pygame.Vector2(x, y)
    self.floor_detect.center += pygame.Vector2(x, y)

  def get_input(self) -> None:
    keystate = pygame.key.get_pressed()
    self.jump_pressed = self.jump_press
    self.jump_press = keystate[self.jump_key]
    if self.jump_press and not self.jump_pressed:
      self.jump_buffer_timer.start()
    self.x_input = keystate[self.right] - keystate[self.left]

  def move_and_collide(self, tiles: list = []) -> None:
    self.move_rect(self.velocity.x, 0)
    for tile in tiles:
      if tile is self:
        continue
      if self.rect.colliderect(tile.rect):
        if self.velocity.x > 0:
          self.set_rect_x(tile.rect.centerx - tile.WIDTH / 2 - self.WIDTH / 2)
        else:
          self.set_rect_x(tile.rect.centerx + tile.WIDTH / 2 + self.WIDTH / 2)
        self.velocity.x = 0
        break
    self.move_rect(0, self.velocity.y)
    was_on_floor = self.is_on_floor
    self.is_on_floor = False
    for tile in tiles:
      if tile is self:
        continue
      if self.floor_detect.colliderect(tile.rect) and self.velocity.y >= 0:
        self.is_on_floor = True
      if self.rect.colliderect(tile.rect):
        if self.velocity.y >= 0:
          self.set_rect_y(tile.rect.centery - tile.HEIGHT / 2 - self.HEIGHT / 2)
        else:
          found_slip = False
          for i in range(1, 6):
            if found_slip:
              break
            for j in [-1, 1]:
              self.move_rect(i * j, 0)
              if not self.rect.colliderect(tile.rect):
                found_slip = True
                break
              self.move_rect(-i * j, 0)
          if found_slip:
            break
          self.set_rect_y(tile.rect.centery + tile.HEIGHT / 2 + self.HEIGHT / 2)
        self.velocity.y = 0
        break
    if not self.is_on_floor and was_on_floor and self.velocity.y >= 0:
      self.velocity.y = 0
      self.coyote_timer.start()

  def apply_gravity(self) -> None:
    if not self.coyote_timer.is_stopped():
      return
    self.velocity.y += self._GRAVITY
    if self.velocity.y > self._MAX_FALL_SPEED:
      self.velocity.y = self._MAX_FALL_SPEED
  
  def jump(self) -> None:
    if ((self.jump_press and \
        not self.jump_pressed) or not self.jump_buffer_timer.is_stopped()) and \
        (self.is_on_floor or not self.coyote_timer.is_stopped()):
      self.velocity.y = -self._JUMP_FORCE
      self.jump_buffer_timer.stop()
      self.coyote_timer.stop()
      pygame.mixer.Sound.play(self._JUMP_SFX)

  def walk(self) -> None:
    self.velocity.x += self.x_input * self._ACCELERATION
    if abs(self.velocity.x) > self._MAX_SPEED:
      self.velocity.x = max(-self._MAX_SPEED, min(self._MAX_SPEED, self.velocity.x))
  
  def apply_friction(self) -> None:
    if self.x_input:
      return
    if abs(self.velocity.x) < self._FRICTION:
      self.velocity.x = 0
    if self.velocity.x > 0:
      self.velocity.x -= self._FRICTION
    else:
      self.velocity.x += self._FRICTION

  def move(self, tiles: list = []) -> None:
    self.get_input()
    self.apply_gravity()
    self.jump()
    self.walk()
    self.apply_friction()
    self.move_and_collide(tiles)
  
  def update(self, tiles = []):
    self.move(tiles)