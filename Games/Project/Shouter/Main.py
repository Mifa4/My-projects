import pygame
from Methods import *
import Methods
from Classe import *
import Classe

pygame.init()
w,h = 500,500

win = pygame.display.set_mode((w,h))
Player = Object([50,50],[0,0],r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\PlayerT1.png',r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\PlayerT2.png')
FPS = 60
clock = pygame.time.Clock()
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    win.fill((255,255,255))
    keys = pygame.key.get_pressed()
    Player.Mouve(5,keys)
    win.blit(Player.image,(Player.pos[0],Player.pos[1]))
    pygame.display.update()
    clock.tick(FPS)