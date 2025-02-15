import pygame
import random
pygame.init()
y_max = 495
x_max = 495
win = pygame.display.set_mode((x_max,y_max))
clock =pygame.time.Clock()
objects = []

class PlayerObject:
    def __init__(self,window,color,cordinate,radius):
        #varribles
        self.col = list(color)
        self.cord = list(cordinate)
        self.cord_go = list((random.randint(-5,5),random.randint(-5,5)))
        self.rad = radius
        self.awake = True
        self.win = window
    
    def Mouvement(self):
        global x_max,y_max
        self.cord[0] += self.cord_go[0]
        self.cord[1] += self.cord_go[1]
        
        if self.col[0] < 255:
            self.col[0] += 1
        if self.col[1] < 255:
            self.col[1] += 1
        if self.col[2] < 255:
            self.col[2] += 1

        if self.cord[0] >= x_max:
            self.cord_go = list((random.randint(-5,0),random.randint(-5,5)))
        elif self.cord[0] <= 0:
            self.cord_go = list((random.randint(0,5),random.randint(-5,5)))
        if self.cord[1] >= y_max:
            self.cord_go = list((random.randint(-5,5),random.randint(-5,0)))
        elif self.cord[1] <= 0:
            self.cord_go = list((random.randint(-5,5),random.randint(0,5)))

    def Display(self):
        pygame.draw.circle(surface=self.win,color=self.col,center=self.cord,radius=self.rad)
    
    def Awake(self):
        if self.awake == True:
            self.awake = False
    
    def Destroyer(self):
        global objects
        if self.col[0] == 255 and self.col[1] == 255 and self.col[2] == 255:
            objects.remove(self)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255,255,255))
    objects.append(PlayerObject(win,(random.randint(1,255),random.randint(1,255),random.randint(1,255)),(x_max / 2,y_max / 2),random.randint(5,75)))
    for i in range(0,len(objects)):
        objects[i].Awake()
        objects[i].Display()
        objects[i].Mouvement()
    pygame.display.update()
    print(clock.get_fps())
    clock.tick(100)