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

volume = 0.5
def options_window(run_menu):
    global volume
    options_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        options_screen.fill((0, 0, 0))
        options_screen.blit(pygame.image.load('font/menu_background_no_light.jpg'), (0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("Volume: " + str(volume), True, (255, 255, 255))
        options_screen.blit(text, (50, 50))

        pygame.draw.rect(options_screen, (255, 255, 255), pygame.Rect(50, 100, 200, 30))
        pygame.draw.rect(options_screen, (0, 255, 0), pygame.Rect(52 + volume * 196, 102, 16, 26))
        pygame.draw.rect(options_screen, (255, 0, 0), pygame.Rect(50, 200, 200, 50))
        text = font.render("Back", True, (255, 255, 255))
        options_screen.blit(text, (85, 215))
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                if pygame.Rect(50, 200, 200, 50).collidepoint(mouse_pos):
                    run_menu()
                if pygame.Rect(50, 100, 200, 30).collidepoint(mouse_pos):
                    volume = (mouse_pos[0] - 50) / 196
                    pygame.mixer.music.set_volume(volume)  # Update the volume

        pygame.display.update()
    pygame.quit()
