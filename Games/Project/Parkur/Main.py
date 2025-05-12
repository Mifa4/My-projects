import pygame
from Methods import *
import Methods
from Classe import *
import Classe

def Parkur_Time(level):
    pygame.init()
    w,h = 1000,500
    win = pygame.display.set_mode((w,h))
    Player = Object([50,50],[0,0], [0, 0],r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\PlayerT1.png',r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\PlayerT2.png',True,'')
    Box = Object([50,50],[0,h-10],[0,h-10], r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Boxes\Textures\Box.png',None,None,'Plat')
    level = 1
    FPS = 60
    clock = pygame.time.Clock()
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
        win.fill((255,255,255))
        keys = pygame.key.get_pressed()
        Player.Mouve(5,keys)
        Player.Update(keys,'',level)
        #Box.Update(keys,Player,level)
        win.blit(Player.image,(Player.pos[0],Player.pos[1]))
        Load_Level(level,win,Player)
        pygame.display.update()
        clock.tick(FPS)