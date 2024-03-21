import pygame
from pygame.locals import *
from pygame import mixer
import pygame_textinput

from pathlib import Path

from SceneManager import SceneManager

from Scene import Scene
from StartScreen import StartScreen
from GameScreen import GameScreen
from EndScreen import EndScreen

from Button import Button

pygame.init()

# Initialize scene manager
scene_manager = SceneManager()

# Create all scene instances
start_screen = StartScreen(scene_manager)
game_screen = GameScreen(scene_manager)
end_screen = EndScreen(scene_manager)


# Add all scenes to scene manager
scene_manager.add_scene("start_screen", start_screen)
scene_manager.add_scene("game_screen", game_screen)
scene_manager.add_scene("end_screen", end_screen)
 
# Set start scene
scene_manager.set_scene("start_screen")
mixer.init()
here = Path(__file__).resolve()
root_folder = here.parents[0]
name = "musicFiles/TalkingCuteChiptune.wav"
my_path = root_folder / name
mixer.music.load(my_path)
mixer.music.play()

scene_manager.run()

pygame.quit()
