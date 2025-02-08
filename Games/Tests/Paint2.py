import pygame
import random
pygame.init()
y_max = 500
x_max = 500
rad_max = 100
s_rad = 5
figure = 'circle'
win = pygame.display.set_mode((x_max,y_max))
objects = []

class PlayerObjectC:
    def __init__(self,window,color,cordinate,radius):
        #varribles
        self.col = list(color)
        self.cord = list(cordinate)
        self.cord_go = list((random.randint(-5,5),random.randint(-5,5)))
        self.rad = radius
        self.awake = True
        self.win = window

    def Display(self):
        pygame.draw.circle(surface=self.win,color=self.col,center=self.cord,radius=self.rad)

class PlayerObjectS:
    def __init__(self,window,color,cordinate,width):
        #varribles
        self.col = list(color)
        self.cord = list(cordinate)
        self.cord_go = list((random.randint(-5,5),random.randint(-5,5)))
        self.wid = width
        self.awake = True
        self.win = window

    def Display(self):
        pygame.draw.rect(self.win,self.col,self.cord,self.wid)

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            exit()
    win.fill((255,255,255))
    
    pos_m = list(pygame.mouse.get_pos())
    press_m = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_PLUS] or keys[pygame.K_EQUALS]:
        if s_rad != rad_max:
            s_rad += 5
            print('radius =' + str(s_rad))
    if keys[pygame.K_MINUS]:
        if s_rad != 5:
            s_rad -= 5
            print('radius =' + str(s_rad))
    if keys[pygame.K_f]:
        if figure == 'circle':
            figure = 'square'
            print('Figure = ' + figure)
        elif figure == 'square':
            figure = 'circle'
            print('Figure = ' + figure)
    if press_m[0]:
        if pos_m[0] > x_max:
            pos_m[0] = x_max
        elif pos_m[0] < 0:
            pos_m[0] = 0
        
        if pos_m[1] > y_max:
            pos_m[1] = y_max
        elif pos_m[1] < 0:
            pos_m[1] = 0

        if figure == 'circle':
            objects.append(PlayerObjectC(win,(random.randint(0,255),random.randint(0,255), random.randint(0,255)),(pos_m[0],pos_m[1]),s_rad))
        elif figure == 'square':
            objects.append(PlayerObjectS())
    for i in range(len(objects)-1,0,-1):
        objects[i].Display()
        
    pygame.display.update()
    pygame.time.delay(100)