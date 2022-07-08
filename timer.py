import pygame

class Timer():

  def __init__(self, wait_time: float = 1.0) -> None:
    self.wait_time = wait_time * 1000
    self._time_left = wait_time * 1000
    self.clock = pygame.time.Clock()
    self._is_stopped = True
  
  def start(self, time_sec: float = -1.0) -> None:
    if time_sec > 0:
      self.wait_time = time_sec * 1000
    self._time_left = self.wait_time
    self.clock.tick()
    self._is_stopped = False

  def stop(self) -> None:
    self._is_stopped = True

  def is_stopped(self) -> bool:
    if self._is_stopped:
      return True
    self.clock.tick()
    elapsed_time = self.clock.get_time()
    self._time_left -= elapsed_time
    if self._time_left >= 0:
      return False
    self._is_stopped = True
    return True
