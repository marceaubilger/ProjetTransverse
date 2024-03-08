import pygame
import sys
from pygame import QUIT
import os
import math
from functions import *
import random

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
WIDTH, HEIGHT = 1200,650

sky_surface=pygame.image.load(chemin_sky)
resized_sky = pygame.transform.scale(sky_surface, (WIDTH, HEIGHT-100)) #load le png du fond et le resize
resized_sky_rect=resized_sky.get_rect(topleft=(0,0))

sentier=pygame.image.load(chemin_sentier)
resized_sentier = pygame.transform.scale(sentier, (WIDTH,300))
sentier_rect=sentier.get_rect(topleft=(0,350))

mountain=pygame.image.load(chemin_mountain)
resized_mountain = pygame.transform.scale(mountain, (WIDTH,300))
mountain_rect=mountain.get_rect(topleft=(0,300))

ground=pygame.image.load(chemin_sol)
resized_ground = pygame.transform.scale(ground, (WIDTH,300))
resized_ground_rect=resized_ground.get_rect(topleft=(0,HEIGHT-300)) # load le png du sol et le resize

arrow=pygame.image.load(chemin_arrow)
resized_arrow=pygame.transform.scale(arrow,(200,100))
arrow_rect = resized_arrow.get_rect(bottomleft=(100, HEIGHT*2/3))
arrow_activated=True

Bird=pygame.image.load(os.path.join('obstacles','Bird','Walk1.png'))
Bird=pygame.transform.scale(Bird,(100,100))

