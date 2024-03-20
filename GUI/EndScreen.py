import pygame

from SceneManager import SceneManager
from Scene import Scene
from Button import Button
from GameScreen import GameScreen
from StartScreen import StartScreen
from pathlib import Path

class EndScreen(Scene):
    def __init__(self, scene_manager):
        # Set window title
        pygame.display.set_caption("RATorical Quest - End Screen")

        # Set Scene Manager Reference
        self.scene_manager = scene_manager

        # Set font and colors
        self.font = pygame.font.Font(None, 40)  # Choose a font or path to a font file
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.scale = 15

        # Load title image
        here = Path(__file__).resolve()
        root_folder = here.parents[0]
        name = "png/EndScreen.png"
        my_path = root_folder / name
        self.endScreenImage = pygame.image.load(my_path)

        # Set game to be running
        self.running = True

        # Create buttons using the Button class
        self.retry_button = Button("Retry", (scene_manager.screen_width // 2 - 50, scene_manager.screen_height // 2 + 200), self.white, (100, 100, 100), self.handle_retry_click)
        self.menu_button = Button("Menu", (scene_manager.screen_width // 2 - 50, scene_manager.screen_height // 2 + 250), self.white, (100, 100, 100), self.handle_menu_click)

    def draw(self, screen, events):
        # Fill screen with color
        screen.fill(0)

        # Draw background image
        screen.blit(self.endScreenImage, (0, 0))

        # Draw buttons
        self.retry_button.draw(screen)
        # self.menu_button.draw(screen) <-- no time :(

    def handle_events(self, event):
        # Check for button clicks only upon mouse button events
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.retry_button.handle_click(event)  # Pass the event to handle click state

    def handle_retry_click(self):
        # Perform action when start button is clicked
        print("Retry button clicked!")
        game_screen = GameScreen(self.scene_manager)  # Create new GameScreen instance
        self.scene_manager.add_scene("game_screen", game_screen)
        self.scene_manager.set_scene("game_screen")  # Switch scene using scene manager

    def handle_menu_click(self):
        # Perform action when start button is clicked
        print("Menu button clicked!")
        start_screen = StartScreen(self.scene_manager)  # Create new GameScreen instance
        self.scene_manager.add_scene("start_screen", start_screen)
        self.scene_manager.set_scene("start_screen")  # Switch scene using scene manager
