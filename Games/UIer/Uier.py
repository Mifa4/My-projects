import pygame
import random

pygame.init()

w,h = 500,500

win = pygame.display.set_mode((w,h))

FPS = 60
clock = pygame.time.Clock()

wl1 = w // 2
hl1 = h // 2
l1 = pygame.Surface((wl1,hl1))
l1_rgb = [255,0,255]
l1.fill((l1_rgb[0],l1_rgb[1],l1_rgb[2]))

wl2 = w // 2
hl2 = h //2
l2 = pygame.Surface((wl2,hl2))
l2_rgb = [255,0,0]
l2.fill((l2_rgb[0],l2_rgb[1],l2_rgb[2]))

wl3 = w // 2
hl3 = h //2
l3 = pygame.Surface((wl3,hl3))
l3_rgb = [0,0,255]
l3.fill((l3_rgb[0],l3_rgb[1],l3_rgb[2]))

wl4 = w // 2
hl4 = h //2
l4 = pygame.Surface((wl4,hl4))
l4_rgb = [255,255,0]
l4.fill((l4_rgb[0],l4_rgb[1],l4_rgb[2]))

image = pygame.image.load(r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\UIer\Images\UIPtester.png')
playerW = 50
playerH = 50
image = pygame.transform.scale(image,(playerW,playerH))
xPos = 0
yPos = 0
nl = 1

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        yPos -= 5
        if yPos <= 0:
            if nl == 3:
                nl = 1
                l3_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                yPos = hl1 - playerH
            elif nl == 2:
                nl = 4
                l2_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                yPos = hl1 - playerH
            elif nl == 1:
                nl = 3
                l1_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                yPos = hl1 - playerH
            elif nl == 4:
                nl = 2
                l4_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                yPos = hl1 - playerH
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        yPos += 5
        if yPos + playerH >= hl1:
            if nl == 4:
                nl = 2
                l4_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
            elif nl == 1:
                nl = 3
                l1_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
            elif nl == 2:
                nl = 4
                l2_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
            elif nl == 3:
                nl = 1
                l3_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
            yPos = 0

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        xPos -= 5
        if xPos <= 0:
            if nl == 2:
                nl = 1
                l2_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                xPos = wl1 - playerW
            elif nl == 4:
                nl = 3
                l4_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                xPos = wl1 - playerW
            elif nl == 3:
                nl = 4
                l3_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                xPos = wl1 - playerW
            elif nl == 1:
                nl = 2
                l1_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                xPos = wl1 - playerW
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        xPos += 5
        if xPos + playerW >= wl1:
            if nl == 4:
                nl = 3
                l4_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
            elif nl == 2:
                nl = 1
                l2_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
            elif nl == 1:
                nl = 2
                l1_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
            elif nl == 3:
                nl = 4
                l3_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
            xPos = 0
    if nl == win:
        nl = 1
        xPos = 1
        yPos = 1
    
    if nl == 1:
        l1.blit(image,(xPos,yPos))
    if nl == 2:
        l2.blit(image,(xPos,yPos))
    if nl == 3:
        l3.blit(image,(xPos,yPos))
    if nl == 4:
        l4.blit(image,(xPos,yPos))
    
    win.fill((255,255,255))
    win.blit(l1,(0,0))
    win.blit(l2,(w // 2,0))
    win.blit(l3,(0,h // 2))
    win.blit(l4,(w // 2,h // 2))
    l1.fill((l1_rgb[0],l1_rgb[1],l1_rgb[2]))
    l2.fill((l2_rgb[0],l2_rgb[1],l2_rgb[2]))
    l3.fill((l3_rgb[0],l3_rgb[1],l3_rgb[2]))
    l4.fill((l4_rgb[0],l4_rgb[1],l4_rgb[2]))
    pygame.display.update()
    clock.tick(FPS)