player=pygame.image.load(chemin_player)
player_rect=player.get_rect(bottomleft=(WIDTH//3,sentier_rect.top+280))

jauge=pygame.image.load(chemin_jauge)
jauge_rect=jauge.get_rect(bottomleft=(100,HEIGHT*2/3))

bar=pygame.transform.scale(jauge,(50,10))
bar_rect=bar.get_rect(bottomleft=(180,HEIGHT*2/3))
jauge_activated=True
move_bar=15


screen=pygame.display.set_mode((WIDTH,HEIGHT))
clock=pygame.time.Clock()

is_in_trajectory=False
compute_trajectory=True
rebound=False
tmp_rebound=False

ValeurDefilementGlobale=7
run=True
angle = 0
rotation_speed = 4
number_of_rebound=1

scrollsky=0
scrollmountain=0
scrollground=0
scrollsentier=0

BirdHere=False

value_x=0
value_y=0

slides=math.ceil(WIDTH / WIDTH) + 1
while run==True:
    clock.tick(60)
    if(is_in_trajectory):
        for i in range(0,slides+1):
            screen.blit(resized_sky,(i * WIDTH+scrollsky, 0))
        scrollsky-=ValeurDefilementGlobale
        if abs(scrollsky)>WIDTH:
            scrollsky=0

        for i in range(0,slides+1):
            screen.blit(resized_mountain,(i * WIDTH+scrollmountain, 300))
        scrollmountain-=ValeurDefilementGlobale*1.2
        if abs(scrollmountain)>WIDTH:
            scrollmountain=0

        for i in range(0,slides+1):
            screen.blit(resized_ground,(i * WIDTH+scrollground, HEIGHT-300))
        scrollground-=ValeurDefilementGlobale*1.2
        if abs(scrollground)>WIDTH:
            scrollground=0

        for i in range(0,slides+1):
            screen.blit(resized_sentier,(i * WIDTH+scrollsentier, HEIGHT-300))
        scrollsentier-=ValeurDefilementGlobale*2
        if abs(scrollsentier)>WIDTH:
            scrollsentier=0

        if BirdHere==True:
            BirdI+=1
            screen.blit(Bird,(Bird_x,Bird_y))
            Bird_x-=ValeurDefilementGlobale*1.3
            Bird_y+=random.randint(-1 ,1)
            if 0<=BirdI<5:
                Bird=pygame.transform.scale(pygame.image.load(os.path.join('obstacles', 'Bird', 'Walk1.png')), (100, 100))
            elif 5<=BirdI<10:
                Bird=pygame.transform.scale(pygame.image.load(os.path.join('obstacles', 'Bird', 'Walk2.png')), (100, 100))
            elif 10<=BirdI<15:
                Bird=pygame.transform.scale(pygame.image.load(os.path.join('obstacles', 'Bird', 'Walk3.png')), (100, 100))
            elif 15<=BirdI<20:
                Bird=pygame.transform.scale(pygame.image.load(os.path.join('obstacles', 'Bird', 'Walk4.png')), (100, 100))
            elif 20<=BirdI<25:
                Bird=pygame.transform.scale(pygame.image.load(os.path.join('obstacles', 'Bird', 'Walk5.png')), (100, 100))
            elif 25<=BirdI<30:
                Bird=pygame.transform.scale(pygame.image.load(os.path.join('obstacles', 'Bird', 'Walk6.png')), (100, 100))
            else:
                BirdI=0
            print(BirdI)
            if Bird_x<-100:
                BirdHere=False

        if not ValeurDefilementGlobale==0:

            if random.randint(0,200)==100 and BirdHere==False:
                BirdHere=True
                BirdI=0
                Bird_x=2000
                Bird_y=random.randint(0,400)

        if ValeurDefilementGlobale==0:
            BirdHere=False
    else:
        screen.blit(resized_sky,resized_sky_rect)
        screen.blit(mountain,mountain_rect)
        screen.blit(resized_ground,resized_ground_rect)
        screen.blit(resized_sentier,sentier_rect)
        screen.blit(player,player_rect)


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
        strenght_value=(HEIGHT-bar_rect.y)/20
        strenght_value=round(strenght_value, 2)
        jauge_activated=False
        
    if keys[pygame.K_RETURN] and arrow_activated==True and jauge_activated==False: # calcule la valuer de l'angle quand la touche entrée est pressé
        angle_value=angle
        arrow_activated=False

    screen.blit(player,player_rect)

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
    
    if arrow_activated is False and jauge_activated is False and rebound is False:
        is_in_trajectory=True
        if compute_trajectory:
            compute_trajectory=False
            if angle==0:angle+=1
            total_time, time_interval=compute_time_parameters(strenght_value, angle, precision=0.01)
            pos_x, pos_y=trajectory(angle, strenght_value, total_time, time_interval)

    if compute_trajectory is False and value_x<len(pos_x) and rebound is False:
        if compute_trajectory is False:
            total_time, time_interval=compute_time_parameters(strenght_value/number_of_rebound, angle/number_of_rebound, precision=0.01)
            pos_x, pos_y=trajectory(angle/number_of_rebound, strenght_value/number_of_rebound, total_time, time_interval)
            compute_trajectory=True
        tmp_value_x,tmp_value_y=player_rect.bottomleft
        player_rect.bottomleft=tmp_value_x,HEIGHT-pos_y[value_y]*300
        value_x+=1
        value_y+=1
        if strenght_value/number_of_rebound<3 or angle/number_of_rebound<15:
            rebound=True
            ValeurDefilementGlobale=0
        if value_x==len(pos_x):
            value_x=0
            value_y=0
            compute_trajectory=False
            number_of_rebound+=0.25

    # if tmp_rebound:
    #     value_x=0
    #     value_y=0
    #     rebound=True
    #     tmp_rebound=False

    # if rebound is True and value_x<len(pos_x):
    #     total_time, time_interval=compute_time_parameters(strenght_value/1.5, angle/1.2, precision=0.01)
    #     pos_x, pos_y=trajectory(angle/1.2, strenght_value/1.5, total_time, time_interval)  
    #     tmp_value_x,tmp_value_y=player_rect.bottomleft
    #     player_rect.bottomleft=tmp_value_x,HEIGHT-pos_y[value_y]*300
    #     value_x+=1
    #     value_y+=1

    
    pygame.display.update()#update le display géneral


pygame.quit()
