import pygame
pygame.init()

class Circle:
    def __init__(self, color,x,y,rad):
        self.color = color
        self.x = x
        self.y = y
        self.rad = rad


    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.rad)


def move_by_keys(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
         self.x -= 5
    if keys[pygame.K_RIGHT]:
         self.x += 5
    if keys[pygame.K_UP]:
         self.y -= 5
    if keys[pygame.K_DOWN]:
         self.y += 5
    pygame.display.update()
    pygame.time.delay(10)

win = pygame.display.set_mode((500,500))
x,y = 250,250
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((255,255,255))


