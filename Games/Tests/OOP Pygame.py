import pygame
import time
pygame.init()
win = pygame.display.set_mode((300,300))

class PlayerObject:
    def __init__(self,window,color,cordinate,radius):
        self.col = (255,255,255)
        self.cord = [0,0]
        self.rad = 5
        self.jump = False
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
        start_cord = 0
        if key[pygame.K_SPACE] and self.jump == False:
            self.jump = True
            s_rad = self.rad
            self.rad += self.rad
            start_cord = self.cord[1]
            if self.cord[1] <= start_cord - 5:
                self.cord[1] +=1
            else:
                self.cord[1] -= 1
                
            if self.cord[1] == start_cord:
                self.jump = False
        if self.jump == True:
            self.cord[1] -= 1
            if self.cord[1] == start_cord - 5:
                self.cord[1] += 5
                
            if self.cord[1] == start_cord:
                self.rad = s_rad
                self.jump = False


Player_Circle = PlayerObject(win,(255,255,255),(150,150),15)
while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            exit()
    win.fill((0,0,0))
    Player_Circle.Display()
    Player_Circle.Mouve()
    Player_Circle.Jump()
    pygame.display.update()
    pygame.time.delay(20)