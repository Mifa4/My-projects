import pygame
import random
pygame.init()
y_max = 500
x_max = 500
win = pygame.display.set_mode((x_max,y_max))
objects = []
P_Objects = []

class FonObject:
    def __init__(self,window,color,cordinate,radius):
        #varribles
        self.col = list(color)
        self.cord = list(cordinate)
        self.cord_go = list((random.randint(-5,5),random.randint(-5,5)))
        self.rad = radius
        self.awake = True
        self.win = window
    
    def Blacker(self):
        if self.col[0] > 0:
            self.col[0] -= 1
        if self.col[1] > 0:
            self.col[1] -= 1
        if self.col[2] > 0:
            self.col[2] -= 1

    def Display(self):
        pygame.draw.circle(surface=self.win,color=self.col,center=self.cord,radius=self.rad)
    
    def Awake(self):
        if self.awake == True:
            if self.col[0] < 208:
                self.col[0] += 2
            if self.col[1] < 208:
                self.col[1] += 2
            if self.col[2] < 208:
                self.col[2] += 2
            if self.col[0] >= 208 and self.col[1] >= 208 and self.col[2] >= 208:
                self.awake = False
    
    def Destroyer(self):
        global objects
        if self.col[0] == 0 and self.col[1] == 0 and self.col[2] == 0:
            if self in objects:
                objects.remove(self)

class PlayerObject:
    def __init__(self,window,color,cordinate,radius):
        #varribles
        self.col = list(color)
        self.cord = list(cordinate)
        self.cord_go = list((random.randint(-5,5),random.randint(-5,5)))
        self.rad = radius
        self.awake = True
        self.win = window
    
    def Blacker(self):
        if self.col[0] > 0:
            self.col[0] -= 1
        if self.col[1] > 0:
            self.col[1] -= 1
        if self.col[2] > 0:
            self.col[2] -= 1
        
    def Destroyer(self):
        global P_Objects
        if self.col[0] == 0 and self.col[1] == 0 and self.col[2] == 0:                
            if self in P_Objects:
                P_Objects.remove(self)

    def Display(self):
        pygame.draw.circle(surface=self.win,color=self.col,center=self.cord,radius=self.rad)

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            exit()
    win.fill((255,255,255))
    objects.append(FonObject(win,(1, 1, 1),(random.randint(0,x_max),random.randint(0,y_max)),random.randint(2,5)))
    win.fill((0,0,0))
    for i in range(len(objects)-1,0,-1):
        objects[i].Awake()
        objects[i].Blacker()
        objects[i].Display()
        objects[i].Destroyer()
    
    pos_m = list(pygame.mouse.get_pos())
    press_m = pygame.mouse.get_pressed()

    if press_m[0]:
        if pos_m[0] > x_max:
            pos_m[0] = x_max
        elif pos_m[0] < 0:
            pos_m[0] = 0
        
        if pos_m[1] > y_max:
            pos_m[1] = y_max
        elif pos_m[1] < 0:
            pos_m[1] = 0

        P_Objects.append(PlayerObject(win,(208, 208, 208),(pos_m[0],pos_m[1]),random.randint(2,5)))
    for i in range(len(P_Objects)-1,0,-1):
        P_Objects[i].Blacker()
        P_Objects[i].Destroyer()
        P_Objects[i].Display()
        
    pygame.display.update()
    pygame.time.delay(50)