import pygame
import sys
from pygame import QUIT
import time

pygame.init()

HEIGHT=600
WIDTH=800

screen=pygame.display.set_mode((WIDTH,HEIGHT))
player=pygame.Rect((300,250,50,50))

run=True
while run==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    pygame.draw.rect(screen,(255,0,0),player)
    
    pygame.display.update()


pygame.quit
