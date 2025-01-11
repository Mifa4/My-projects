#import
import pygame

#constants
size = [500,500]
fon_color = [250,10,250]
player_color = [250,250,0]
clone_color = [250,0,0]
player_rad = 15
different = [0,0]
cords = [size[0] / 2,size[1] / 2]

#window
pygame.init()
win = pygame.display.set_caption('circle clones')
win = pygame.display.set_mode(size)

while True:
    different = [size[0] - cords[0],size[1] - cords[1]]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(fon_color)
    pygame.draw.circle(win,player_color,cords,player_rad)

    #cloner
    if cords[0] > (size[0] / 2) + 150:
        pygame.draw.circle(win,clone_color,(different[0], different[1]),player_rad)
    elif cords[0] < (size[0] / 2) - 150:
        pygame.draw.circle(win,clone_color,(different[0], different[1]),player_rad)
    
    if cords[1] > (size[1] / 2) + 150:
        pygame.draw.circle(win,clone_color,(different[0], different[1]),player_rad)
    elif cords[1] < (size[1] / 2) - 150:
        pygame.draw.circle(win,clone_color,(different[0], different[1]),player_rad)

    #telleporter
    if cords[0] > size[0]:
        cords[0] = 0
    elif cords[0] < 0:
        cords[0] = size[0]

    if cords[1] > size[1]:
        cords[1] = 0
    elif cords[1] < 0:
        cords[1] = size[1]

    if player_rad > 0:
        player_rad -= 0.001
        #movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            cords[0] += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            cords[0] -= 1
    
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            cords[1] -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            cords[1] += 1
    else:
        fon_color = [0,0,255]
    pygame.display.update()
    pygame.time.delay(5)