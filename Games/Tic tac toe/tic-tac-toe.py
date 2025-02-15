import pygame
X_size = 500
Y_size = 500
win = pygame.display.set_mode((X_size,Y_size))

class Board:
    def __init__(self):
        self.map = [0,0,0,
                    0,0,0,
                    0,0,0]

    def ClearMap(self):
        self.map = [0,0,0,
                    0,0,0,
                    0,0,0]
    
    def ChangeMap(self,changeIndex,changeValue):
        if changeIndex < len(self.map) and (changeValue >= 0 and changeValue <= 2):
            self.map[changeIndex] = changeValue
        else:
            print('In correct index or value')
    
    def UDLine(self,X_max):
        return X_max / 3
    
    def LRLine(self,Y_max):
        return Y_max / 3
    
    def Printer(self,X_max,Y_max):
        index = 0
        Yindex = 0
        x_c = X_max / 3
        y_c = Y_max / 3
        for i in self.map:
            if i == 1:
                pass
            elif i == 2:
                if X_max <= Y_max:
                    pygame.draw.circle(win,(0,0,255),((x_c * index) + (x_c / 2),(y_c * Yindex) + (y_c / 2)),x_c / 2)
                else:
                    pygame.draw.circle(win,(0,0,255),((x_c * index) + (x_c / 2),(y_c * Yindex) + (y_c / 2)),y_c / 2)
            if index == 2:
                index = -1
                Yindex += 1
            index += 1
            if index == 3 and Yindex == 3:
                break
            
class Motions:
    def __init__(self):
        self.motion = 2
    
    def NextMotion(self):
        if self.motion == 1:
            self.motion = 2
        elif self.motion == 2:
            self.motion = 1
        else:
            self.motion = 1

GameBoard = Board()
Motion = Motions()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_c = X_size / 3
            y_c = Y_size / 3
            m_p = pygame.mouse.get_pos()
            for i in range(0,len(GameBoard.map),1):
                if m_p[0] * i < x_c and m_p[1] * i < y_c:
                    GameBoard.ChangeMap(i,Motion.motion)
                    break

    win.fill((255,255,255))

    for i in range(1,3,1):
        pygame.draw.line(win,(0,0,0),(GameBoard.UDLine(X_size) * i,0),(GameBoard.UDLine(X_size) * i,Y_size))
    for i in range(1,3,1):
        pygame.draw.line(win,(0,0,0),(0,GameBoard.LRLine(Y_size) * i),(X_size,GameBoard.LRLine(Y_size) * i))
    
    GameBoard.Printer(X_size,Y_size)

    pygame.display.update()