import pygame
import sys
from pygame import QUIT
import os
import math

#trouve le chemin d'acces pour les sprites pour pouvoir les utiliser
script_path = os.path.abspath(sys.argv[0]).replace("main.py","") 
nom_player="player_stand.png"
chemin_player=os.path.join(script_path,nom_player)
nom_sky="background.png"
chemin_sky=os.path.join(script_path,nom_sky)
nom_sol="base_sol_3.png"
chemin_sol=os.path.join(script_path,nom_sol)
nom_arrow="pngwing.com.png"
chemin_arrow=os.path.join(script_path,nom_arrow)
nom_jauge="buttonLong_brown.png"
chemin_jauge=os.path.join(script_path,nom_jauge)
nom_montain="mountain.png"
chemin_mountain=os.path.join(script_path,nom_montain)
nom_sentier="sand_1.png"
chemin_sentier=os.path.join(script_path,nom_sentier)

pygame.font.init()
font_test = pygame.font.Font(None, 36)  

pygame.init()
screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h #utilise une fonction prédéfinie pour obtenir la taille de l'écran et mettre le jeu en full screen

sky_surface=pygame.image.load(chemin_sky)
resized_sky = pygame.transform.scale(sky_surface, (WIDTH, HEIGHT-100)) #load le png du fond et le resize
resized_sky_rect=resized_sky.get_rect(topleft=(0,0))

sentier=pygame.image.load(chemin_sentier)
sentier_rect=sentier.get_rect(topleft=(0,420))

mountain=pygame.image.load(chemin_mountain)
mountain_rect=mountain.get_rect(topleft=(0,370))

ground=pygame.image.load(chemin_sol)
resized_ground = pygame.transform.scale(ground, (WIDTH,300))
resized_ground_rect=resized_ground.get_rect(topleft=(0,HEIGHT-300)) # load le png du sol et le resize

arrow=pygame.image.load(chemin_arrow)
resized_arrow=pygame.transform.scale(arrow,(200,100))
arrow_rect = resized_arrow.get_rect(bottomleft=(100, HEIGHT*2/3))
arrow_activated=True


player=pygame.image.load(chemin_player)
player_rect=player.get_rect(bottomleft=(WIDTH//3,sentier_rect.top+265))

jauge=pygame.image.load(chemin_jauge)
jauge_rect=jauge.get_rect(bottomleft=(100,HEIGHT*2/3))

bar=pygame.transform.scale(jauge,(50,10))
bar_rect=bar.get_rect(bottomleft=(180,HEIGHT*2/3))
jauge_activated=True
move_bar=15


screen=pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)
clock=pygame.time.Clock()


ValeurDefilementGlobale=5
run=True
angle = 0
rotation_speed = 4

scrollsky=0
scrollground=0
slides=math.ceil(screen_info.current_w / WIDTH) + 1
while run==True:
    clock.tick(60)

    for i in range(0,slides+1):
        screen.blit(resized_sky,(i * screen_info.current_w+scrollsky, 0))
    scrollsky-=ValeurDefilementGlobale
    if abs(scrollsky)>screen_info.current_w:
        scrollsky=0

    for i in range(0,slides+1):
        screen.blit(resized_ground,(i * screen_info.current_w+scrollground, HEIGHT-100))
    scrollground-=ValeurDefilementGlobale*1.2
    if abs(scrollground)>screen_info.current_w:
        scrollground=0

    keys=pygame.key.get_pressed()
    for event in pygame.event.get(): #check si la touche échap est pressée et quitte le jeu si c'est le cas
        if event.type==pygame.QUIT :
            run=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False 



    if keys[pygame.K_UP]:# fait une sorte de gravité, pas neccessaire en fonction de la future fonction trajectoire
        player_rect.y-=15

    if keys[pygame.K_SPACE] and jauge_activated==True: # calcule la valeur de la jauge lorsque la touche aspace est pressée
        strenght_value=5-4*(bar_rect.y-jauge_rect.top)/(jauge_rect.bottom-jauge_rect.top)
        strenght_value=round(strenght_value, 2)
        jauge_activated=False
        
    if keys[pygame.K_RETURN] and arrow_activated==True and jauge_activated==False: # calcule la valuer de l'angle quand la touche entrée est pressé
        angle_value=angle
        arrow_activated=False


    screen.blit(mountain,mountain_rect)
    screen.blit(player,player_rect)
    screen.blit(sentier,sentier_rect)#update le display du joueur et du background

    if jauge_activated:
        if(bar_rect.bottom==jauge_rect.bottom or bar_rect.top==jauge_rect.top):
            move_bar*=-1
        bar_rect.bottom+=move_bar
        screen.blit(jauge,jauge_rect)
        screen.blit(bar,bar_rect)#fait monter et descendre la jauge pour la puissance

    if (jauge_activated)is False and arrow_activated is True:
        if angle > 90 or angle < 0:
            rotation_speed *= -1
        angle += rotation_speed
        rotated_arrow = pygame.transform.rotate(resized_arrow, angle)
        rotated_rect = rotated_arrow.get_rect(center=arrow_rect.center)
        screen.blit(rotated_arrow, rotated_rect.topleft)# affiche la fleche pour l'angle quand la jauge pour la puissance disparait

    if jauge_activated is False:#affiche la force sur l'écran
        text1 = font_test.render(f"Strenght : {strenght_value}", True, (255, 0, 0))
        screen.blit(text1, (10, 10))
    if arrow_activated is False: #affiche l'angle sur l'écran
        text2 = font_test.render(f"Angle : {angle}", True, (255, 0, 0))
        screen.blit(text2, (200, 10))

    pygame.display.update()#update le display géneral


pygame.quit()