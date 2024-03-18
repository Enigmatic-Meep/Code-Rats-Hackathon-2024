import pygame

class Button:
    def __init__(self, text, pos, color, click_color, click_function=None):
        self.text = text
        self.pos = pos
        self.color = color
        self.click_color = click_color
        self.click_function = click_function
        self.font = pygame.font.Font(None, 40)  # Choose a font

        # Pre-render text for efficiency
        self.text_surface = self.font.render(self.text, True, self.color)
        self.button_width = self.text_surface.get_width() + 20
        self.button_height = self.text_surface.get_height() + 10
        self.button_rect = pygame.Rect(pos[0], pos[1], self.button_width, self.button_height)

    def draw(self, screen):
        # Check for hover and change color
        mouse_pos = pygame.mouse.get_pos()
        mouse_over = self.button_rect.collidepoint(mouse_pos)
        color = self.click_color if mouse_over else self.color

        # Draw text (avoid redundant rendering)
        screen.blit(self.text_surface, (self.button_rect.x + 5, self.button_rect.y + 5))

        # Optionally draw rectangle outline
        # pygame.draw.rect(screen, color, self.button_rect, 2)  # Uncomment to show outline

    def handle_click(self, event):
        if self.click_function:
            if event.type == pygame.MOUSEBUTTONDOWN:  # Check for button press
                self.click_function()