import pygame

pygame.init()

# Set screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window title
pygame.display.set_caption("RATorical Quest - Start Screen")

# Set font and colors
font = pygame.font.Font(None, 40)  # Choose a font or path to a font file
white = (255, 255, 255)
black = (0, 0, 0)

# Set scale factor
scale = 15

def draw_button(text, pos, color, click_color):
  # Get button size based on text
  text_surface = font.render(text, True, color)
  button_width = text_surface.get_width() + 20
  button_height = text_surface.get_height() + 10

  # Create button rectangle
  button_rect = pygame.Rect(pos[0], pos[1], button_width, button_height)

  # Check if mouse is hovering over button
  mouse_pos = pygame.mouse.get_pos()
  mouse_over = button_rect.collidepoint(mouse_pos)

  # Change button color based on hover
  if mouse_over:
    color = click_color

  # Draw button rectangle and text
  #pygame.draw.rect(screen, color, button_rect)
  text_surface = font.render(text, True, color)
  screen.blit(text_surface, (button_rect.x + 5, button_rect.y + 5))

#   # Check for button click and perform action
#   if mouse_over and pygame.mouse.get_pressed()[0]:
#     action()  # Call a function to handle start button click

    # Check for button click and perform action (blank action for testing)
  if mouse_over and pygame.mouse.get_pressed()[0]:
    pass  # This does nothing, just a placeholder for testing


running = True
while running:
  # Check for quit events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Fill screen with color
  screen.fill(0)

  # Load title image and scale
  startScreenImage = pygame.image.load("png/StartScreen.png")

  # Draw background image
  screen.blit(startScreenImage, (0, 0))

  # Draw start button
  draw_button("Start", (screen_width // 2 - 50, screen_height // 2 + 80), white, (100, 100, 100))

  # Update display
  pygame.display.flip()

# Quit Pygame
pygame.quit()