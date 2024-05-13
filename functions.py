import pygame
import sys
import math
import numpy as np
from pygame.locals import *

WIDTH, HEIGHT = 1200,650
value_x=0

def compute_time_parameters(strength, angle, precision=0.01):
    # Convert angle from degrees to radians
    angle_rad = np.deg2rad(angle)

    # Gravity constant (m/s^2)
    g = 25

    # Initial velocity components
    v_initial_y = strength * np.sin(angle_rad)

    # Compute time of flight
    total_time = (2 * v_initial_y) / g

    # Compute number of steps
    num_steps = int(total_time / precision)

    # Compute time interval
    time_interval = total_time / num_steps

    return total_time, time_interval


def trajectory(angle, initial_speed, total_time, time_interval):
    angle_radians = math.radians(angle)
    speed_x = initial_speed * np.cos(angle_radians)
    speed_y = initial_speed * np.sin(angle_radians)
    g = 25 #gravity

    #number of intervals of time
    number_of_points = int(total_time / time_interval)

    #initialization of lists to store the x and y coordinates of the trajectory
    pos_x = [0.0]
    pos_y = [0.0]

    #compute the trajectory
    for i in range(1, number_of_points + 1):
        #computation of the new position
        time = i * time_interval
        position_x = speed_x * time
        position_y = ((speed_y * time) - 0.5 *( g * time ** 2))

        #adding the position to the list
        pos_x.append(position_x)
        pos_y.append(position_y)

        if pos_y[-1] < 0:  # Check if the last element of pos_y is less than 0
            break

    return pos_x, pos_y

def play_background_music(music_path):
    pygame.mixer.init()
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)

def update_high_score(score):
    global high_score
    if score > high_score:
        high_score = score

def draw_text_with_outline(text, font, color, surface, x, y):
    outline_color = (0, 0, 0)  # Black outline color
    offsets = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]  # Create a list of offsets
    offsets.remove((0, 0))  # Remove the original position from the offsets

    for offset in offsets:
        text_surface = font.render(text, True, outline_color)
        surface.blit(text_surface, (x + offset[0], y + offset[1]))

    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))


volume = 0.1
def options_window(run_menu, background_image, bird_hit_sound, ground_hit_sound):
    global volume
    options_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        options_screen.blit(background_image, (0, 0))

        # Create a black shadow effect for the volume text
        font = pygame.font.Font('font/Buycat.ttf', 52)
        text = font.render("Volume: " + str(round(volume, 2)), True, (0, 0, 0))
        text_rect = text.get_rect(topleft=(52, 52))
        options_screen.blit(text, text_rect)

        # Blit the original volume text on top of the shadow
        text = font.render("Volume: " + str(round(volume, 2)), True, (255, 255, 255))
        text_rect = text.get_rect(topleft=(50, 50))
        options_screen.blit(text, text_rect)

        # Draw the background volume bar
        pygame.draw.rect(options_screen, (255, 255, 255), pygame.Rect(50, 100, 200, 30))

        # Draw the actual volume bar on top of the background bar
        pygame.draw.rect(options_screen, (255, 223, 0), pygame.Rect(52 + volume * 196, 102, 16, 26))

        # Create a black shadow effect for the back button text
        text = font.render("Back", True, (0, 0, 0))
        text_rect = text.get_rect(center=(87, 217))
        options_screen.blit(text, text_rect)

        # Blit the original back button text on top of the shadow
        text = font.render("Back", True, (255, 255, 255))
        text_rect = text.get_rect(center=(85, 215))
        options_screen.blit(text, text_rect)

        # display the key bindings of the game controls at the right side of the screen
        text = "Key Bindings :\n - M = menu\n - R = restart the game\n - Space = chose the strength of the shot\n - Enter = chose the angle of the shot\n - C = clear the high score"
        lignes = text.split("\n")

        for i, l in enumerate(lignes):
            # Draw the black outline
            text_black = font.render(l, True, (0, 0, 0))
            text_rect_black = text_black.get_rect(center=(WIDTH - 553, HEIGHT // 3.5 + i * 75))
            options_screen.blit(text_black, text_rect_black)

            # Draw the white text on top of the black outline
            text_white = font.render(l, True, (255, 255, 255))
            text_rect_white = text_white.get_rect(center=(WIDTH - 550, HEIGHT // 3.5 + i * 75))
            options_screen.blit(text_white, text_rect_white)


        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                if pygame.Rect(50, 200, 200, 50).collidepoint(mouse_pos):
                    run_menu()
                if pygame.Rect(50, 100, 200, 30).collidepoint(mouse_pos):
                    volume = (mouse_pos[0] - 50) / 196
                    volume = round(volume, 2)
                    pygame.mixer.music.set_volume(volume)
                    # Set the volume of all sound effects
                    bird_hit_sound.set_volume(volume)
                    ground_hit_sound.set_volume(volume)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run_menu()

        pygame.display.update()
    pygame.quit()
