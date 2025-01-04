import pygame
size = float(input("size: "))
if size > 800:
    size = 800
win = pygame.display.set_mode((size,size))
win.fill((255,255,255))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()