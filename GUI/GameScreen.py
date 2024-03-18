import pygame_textinput
import pygame

from pygame.font import Font  # Import Font class for custom font

from SceneManager import SceneManager
from Scene import Scene
from Button import Button

# Set screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

class GameScreen(Scene):
    def __init__(self, scene_manager):
        # Set window title
        pygame.display.set_caption("RATorical Quest - Game Screen")

        # Set Scene Manager Reference
        self.scene_manager = scene_manager

        # Set font and colors
        self.font = pygame.font.Font(None, 40)  # Choose a font or path to a font file
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.scale = 15

        # Load background image
        self.gameScreenImage = pygame.image.load("png/GameScreen.png")

        # Create text-input object
        self.textinput = pygame_textinput.TextInputVisualizer()

    def handle_events(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        

    def draw(self, screen):
        # Fill screen with color
        screen.fill(0)

        # Draw background image
        screen.blit(self.gameScreenImage, (0, 0))

        self.textinput.update(pygame.event.get()) # type: ignore

        # Blit its surface onto the screen
        screen.blit(self.textinput.surface, ((self.scene_manager.screen_width // 2 - 50, self.scene_manager.screen_height // 2 + 80)))