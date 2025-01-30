import pygame

pygame.init()
width = 700
height = 700
win = pygame.display.set_caption('Circle mouving')
win = pygame.display.set_mode((width, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        

            pygame.display.update()