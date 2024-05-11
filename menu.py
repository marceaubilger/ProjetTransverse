import pygame
import sys
from pygame.locals import *

WIDTH, HEIGHT = 1200,650

class Menu:

    def __init__(self, screen, options, background_image):
        self.screen = screen
        self.options = options
        self.background_image = background_image
        self.selected_option = 0
        self.mouse_over_option = None
        self.using_mouse = False
        self.font = pygame.font.Font('font/Buycat.ttf', 52)
        self.title_font = pygame.font.Font('font/Buycat.ttf', 100)
        self.title = self.title_font.render("My Game", True, (255, 255, 255))

        # Scale the background image to fit the screen size
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))

    def display_menu(self):
        # Draw the background image
        self.screen.blit(self.background_image, (0, 0))

        # Draw the title
        screen_width, screen_height = self.screen.get_size()
        title_rect = self.title.get_rect(center=(screen_width // 2.1, screen_height // 6))

        # Create a black shadow effect for the title
        black_title = self.title_font.render("My Game", True, (0, 0, 0))
        black_title_rect = black_title.get_rect(center=(title_rect.centerx + 2, title_rect.centery + 2))
        self.screen.blit(black_title, black_title_rect)

        # Blit the original title on top of the shadow
        self.screen.blit(self.title, title_rect)

        # Draw the options
        mouse_pos = pygame.mouse.get_pos()
        for index, option in enumerate(self.options):
            text_surface = self.font.render(option, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(screen_width // 2.1, screen_height // 2.8 + index * 100))

            # Create a black shadow effect for the options
            black_text = self.font.render(option, True, (0, 0, 0))
            black_text_rect = black_text.get_rect(center=(text_rect.centerx + 2, text_rect.centery + 2))
            self.screen.blit(black_text, black_text_rect)

            if (self.using_mouse and index == self.mouse_over_option) or (not self.using_mouse and index == self.selected_option):
                text_surface = self.font.render(option, True, (128, 128, 128))  # Change the color to gray

            # Blit the original text on top of the shadow
            self.screen.blit(text_surface, text_rect)

    def run(self):
        while True:
            self.display_menu()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    self.using_mouse = False
                    if event.key == K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                        self.mouse_over_option = None
                    elif event.key == K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                        self.mouse_over_option = None
                    elif event.key == K_RETURN:
                        return self.selected_option
                elif event.type == MOUSEMOTION:
                    # Get the position of the mouse
                    mouse_pos = pygame.mouse.get_pos()
                    # Check if the mouse is over any of the options
                    for index, option in enumerate(self.options):
                        text_surface = self.font.render(option, True, (255, 255, 255))
                        text_rect = text_surface.get_rect(center=(WIDTH//2.1, HEIGHT// 2.9 + index * 100))
                        if text_rect.collidepoint(mouse_pos):
                            self.mouse_over_option = index
                            break
                    else:
                        self.mouse_over_option = None
                elif event.type == MOUSEBUTTONDOWN:
                    self.using_mouse = True
                    # Get the position of the mouse click
                    mouse_pos = pygame.mouse.get_pos()
                    # Check if the click was inside any of the options
                    for index, option in enumerate(self.options):
                        text_surface = self.font.render(option, True, (255, 255, 255))
                        text_rect = text_surface.get_rect(center=(WIDTH//2.1, HEIGHT// 3 + index * 100))
                        if text_rect.collidepoint(mouse_pos):
                            self.selected_option = index
                            self.mouse_over_option = None
                            return self.selected_option

