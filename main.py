import pygame
import sys
from pygame import QUIT
import os
import math
from functions import *
import random
import time
from menu import Menu
from pygame import mixer

#trouve le chemin d'acces pour les sprites pour pouvoir les utiliser
script_path = os.path.abspath(sys.argv[0]).replace("main.py","")
#background image
background_image = pygame.image.load(os.path.join(script_path, 'font/menu_background_no_light.jpg'))

#background music
nom_music_background="sons/Firelight.mp3"
chemin_music_background=os.path.join(script_path,nom_music_background)
play_background_music(chemin_music_background)

#Load the bird hit sound
nom_bird_hit_sound="sons/raven-caw-caw.mp3"
chemin_bird_hit_sound = os.path.join(script_path, nom_bird_hit_sound)
bird_hit_sound = mixer.Sound(chemin_bird_hit_sound)

# Load the ground hit sound
nom_ground_hit_sound = "sons/punch-sound-effect-meme.mp3"
chemin_ground_hit_sound = os.path.join(script_path, nom_ground_hit_sound)
ground_hit_sound = mixer.Sound(chemin_ground_hit_sound)

nom_player="Player/Frame0000.png"
chemin_player=os.path.join(script_path,nom_player)
nom_sky="map/background.png"
chemin_sky=os.path.join(script_path,nom_sky)
nom_sol="map/base_sol_3.png"
chemin_sol=os.path.join(script_path,nom_sol)
nom_arrow="map/pngwing.com.png"
chemin_arrow=os.path.join(script_path,nom_arrow)
nom_jauge="jauge_stp.png"
chemin_jauge=os.path.join(script_path,nom_jauge)
nom_montain="map/mountain.png"
chemin_mountain=os.path.join(script_path,nom_montain)
nom_sentier="map/sand_2.png"
chemin_sentier=os.path.join(script_path,nom_sentier)
nom_bar="map/buttonLong_brown.png"
chemin_bar=os.path.join(script_path,nom_bar)

pygame.font.init()
font_test = pygame.font.Font(os.path.join(script_path, 'font/Buycat.ttf'), 36)

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
Bird_rect=Bird.get_rect()

