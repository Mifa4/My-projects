import pygame
import random

width = 500
height = 500
win = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
tick = 60
class Ball:
    def __init__(self,pos,speed,radius,color,fon,weight,a):
        self.pos = pos
        self.speed = speed
        self.rad = radius
        self.col = color
        self.fon = fon
        self.w = weight
        self.a = a
        self.go = random.uniform(-1,1)
    
    def Printer(self):
        pygame.draw.circle(win,self.col,(self.pos[0],self.pos[1]),self.rad)
    
    def Mouvemet(self):
        self.pos[0] += self.go * self.speed
        self.pos[1] += (self.a * self.w) * self.speed
class BallEmulator:
    def __init__(self,pos,radius,col):
        self.pos = pos
        self.rad = radius
        self.col = col
    
    def Printer(self):
        pygame.draw.circle(win,self.col,self.pos,self.rad)

class FonCircle:
    def __init__(self):
        self.pos = (width / 2,height / 2)
        self.rad = 500

    def Printer(self):
        pygame.draw.circle(win,(255,0,255),(self.pos[0],self.pos[1]),self.rad) 

Balls = []
Fon = FonCircle()
MainBall = Ball([250,250],0.1,15,(255,255,255),Fon,0.1,0.982)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((0,0,0))
    Balls.append(BallEmulator(MainBall.pos,MainBall.rad,MainBall.col))
    for i in range(0,len(Balls),1):
        Balls[i].Printer()
    MainBall.Mouvemet()
    MainBall.a += MainBall.a
    if MainBall.go > 0:
        MainBall.go -= 0.01
    elif MainBall.go < 0:
        MainBall.go += 0.01
    MainBall.Printer()
    clock.tick(tick)
    pygame.display.update()