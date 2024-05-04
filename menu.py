import pygame
import sys
from pygame.locals import *

WIDTH, HEIGHT = 1200,650

class Menu:
    def __init__(self, screen, options):
        self.screen = screen
        self.options = options
        self.selected_option = 0
        self.mouse_over_option = None
        self.using_mouse = False
        self.font = pygame.font.Font('font/Buycat.ttf', 52)

    def display_menu(self):
        self.screen.fill((0, 0, 0))
        mouse_pos = pygame.mouse.get_pos()
        for index, option in enumerate(self.options):
            text_surface = self.font.render(option, True, (255, 255, 255))
            screen_width, screen_height = self.screen.get_size()
            text_rect = text_surface.get_rect(center=(screen_width // 2.1, screen_height // 3 + index * 100))
            if (self.using_mouse and index == self.mouse_over_option) or (not self.using_mouse and index == self.selected_option):
                text_surface = self.font.render(option, True, (128, 128, 128))  # Change the color to gray
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
                        text_rect = text_surface.get_rect(center=(WIDTH//2.1, HEIGHT// 3 + index * 100))
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

