import pygame
from time import sleep
from Parkur.Classe import *
import Parkur.Classe

pygame.init()
def Timer():
    global s,m,h
    sleep(1)
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0
def New_Level():
        Parkur.Main.level += 1
#Spike = Object([size],[pos],None,r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spake№.png',None,None,'Obctacle')
#Lava = Object([size],[pos],None,r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Lava.png',None,None,'Obctacle')    
#Plat = Object([size],[pos],None,r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat')
#End = Object([size],[pos],None,r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'End')
level1 = [
    Object([2000,50],[-500,475],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Lava.png',None,None,'Obctacle'),
    Object([118,15],[1,364],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([50,5],[200,341],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([50,5],[300,300],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([100,15],[400,225],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([25,10],[650,350],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([25,25],[425,200],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([25,25],[450,200],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([25,25],[475,200],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([25,10],[800,300],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\End.png',None,None,'End')
    ]
level2 = [
    Object([2000,50],[-500,475],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Lava.png',None,None,'Obctacle'),
    Object([15,5],[500,250],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Lava.png',None,None,'Button'),
    Object([15,5],[500,250],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Lava.png',None,None,'Plat'),
    Object([25,10],[800,300],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([50,10],[50,100],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\End.png',None,None,'End')
    ]
def Load_Level(level,win,Player):
    global level1,plats1
    if level == 1:
      Plat_p(level1)
      for i in level1:
        i.Update('',Player,level,None,None)
        win.blit(i.image,(i.pos[0],i.pos[1]))
    elif level == 2:
        Parkur.Main.Player.start_pos = [800,250]
        Plat_p(level2)
        for i in level2:
            i.Update('',Player,level,level2,2,1)
            win.blit(i.image,(i.pos[0],i.pos[1]))
def Plat_p(plats):
    #global Player
    for i in plats:
        if i.p == True:
            Parkur.Main.Player.touch = True
            break
        else:
            Parkur.Main.Player.touch = False