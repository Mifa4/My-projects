import pygame
import random
pygame.init()
y_max = 495
x_max = 495
win = pygame.display.set_mode((x_max,y_max))
clock = pygame.time.Clock()
objects = []

class PlayerObject:
    def __init__(self,window,color,cordinate,radius):
        #varribles
        self.col = color
        self.cord = list(cordinate)
        self.rad = radius
        self.awake = True
        self.win = window
        self.X_Pluser = True
    
    def Mouvement(self):
        global x_max,y_max
        if self.X_Pluser == True:
            self.cord[0] += 5
        else:
            self.cord[0] -= 5

        if self.cord[0] >= 500:
            self.X_Pluser = False
        elif self.cord[0] <= 0:
            self.X_Pluser = True

    def Display(self):
        pygame.draw.circle(surface=self.win,color=self.col,center=self.cord,radius=self.rad)
    
    def Awake(self):
        if self.awake == True:
            self.awake = False

for i in range(0,100):
    objects.append(PlayerObject(win,(random.randint(1,255),random.randint(1,255),random.randint(1,255)),(i * 10,i * 5),15))
    objects[i].Awake()

for i in range(0,100):
    objects.append(PlayerObject(win,(random.randint(1,255),random.randint(1,255),random.randint(1,255)),(x_max - i * 10,i * 5),15))
    objects[i].Awake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255,255,255))
    for i in range(0,len(objects)):
        objects[i].Display()
        objects[i].Mouvement()
    pygame.display.update()
    print(clock.get_fps())
    clock.tick(100)