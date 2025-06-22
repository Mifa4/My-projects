#v 0.1.0
import pygame

from Acoustics import *
from Optics import *
from Termodinamics import *
from Mechanic import *
from FisicalQuantities import *

import Acoustics
import Optics
import Termodinamics
import Mechanic
import FisicalQuantities

FPS = 60
clock = pygame.time.Clock()
quit_permission = True
windows = []

class Camera: #Private
    def __init__(self,pos):
        self.pos = pos
    
    def SetPos(self,pos):
        self.pos = pos

    def MoveLeft(self,speed):
        self.pos[0] += speed
    
    def MoveRight(self,speed):
        self.pos[0] -= speed
    
    def MoveUp(self,speed):
        self.pos[1] += speed
    
    def MoveDown(self,speed):
        self.pos[1] -= speed

class Window: #Private
    def __init__(self,size,objects,col,cam):
        self.win = pygame.display.set_mode(size)
        self.col = col
        self.cam = cam
        self.obj = objects
    
    def Obj_Update(self):
        self.win.fill((self.col[0],self.col[1],self.col[2]))
        for changer in self.obj:
            changer.pos = changer.startPos - self.cam.pos

class Object: #Private
    def __init__(self,pos,type,col,Img):
        self.startPos = pos[:]
        self.pos = pos

class ObjectMassive:
    def __init__(self,obj):
        self.obj = obj

    def Do(self,Id):
        obj = self.obj[Id]

while True: #Public
    key = pygame.key.get_pressed()
    if quit_permission:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
    for updater in windows:
        updater.Obj_Update()
    pygame.display.update()
    clock.tick(FPS)