player=pygame.image.load(chemin_player)
player=pygame.transform.scale(player,(150,100))
player_rect=player.get_rect(bottomleft=(WIDTH//3,sentier_rect.top+280))

jauge=pygame.image.load(chemin_jauge)
jauge_rect=jauge.get_rect(bottomleft=(100,HEIGHT))


bar=pygame.image.load(chemin_bar)
bar=pygame.transform.scale(bar,(50,10))
bar_rect=bar.get_rect(bottomleft=(180,HEIGHT*1/3))
jauge_activated=True
move_bar=15


screen=pygame.display.set_mode((WIDTH,HEIGHT))
clock=pygame.time.Clock()

# Variables : 
is_in_trajectory=False
compute_trajectory=True
rebound=False
tmp_rebound=False

ValeurDefilementGlobale=7

angle = 0
rotation_speed = 4
number_of_rebound=1
Score=0
count_score=0

scrollsky=0
scrollmountain=0
scrollground=0
scrollsentier=0

BirdHere=False
print_bird_hit=False
Bird_collision=0
FramePlayer=0

value_x=0
value_y=0

angle_rotation=0

slides=math.ceil(WIDTH / WIDTH) + 1



# Options for the menu
menu_options = ['Play', 'Options', 'Quit']
menu = Menu(screen, menu_options, background_image)
ValeurDefilementGlobale=7
run = True
# Function to run the menu
def run_menu():
    global player,run,FramePlayer, is_in_trajectory, scrollsky, scrollmountain, scrollground, scrollsentier, BirdHere, Bird_collision, count_score, print_bird_hit, Bird_rect, player_rect, arrow_activated, jauge_activated, angle, number_of_rebound, Score, value_x, value_y, slides, ValeurDefilementGlobale, compute_trajectory, rebound, tmp_rebound, BirdHere, Bird_collision, count_score, print_bird_hit, Bird_rect, player_rect, arrow_activated, jauge_activated, angle, number_of_rebound, Score, value_x, value_y, slides, ValeurDefilementGlobale, compute_trajectory, rebound, tmp_rebound, move_bar, rotation_speed, Bird
    option = menu.run()
    if option == 0:  # Play
        print("Starting the game...")
        player_on_ground = True # Add a flag to check if the player is already on the ground
        PLAY_GROUND_HIT_SOUND = pygame.USEREVENT + 1  # Custom event for playing the ground hit sound
        while run == True:
            clock.tick(60)
            if(run):
                if is_in_trajectory is False:
                    ValeurDefilementGlobale=0
                else: 
                    Score+=1
                    if ValeurDefilementGlobale<3:
                        ValeurDefilementGlobale=3
                    ValeurDefilementGlobale+=0.1
                    if random.randint(0,200)==100 and BirdHere==False:
                        BirdHere=True
                        BirdI=0
                        Bird_rect.x=2000
                        Bird_rect.y=random.randint(0,400)
                    if 0<=FramePlayer<5:
                        player=pygame.transform.scale(pygame.image.load(os.path.join('Player','Frame0000.png')), (150, 100))
                    if 5<=FramePlayer<10:
                        player=pygame.transform.scale(pygame.image.load(os.path.join('Player','Frame0001.png')), (150, 100))
                    if 10<=FramePlayer<15:
                        player=pygame.transform.scale(pygame.image.load(os.path.join('Player','Frame0002.png')), (150, 100))
                    if 15<=FramePlayer<20:
                        player=pygame.transform.scale(pygame.image.load(os.path.join('Player','Frame0003.png')), (150, 100))
                    if 20<=FramePlayer<25:
                        player=pygame.transform.scale(pygame.image.load(os.path.join('Player','Frame0004.png')), (150, 100))
                    if 25<=FramePlayer<30:
                        player=pygame.transform.scale(pygame.image.load(os.path.join('Player','Frame0005.png')), (150, 100))
                    if 30<=FramePlayer<35:
                        player=pygame.transform.scale(pygame.image.load(os.path.join('Player','Frame0006.png')), (150, 100))
                    if 35<=FramePlayer<40:
                        player=pygame.transform.scale(pygame.image.load(os.path.join('Player','Frame0007.png')), (150, 100))
                    if 40<=FramePlayer<45:
                        player=pygame.transform.scale(pygame.image.load(os.path.join('Player','Frame0008.png')), (150, 100))
                    if 45<=FramePlayer<50:
                        player=pygame.transform.scale(pygame.image.load(os.path.join('Player','Frame0009.png')), (150, 100))
                    if 50<=FramePlayer<55:
                        player=pygame.transform.scale(pygame.image.load(os.path.join('Player','Frame0010.png')), (150, 100))
                    if 55<=FramePlayer<60:
                        player=pygame.transform.scale(pygame.image.load(os.path.join('Player','Frame0011.png')), (150, 100))
                    if 60<=FramePlayer<65:
                        player=pygame.transform.scale(pygame.image.load(os.path.join('Player','Frame0012.png')), (150, 100))

                    elif FramePlayer>65:
                        FramePlayer=0
                    FramePlayer += 1
                    #print(FramePlayer)
                    FramePlayer += 1

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
                    screen.blit(Bird,Bird_rect)
                    Bird_rect.x-=ValeurDefilementGlobale*1.3
                    Bird_rect.y+=random.randint(-1 ,1)
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
                    if Bird_rect.x<-100:
                        BirdHere=False

                if player_rect.colliderect(Bird_rect) and Bird_collision>50:
                    Score+=100
                    Bird_collision=0
                    count_score=100
                    #play the bird hit sound
                    bird_hit_sound.play()

                if ValeurDefilementGlobale==0:
                    BirdHere=False

            keys=pygame.key.get_pressed()
            for event in pygame.event.get(): #check si la touche échap est pressée et quitte le jeu si c'est le cas
                if event.type==pygame.QUIT :
                    run=False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        run_menu() # Retourne au menu 
                
                if event.type == PLAY_GROUND_HIT_SOUND:
                    ground_hit_sound.play()

            if keys[pygame.K_SPACE] and jauge_activated==True: # calcule la valeur de la jauge lorsque la touche aspace est pressée
                strenght_value=(HEIGHT-bar_rect.y)/20
                strenght_value=round(strenght_value, 2)
                jauge_activated=False
                
            if keys[pygame.K_RETURN] and arrow_activated==True and jauge_activated==False: # calcule la valuer de l'angle quand la touche entrée est pressé
                angle_value=angle
                arrow_activated=False

            if keys[pygame.K_r]: # reset le jeu
                if is_in_trajectory is False:
                    angle=0
                    angle_value=0
                    
                    jauge_activated=True
                    arrow_activated=True
                    player_rect.bottomleft=(WIDTH//3,sentier_rect.top+280)
                    rebound=False
                    tmp_rebound=False
                    number_of_rebound=1
                    Score=0
                    count_score=0
                    print_bird_hit=False
                    Bird_collision=0
                    BirdHere=False
                    value_x=0
                    value_y=0
                    slides=math.ceil(WIDTH / WIDTH) + 1
                    compute_trajectory=True
                    ValeurDefilementGlobale=7

            screen.blit(player,player_rect)

            if jauge_activated:
                if(bar_rect.bottom>=jauge_rect.bottom-240 or bar_rect.top<=jauge_rect.top+140):
                    move_bar*=-1
                bar_rect.bottom+=move_bar
                #print("     ", bar_rect.bottom,"  \n", jauge_rect.bottom)
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
                text1 = font_test.render(f"Strength : {strenght_value}", True, (255, 255, 255))
                screen.blit(text1, (10, 10))
            if arrow_activated is False: #affiche l'angle sur l'écran
                text2 = font_test.render(f"Angle : {angle}", True, (255, 255, 255))
                text3=font_test.render(f"Score : {Score}",True,(255, 255, 255))
                text4=font_test.render("+100",True,(255, 255, 255))
                if count_score>0:
                    print_bird_hit=True
                    count_score-=1
                else:
                    print_bird_hit=False
                if print_bird_hit:
                    screen.blit(text4,(700,10))
                screen.blit(text2, (290, 10))
                screen.blit(text3,(490,10))
                
            
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
                player_rect.bottomleft=tmp_value_x,HEIGHT-pos_y[value_y]*400
                value_x+=1
                value_y+=1
                if strenght_value/number_of_rebound<3 or angle/number_of_rebound<15:
                    rebound=True
                    ValeurDefilementGlobale=0
                    is_in_trajectory=False
                if value_x==len(pos_x):
                    value_x=0
                    value_y=0
                    compute_trajectory=False
                    number_of_rebound+=0.25
                    ValeurDefilementGlobale-=3.75

            # Check if the player hits the ground
            if player_rect.bottom >= resized_ground_rect.top:
                if not player_on_ground:  # Play the sound only if the player is not already on the ground
                    # Remove the lines that reset the player's position or affect the game's flow

                    # Schedule the custom event to play the ground hit sound
                    pygame.time.set_timer(PLAY_GROUND_HIT_SOUND, 100, 1)

                player_on_ground = True  # Update the flag

            else:
                player_on_ground = False  # Update the flag

            Bird_collision+=1
            pygame.display.update()#update le display géneral
    elif option == 1:  # Options
        print("Opening options...")
        options_window(run_menu, background_image, bird_hit_sound, ground_hit_sound)
    elif option == 2:  # Quit
        print("Quitting the game...")
        pygame.quit()
        sys.exit()
        
run_menu()
