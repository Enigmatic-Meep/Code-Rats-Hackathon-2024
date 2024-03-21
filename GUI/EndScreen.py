import pygame

from SceneManager import SceneManager
from Scene import Scene
from Button import Button
# from GameScreen import GameScreen
from StartScreen import StartScreen
from pathlib import Path

class EndScreen(Scene):
    def __init__(self, scene_manager, score):
        # Set window title
        pygame.display.set_caption("RATorical Quest - End Screen")

        # Set Scene Manager Reference
        self.scene_manager = scene_manager

        # Set font and colors
        self.font = pygame.font.SysFont("inkfree", 40)  # Choose a font or path to a font file
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.scale = 15

        # initialize score from gamescreen
        self.score = score

        # Load title image
        here = Path(__file__).resolve()
        root_folder = here.parents[0]
        name = "png/EndScreen.png"
        my_path = root_folder / name
        self.endScreenImage = pygame.image.load(my_path)

        # Set game to be running
        self.running = True

        # Create button using the Button class
        self.retry_button = Button("Restart", (scene_manager.screen_width // 2 - 70, scene_manager.screen_height // 2 + 200), self.white, (100, 100, 100), self.handle_retry_click)

    def draw(self, screen, events):
        # Fill screen with color
        screen.fill(0)

        # Draw background image
        screen.blit(self.endScreenImage, (0, 0))

        # Render and draw score
        finalScore = self.font.render(f"Final score: {self.score}", True, (255, 255, 255))
        screen.blit(finalScore, (800 // 2 - 130, 800 // 2 - 60))

        # Draw buttons
        self.retry_button.draw(screen)
        # self.menu_button.draw(screen) <-- no time :(

    def handle_events(self, event):
        # Check for button clicks only upon mouse button events
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.retry_button.handle_click(event)  # Pass the event to handle click state

    def handle_retry_click(self):
        # Perform action when start button is clicked
        print("Restart button clicked!")
        start_screen = StartScreen(self.scene_manager)  # Create new GameScreen instance
        self.scene_manager.add_scene("start_screen", start_screen)
        self.scene_manager.set_scene("start_screen")  # Switch scene using scene manager