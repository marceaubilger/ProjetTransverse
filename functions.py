import pygame
screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h

def load_screen():
    sky_surface=pygame.image.load("C:\ProjetTransverse\layer-1-sky.png")
    resized_sky = pygame.transform.scale(sky_surface, (WIDTH, HEIGHT-100))
    ground=pygame.image.load("C:\ProjetTransverse\ground.png")
    resized_ground = pygame.transform.scale(ground, (WIDTH,100))


def arrow_rotation(angle):
    arrow=pygame.image.load("C:\ProjetTransverse\pngwing.com.png")
    resized_arrow=pygame.transform.scale(arrow,(200,100))
    arrow_rect = resized_arrow.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    if angle > 90 or angle < 0:
        rotation_speed *= -1
    angle += rotation_speed
    rotated_arrow = pygame.transform.rotate(resized_arrow, angle)
    rotated_rect = rotated_arrow.get_rect(center=arrow_rect.center)