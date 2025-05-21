import pygame
from time import sleep
from Parkur.Classe import *
import Parkur.Classe

pygame.init()
def Timer():
    while True:
        sleep(1)
        Parkur.Main.sec += 1
        if Parkur.Main.sec == 60:
            Parkur.Main.sec = 0
            Parkur.Main.min += 1
        if Parkur.Main.min == 60:
            Parkur.Main.min = 0
            Parkur.Main.hours += 1
        if Parkur.Main.hours == 24:
            Parkur.Main.hours = 0
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
    Object([50,5],[350,300],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([100,15],[400,225],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([25,10],[650,350],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([25,25],[425,200],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([25,25],[450,200],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([25,25],[475,200],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([25,10],[800,300],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\End.png',None,None,'End')
    ]
level2 = [
    Object([2000,50],[-500,475],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Lava.png',None,None,'Obctacle'),
    Object([25,5],[715,395],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Lava.png',None,None,'Button'),
    Object([15,25],[500,375],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([25,10],[800,325],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([75,10],[700,325],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([75,15],[675,400],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([15,5],[500,400],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([45,10],[375,325],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([45,10],[275,275],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([100,10],[100,250],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([25,25],[100,225],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([25,25],[125,225],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([25,25],[375,300],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([25,25],[730,300],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([25,25],[700,300],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([50,10],[50,175],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\End.png',None,None,'End')
    ]
level3 = [
    Object([2000,50],[-500,475],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Lava.png',None,None,'Obctacle'),
    Object([25,5],[200,95],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Lava.png',None,None,'Button'),
    Object([15,175],[250,0],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Lava.png',None,None,'Obctacle'),

    Object([500,15],[0,0],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Hitbox.png',None,None,'Obctacle'),
    Object([500,5],[0,0],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'so'),
    Object([50,10],[0,5],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike4.png',None,None,'so'),
    Object([50,10],[50,5],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike4.png',None,None,'so'),
    Object([50,10],[100,5],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike4.png',None,None,'so'),
    Object([50,10],[150,5],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike4.png',None,None,'so'),
    Object([50,10],[200,5],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike4.png',None,None,'so'),
    Object([50,10],[250,5],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike4.png',None,None,'so'),
    Object([50,10],[300,5],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike4.png',None,None,'so'),
    Object([50,10],[350,5],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike4.png',None,None,'so'),
    Object([50,10],[400,5],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike4.png',None,None,'so'),
    Object([50,10],[450,5],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike4.png',None,None,'so'),

    Object([15,500],[0,0],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Hitbox.png',None,None,'Obctacle'),
    Object([15,500],[0,0],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'so'),
    Object([10,50],[15,0],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),
    Object([10,50],[15,50],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),
    Object([10,50],[15,100],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),
    Object([10,50],[15,150],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),
    Object([10,50],[15,200],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),
    Object([10,50],[15,250],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),
    Object([10,50],[15,300],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),
    Object([10,50],[15,350],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),
    Object([10,50],[15,400],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),
    Object([10,50],[15,450],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),

    Object([500,15],[0,175],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([25,15],[200,100],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([25,15],[550,180],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([25,15],[580,100],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([25,50],[580,0],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike4.png',None,None,'Obctacle'),
    Object([60,10],[740,400],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([60,10],[850,390],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([60,10],[850,400],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([60,10],[740,390],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([50,10],[800,400],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\End.png',None,None,'End')
]
level4 = [
    Object([2000,50],[-500,475],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Lava.png',None,None,'Obctacle'),
    Object([30,500],[500,0],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Hitbox.png',None,None,'Obctacle'),
    Object([15,50],[500,0],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),
    Object([15,50],[500,50],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),
    Object([15,50],[500,100],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),
    Object([15,50],[500,150],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),
    Object([15,50],[500,200],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),
    Object([15,50],[500,250],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),
    Object([15,50],[500,300],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),
    Object([15,50],[500,350],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),
    Object([15,50],[500,400],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),
    Object([15,50],[500,450],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike2.png',None,None,'so'),
    Object([15,50],[485,0],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike3.png',None,None,'so'),
    Object([15,50],[485,50],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike3.png',None,None,'so'),
    Object([15,50],[485,100],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike3.png',None,None,'so'),
    Object([15,50],[485,150],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike3.png',None,None,'so'),
    Object([15,50],[485,200],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike3.png',None,None,'so'),
    Object([15,50],[485,250],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike3.png',None,None,'so'),
    Object([15,50],[485,300],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike3.png',None,None,'so'),
    Object([15,50],[485,350],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike3.png',None,None,'so'),
    Object([15,50],[485,400],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike3.png',None,None,'so'),
    Object([15,50],[485,450],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike3.png',None,None,'so'),
    Object([50,10],[0,140],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([50,500],[0,150],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([50,10],[50,190],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([50,500],[50,200],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([50,10],[100,240],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([50,500],[100,250],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([50,10],[150,290],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([50,500],[150,300],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([50,10],[200,340],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([50,500],[200,350],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([50,10],[250,390],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([50,500],[250,400],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([50,10],[300,440],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([50,500],[300,450],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([50,10],[350,465],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Spike.png',None,None,'Obctacle'),
    Object([50,500],[350,475],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([50,500],[400,900],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Plat.png',None,None,'Plat'),
    Object([50,10],[425,450],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\End.png',None,None,'End'),
    Object([50,10],[800,450],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Teleport.png',None,None,'Teleport'),
]
level5 = [
    Object([1000,15],[0,485],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Lava.png',None,None,'Plat'),
    Object([25,15],[425,400],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\End.png',None,None,'Button'),
    Object([15,500],[500,0],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Lava.png',None,None,'Obctacle'),
    Object([15,500],[0,0],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Lava.png',None,None,'Obctacle'),
    Object([15,425],[100,0],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Lava.png',None,None,'Obctacle'),
    Object([15,500],[985,0],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Lava.png',None,None,'Obctacle'),
    Object([45,10],[300,475],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Teleport.png',None,None,'Teleport'),
    Object([45,10],[310,475],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Teleport.png',None,None,'Teleport'),
    Object([45,10],[450,475],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Teleport.png',None,None,'Teleport'),
    Object([45,10],[460,475],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\Teleport.png',None,None,'Teleport'),
    Object([45,10],[900,475],None,r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\plat.png',None,None,'Over'),
]
Lv5 = False
def Load_Level(level,win,Player):
    global level1,plats1,Lv5
    if level == 1:
      Plat_p(level1)
      for i in level1:
        i.Update('',Player,level,None,None,None)
        win.blit(i.image,(i.pos[0],i.pos[1]))
    elif level == 2:
        Parkur.Main.Player.start_pos = [800,250]
        Plat_p(level2)
        for i in level2:
            i.Update('',Player,level,level2,2,1)
            win.blit(i.image,(i.pos[0],i.pos[1]))
    elif level == 3:
        Parkur.Main.Player.start_pos = [50,125]
        Plat_p(level3)
        for i in level3:
            i.Update('',Player,level,level3,2,1)
            win.blit(i.image,(i.pos[0],i.pos[1]))
    elif level == 4:
        Parkur.Main.Player.start_pos = [800,350]
        Plat_p(level4)
        for i in level4:
            i.Update('',Player,level,None,None,None)
            win.blit(i.image,(i.pos[0],i.pos[1]))
    elif level == 5:
        Parkur.Main.Player.start_pos = [45,475]
        if Lv5 == False:
            Lv5 = True
            Parkur.Main.Player.pos = [50,475]
        Plat_p(level5)
        for i in level5:
            i.Update('',Player,level,level5,2,1)
            win.blit(i.image,(i.pos[0],i.pos[1]))
def Plat_p(plats):
    #global Player
    for i in plats:
        if i.p == True:
            Parkur.Main.Player.touch = True
            break
        else:
            Parkur.Main.Player.touch = False