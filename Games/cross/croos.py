import pygame

size = int(input("size of cross:\t"))
r = int(input("red count in rgb:\t"))
g = int(input("green count in rgb:\t"))
b = int(input("blue count in rgb:\t"))

if r > 255 :
    r = 255
elif r < 0:
    r = 0

if g > 255 :
    g = 255
elif g < 0:
    g = 0

if b > 255 :
    b = 255
elif b < 0:
    b = 0
    

win = pygame.display.set_mode((200,200))
win.fill((0,0,15))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.draw.line(win,(r,g,b),(0,0),(200,200),size)
    pygame.draw.line(win,(r,g,b),(0,200),(200,0),size)
    pygame.display.update()