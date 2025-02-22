import pygame
import random

Gray = [70] * 3
Black = [0] * 3
White = [255] * 3
Widht,Height = 600,600

pygame.init()
win = pygame.display.set_mode((Widht,Height))

class Board:
    def __init__(self,Width,Heights,size):
        self.Width,self.Height = Widht,Height
        self.size = size
        self.board = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        self.move = 1
        self.winner = 0
        self.situation = -1
    
    def click(self,mouse_pos):
        x = mouse_pos[0] // self.size
        y = mouse_pos[1] // self.size
        if self.board[y][x] == 0:
            self.board[y][x] = self.move
        self.move = -self.move

    def renderer(self,screen):
        pygame.draw.line(screen,Gray,(0,200), (self.Width,200))
        pygame.draw.line(screen,Gray,(0,400), (self.Width,400))

        pygame.draw.line(screen,Gray,(200,0), (200,self.Width))
        pygame.draw.line(screen,Gray,(400,0), (400,self.Width))

        for y in range(3):
            for x in range(3):
                if self.board[y][x] == 1:
                    self.draw_cross(screen,x,y,self.size)
                elif self.board[y][x] == -1:
                    self.draw_circle(screen,x,y,self.size)
        
        if self.winner != 0:
            if self.situation == 0:
                pygame.draw.line(screen,(0,255,255),(0,(Height / 3) / 2),(Widht,(Height / 3) / 2),5)
            if self.situation == 1:
                pygame.draw.line(screen,(0,255,255),(0,(Height / 3 * 2) - Height / 3 / 2),(Widht,(Height / 3 * 2) - Height / 3 / 2),5)
            if self.situation == 2:
                pygame.draw.line(screen,(0,255,255),(0,(Height / 3 * 3) - Height / 3 / 2),(Widht,(Height / 3 * 3) - Height / 3 / 2),5)
            
            if self.situation == 3:
                pygame.draw.line(screen,(0,255,255),((Widht / 3) / 2,0),((Widht / 3) / 2,Height),5)
            if self.situation == 4:
                pygame.draw.line(screen,(0,255,255),((Widht / 3 * 2) - Widht / 3 / 2,0),((Widht / 3 * 2) - Widht / 3 / 2,Height),5)
            if self.situation == 5:
                pygame.draw.line(screen,(0,255,255),((Widht / 3 * 3) - Widht / 3 / 2,0),((Widht / 3 * 3) - Widht / 3 / 2,Height),5)
            
            if self.situation == 6:
                pygame.draw.line(screen,(0,255,255),(0,0),(Widht,Height),5)
            if self.situation == 7:
                pygame.draw.line(screen,(0,255,255),(Widht,0),(0,Height),5)
    
    def draw_circle(self,screen,x,y,size):
        x = (x + .5) * size
        y = (y + .5) * size
        pygame.draw.circle(screen, (0,0,255),(x,y),(size - 3) // 2,3)

    def draw_cross(self,screen,x,y,size):
        x = x * size + 3
        y = y * size + 3
        pygame.draw.line(screen,(255,0,0),(x,y),(x + size - 3, y + size -3),3)
        pygame.draw.line(screen,(255,0,0),(x + size - 3,y - 3),(x,y + size  -3),3)
    
    def win(self):
        #Cross checker
        for y in range(3):
            if self.board[y][0] == 1 and self.board[y][1] == 1 and self.board[y][2] == 1:
                self.winner = 1
                self.situation = 1 * y

        for x in range(3):
            if self.board[0][x] == 1 and self.board[1][x] == 1 and self.board[2][x] == 1:
                self.winner = 1
                self.situation = 3 + (1 * x)

        if self.board[0][0] == 1 and self.board[1][1] == 1 and self.board[2][2] == 1:
            self.winner = 1
            self.situation = 6
        if self.board[0][2] == 1 and self.board[1][1] == 1 and self.board[2][0] == 1:
            self.winner = 1
            self.situation = 7
        
        #Circle checker
        for y in range(3):
            if self.board[y][0] == -1 and self.board[y][1] == -1 and self.board[y][2] == -1:
                self.winner = -1
                self.situation = 1 * y

        for x in range(3):
            if self.board[0][x] == -1 and self.board[1][x] == -1 and self.board[2][x] == -1:
                self.winner = -1
                self.situation = 3 + (1 * y)

        if self.board[0][0] == -1 and self.board[1][1] == -1 and self.board[2][2] == -1:
            self.winner = -1
            self.situation = 6
        if self.board[0][2] == -1 and self.board[1][1] == -1 and self.board[2][0] == -1:
            self.winner = -1
            self.situation = 7
    

board = Board(Width=Widht,Heights=Height,size=200)
win_ = False
while True:
    if win_ == False:
        if board.winner == 1:
            print("Cross is win!")
            win_ = True
        elif board.winner == -1:
            print("Circles is win!")
            win_ = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if board.winner == 0:
                board.click(event.pos)
                board.win()
        
        for i in range(10):
            pygame.draw.circle(win,Gray,(random.randint(0,Widht),random.randint(0,Height)),1)

    win.fill(White)
    board.renderer(screen=win)
    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(win,White,pos,5)
    pygame.display.update()