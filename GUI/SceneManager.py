import pygame

class SceneManager:
  def __init__(self):
    self.scenes = {}  # Dictionary to store scenes with names as keys
    self.current_scene = None
    self.running = True

    # Set screen size for all scenes
    self.screen_width = 800
    self.screen_height = 600
    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

  def add_scene(self, name, scene):
    self.scenes[name] = scene

  def set_scene(self, name): # Set current scene from list of added scenes
    if name in self.scenes:
      self.current_scene = self.scenes[name]

  def run(self):
    clock = pygame.time.Clock()

    while self.running:
      
      # Handle events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
        if self.current_scene:
          self.current_scene.handle_events(event)

      # Update and draw current scene if available
      if self.current_scene:
        # self.current_scene.update(dt)
        self.current_scene.draw(self.screen)

      clock.tick(60)  # Delta time in milliseconds, capped at 60 FPS

      # Update display
      pygame.display.flip()

    # Quit Pygame
    pygame.quit()