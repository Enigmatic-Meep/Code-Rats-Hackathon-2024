import pygame

from SceneManager import SceneManager

from Scene import Scene
from StartScreen import StartScreen
from GameScreen import GameScreen

from Button import Button

# Create StartScreen instance
pygame.init()

scene_manager = SceneManager()
start_screen = StartScreen(scene_manager)
game_screen = GameScreen(scene_manager)

scene_manager.add_scene("start_screen", start_screen)
scene_manager.add_scene("game_screen", game_screen)
scene_manager.set_scene("start_screen")

scene_manager.run()

# Main game loop
# while scene_manager.running:
#     start_screen.draw()
#     start_screen.handle_events()
#     pygame.display.flip()

pygame.quit()
