import pygame

pygame.init()
width = 700
height = 700

cords = [15,15]

win = pygame.display.set_caption('circle clones')
win = pygame.display.set_mode((width, height))
chapter1 = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((0,0,0))
    pygame.draw.circle(win,[255,255,255],cords,15)
    if chapter1 == False:
        if cords[0] < width-15:
            cords[0] += 1
        elif cords[1] < height-15:
            cords[1] += 1
        else:
            chapter1 = True
    else:
        if cords[0] > 15:
            cords[0] += -1
        elif cords[1] > 15:
            cords[1] += -1
        else:
            chapter1 = False
    
    pygame.display.update()
    pygame.time.delay(5)