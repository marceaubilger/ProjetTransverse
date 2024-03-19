import pygame
import sys
from pygame.locals import *

class Menu:
    def __init__(self, screen, options):
        self.screen = screen
        self.options = options
        self.selected_option = 0
        self.font = pygame.font.Font(None, 36)

    def display_menu(self):
        self.screen.fill((0, 0, 0))
        for index, option in enumerate(self.options):
            text_surface = self.font.render(option, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(400, 200 + index * 50))
            if index == self.selected_option:
                pygame.draw.rect(self.screen, (255, 0, 0), text_rect, 2)
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
                    if event.key == K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == K_RETURN:
                        return self.selected_option
                    


