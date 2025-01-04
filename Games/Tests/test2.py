import pygame
pygame.init()
win = pygame.display.set_mode(size=(1080,600))#win = window
#colors
fon_color = (0,0,0)#RGB
#settings
w = 10#width
h = 25#height

#game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    win.fill(fon_color)
    for i in range(25,1075,25):
        for i1 in range(25,575,25):
            pygame.draw.rect(win,(255,255,0),(i,i1,w,h))
            pygame.draw.line(win,(255,0,255),(i,i1),(1080,i1 - 10),5)
            
    rad = 3#radius
    for i in range(0,1080,10):
        for i1 in range(0,600,10):
            pygame.draw.circle(win,(255,50,0),(i,i1),rad)
        for i in range(0,1000,100):
            for i1 in range(0,600,100):
                pygame.draw.lines(win,(255,255,255),True,((i + 200,i1 + 200),(i+ 300,i1 + 150),(i + 300,i1 + 250)),5)
                pygame.draw.polygon(win,(0,25,0),[(i + 5,i1 + 100),(i + 95,i1 + 50),(i + 95,i1 + 150)],False)
    pygame.display.update()