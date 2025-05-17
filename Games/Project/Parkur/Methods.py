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
def New_Level(level):
        level += 1
def Load_Level(level,win,Player):
    level1 = [Object([100,50],[0,50],[], r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Boxes\Textures\Box.png',None,None,'Plat'), Object([50,50],[150,100],[], r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Boxes\Textures\Box.png',None,None,'Plat')]
    if level == 1:
      for i in level1:
        i.Update('',Player,level)
        win.blit(i.image,(i.pos[0],i.pos[1]))

