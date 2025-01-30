import pygame
import time
pygame.init()
win = pygame.display.set_mode((300,300))

class PlayerObject:
    def __init__(self,window,color,cordinate,radius):
        #varribles
        self.col = (255,255,255)
        self.cord = [0,0]
        self.rad = 5
        self.jump = False
        #constants
        self.start_cord = self.cord[1]
        self.down_jump = False
        self.awake = True
        if not(isinstance(color, list)):
            if list(color).count == 3:
                self.col = color
        if type(cordinate) == type((1,2,3)):
            if len(cordinate) == 2:
                self.cord = list(cordinate)
        if type(radius) == type(1):
            self.rad = radius
        if type(win) == pygame.Surface:
            self.win = window
        else:
            print("Error!")
    
    def Display(self):
        pygame.draw.circle(surface=self.win,color=self.col,center=self.cord,radius=self.rad)
    
    def Awake(self):
        if self.awake == True:
            self.awake = False

    def Mouve(self):
        if self.jump == False:
            key = pygame.key.get_pressed()
            if key[pygame.K_a] or key[pygame.K_LEFT]:
                self.cord[0] -= 5
            elif key[pygame.K_d] or key[pygame.K_RIGHT]:
                self.cord[0] += 5
            
            if key[pygame.K_w] or key[pygame.K_UP]:
                self.cord[1] -= 5
            elif key[pygame.K_s] or key[pygame.K_DOWN]:
                self.cord[1] += 5
    def Jump(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jump == False:
            self.jump = True
            self.start_cord = self.cord[1]
        if self.jump == True:
            if self.down_jump == False:
                self.rad += 1
                self.cord[1] -= 5
            else:
                self.cord[1] += 5
                self.rad -= 1
            if self.cord[1] == self.start_cord - 15:
                self.down_jump = True
                
            if self.cord[1] == self.start_cord and self.down_jump:
                self.jump = False
                self.down_jump = False


Player_Circle = PlayerObject(win,(255,255,255),(150,150),15)
while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            exit()
    win.fill((0,0,0))
    Player_Circle.Display()
    Player_Circle.Mouve()
    Player_Circle.Jump()
    Player_Circle.Awake()
    pygame.display.update()
    pygame.time.delay(20)