import pygame


class Button:
    STANDARD_WIDTH = 200
    STANDARD_HEIGHT = 60

    def __init__(self, x, y, text, color=(50, 150, 255), hover_color=(30, 130, 235), click_color=(10, 110, 215)):
        """
        Initialize a Button.

        :param x: X Position
        :param y: Y Position
        :param text: Button Label
        :param font: Custom Font (pygame.font.Font)
        :param color: Default Button Color
        :param hover_color: Hover Color
        :param click_color: Click Color
        """
        self.rect = pygame.Rect(x, y, self.STANDARD_WIDTH, self.STANDARD_HEIGHT)
        self.default_color = color
        self.hover_color = hover_color
        self.click_color = click_color
        self.current_color = self.default_color
        self.text = text
        self.clicked = False
        self.font = pygame.font.Font(None, 40)

    def draw(self, screen):
        """Draw the button with hover and click effects."""
        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=15)

        # Render text
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_events(self, event):
        """Handle hover and click events."""
        mouse_pos = pygame.mouse.get_pos()

        # Hover effect
        if self.rect.collidepoint(mouse_pos):
            self.current_color = self.hover_color
        else:
            self.current_color = self.default_color

        # Click effect
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.current_color = self.click_color
            self.clicked = True
        
        elif event.type == pygame.MOUSEBUTTONUP and self.clicked:
            self.clicked = False

    def is_clicked(self, event):
        """Returns True if button is clicked."""
        return event.type == pygame.MOUSEBUTTONDOWN and self.clicked and self.rect.collidepoint(event.pos)
