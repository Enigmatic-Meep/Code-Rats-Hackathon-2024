import pygame
import pygame_textinput

from pygame.font import Font  # Import Font class for custom font

from SceneManager import SceneManager
from Scene import Scene
from Button import Button
import sys
import os
from pathlib import Path

from Word_Processing.Scoring import assign_points
from Word_Processing.letter_generation import generate_letters


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
        self.font = pygame.font.SysFont("inkfree", 40)  # Choose a font or path to a font file
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.scale = 15

        # Load background image
        here = Path(__file__).resolve()
        root_folder = here.parents[0]
        name = "png/GameScreen.png"
        my_path = root_folder / name
        self.gameScreenImage = pygame.image.load(my_path)

        # Create text-input object
        self.textinput = pygame_textinput.TextInputVisualizer()

        # Initialize list of user inputted words
        self.user_words = []

        # Initialize random letters to be typed out
        self.letters = generate_letters()

        # Initialize user score to 0
        self.score = 0

        # Create timer
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, 1000)  # 1 second timer
        self.countdown_time = 60  # countdown duration (seconds)
        self.time_remaining = self.countdown_time  # Keep track of remaining time

    def draw(self, screen, events):
        # Fill screen with color
        screen.fill(0)

        self.textinput.update(events)

        # Draw background image
        screen.blit(self.gameScreenImage, (0, 0))

        self.text = self.font.render(self.letters[0]+ " " + self.letters[1] + " " + self.letters[2] + " " + self.letters[3],True, self.white, self.black)
        screen.blit(self.text,(screen_width // 2 - 50, screen_height // 2 + 20) )

        # Blit text input onto the screen
        screen.blit(self.textinput.surface, ((screen_width // 2 - 50, screen_height // 2 + 80)))

        # Timer countdown
        if self.time_remaining > 0:
            time_surface = self.font.render(f"Time Remaining: {self.time_remaining}", True, (255, 255, 255))
            screen.blit(time_surface, (20, 50))  # Adjust position

    def handle_events(self, event):
        if event.type == pygame.QUIT:
            self.running = False

        if event.type == self.timer_event:
            self.time_remaining -= 1

            # Check if countdown has reached 0
            if self.time_remaining == 0:
                # Perform actions when countdown finishes (e.g., game over)
                print("Game Over!")

                # Print list of user inputs
                for word in self.user_words:
                    print(f"{word}, ")

                # Optionally stop the timer here
                pygame.time.set_timer(self.timer_event, 0)

                # end_screen = EndScreen(self.scene_manager)
                self.scene_manager.set_scene("end_screen")


        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # Print and capture user input
            print(f"Word inputted: {self.textinput.value}")
            self.user_words.append(self.textinput.value)
            
            # Decide if input is a match
            data_folder = Path("CODE-RATS-HACKATHON-2024-Main/Word_Processing/letter_files/")
            add = assign_points(self.textinput.value,self.letters)
            self.score+=add
            if add > 0:
                print(f"Correct Word!")
            else:
                print(f"Try again!")
            
            # Reset user input
            self.textinput.value = ""
                
