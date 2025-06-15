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
debug = True

#Главный класс
class Object:
    def __init__(self):
        pass

def Update():
    pass

#Дебаг

#Методы для дебага
class DebugTable:
    def __init__(self):
        pass

    def ShowTable(self):
        pass

    def AddSquare(self):
        pass

    def AddCircle(self):
        pass

    def AddCoustomObject(self):
        pass

#Класс дебага
class Debug:
    def __init__(self,size):
        self.size = size
        self.simulation = pygame.display.set_mode((self.size[0],self.size[1]))

    def Start(self):
        global debug
        debug = True
        self.simulation.fill((0,0,0))
        pygame.display.set_caption('Debug')
        icon = pygame.image.load(r'Engine_Images\Debug_image.png')
        pygame.display.set_icon(icon)

        for i in range(-100 * int(metr),self.size[1] + 100 * int(metr),int(centimeter)*5):
            pygame.draw.line(self.simulation,(0,255,255),(-100 * int(metr),i),(100 * int(metr),i))
        for i in range(-100 * int(metr),self.size[0] + 100 * int(metr),int(centimeter)*5):
            pygame.draw.line(self.simulation,(0,255,255),(i,-100 * int(metr)),(i,100 * int(metr)))

        for i in range(-100 * int(metr),self.size[1] + 100 * int(metr),int(centimeter)*10):
            pygame.draw.line(self.simulation,(0,0,255),(-100 * int(metr),i),(100 * int(metr),i))
        for i in range(-100 * int(metr),self.size[0] + 100 * int(metr),int(centimeter)*10):
            pygame.draw.line(self.simulation,(0,0,255),(i,-100 * int(metr)),(i,100 * int(metr)))

        for i in range(-100 * int(metr),self.size[1] + 100 * int(metr),int(centimeter)*25):
            pygame.draw.line(self.simulation,(255,255,255),(-100 * int(metr),i),(100 * int(metr),i))
        for i in range(-100 * int(metr),self.size[0] + 100 * int(metr),int(centimeter)*25):
            pygame.draw.line(self.simulation,(255,255,255),(i,-100 * int(metr)),(i,100 * int(metr)))
        
        for i in range(-100 * int(metr),self.size[1] + 100 * int(metr),int(centimeter)*50):
            pygame.draw.line(self.simulation,(255,255,255),(-100 * int(metr),i),(100 * int(metr),i))
        for i in range(-100 * int(metr),self.size[0] + 100 * int(metr),int(centimeter)*50):
            pygame.draw.line(self.simulation,(255,255,255),(i,-100 * int(metr)),(i,100 * int(metr)))

        for i in range(-100 * int(metr),self.size[1] + 100 * int(metr),int(metr)):
            pygame.draw.line(self.simulation,(255,0,0),(-100 * int(metr),i),(100 * int(metr),i))
        for i in range(-100 * int(metr),self.size[0] + 100 * int(metr),int(metr)):
            pygame.draw.line(self.simulation,(255,0,0),(i,-100 * int(metr)),(i,100 * int(metr)))

#Тик игры
deb = Debug([500,500])
while True:
    if quit_permission:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
    if debug:
        deb.Start()
    pygame.display.update()
    clock.tick(FPS)