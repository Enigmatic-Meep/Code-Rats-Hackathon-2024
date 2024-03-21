import pygame

class SceneManager:
  def __init__(self):
    self.scenes = {}  # Dictionary to store scenes with names as keys
    self.current_scene = None
    self.current_name = None
    self.running = True

    # Set screen size for all scenes
    self.screen_width = 800
    self.screen_height = 800
    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

  def add_scene(self, name, scene):
    self.scenes[name] = scene

  def set_scene(self, name): # Set current scene from list of added scenes
    if name in self.scenes:
      self.current_scene = self.scenes[name]

  def run(self):
    clock = pygame.time.Clock()
    dt = 0

    while self.running:
      events = pygame.event.get()

      # Update and draw current scene if available
      if self.current_scene:
        self.current_scene.update(dt)
        self.current_scene.draw(self.screen, events)

      # Handle events
      for event in events:
        if event.type == pygame.QUIT:
          self.running = False
        if self.current_scene:
          self.current_scene.handle_events(event)

      # Delta time in milliseconds, capped at 60 FPS
      # divided by 1000 to have units of seconds for dt
      dt = clock.tick(60) / 1000 

      # Update display
      pygame.display.flip()

    # Quit Pygame
    pygame.quit()