import pygame
import random
pygame.init()
y_max = 500
x_max = 500
win = pygame.display.set_mode((x_max, y_max))
clock = pygame.time.Clock()
fps = 50
class IMG_Worker:
    def __init__(self):
        self.UnRegisterGroup = pygame.sprite.Group() #-1
        self.StaticGroup = pygame.sprite.Group() #0
        self.NPCGroup = pygame.sprite.Group() #1
        self.PlayerGroup = pygame.sprite.Group() #2
        self.UIGroup = pygame.sprite.Group() #3
        self.workRes = [0,0]

    def Load_img(self, path, pos, scale, group):
        self.workRes = [0, 0]
        img = pygame.sprite.Sprite()
        img.image = pygame.image.load(path)
        img.image.convert()
        colorkey = img.image.get_at((0, 0))
        img.image.set_colorkey(colorkey)
        if scale[0] and scale[1] <= 0:
            self.workRes = [-1, 2]
            pygame.transform.scale(img.image, (5, 5))
        else:
            pygame.transform.scale(img.image, scale)

        img.rect = img.image.get_rect()
        img.rect.x = pos[0]
        img.rect.y = pos[1]
        if group == 0:
            self.StaticGroup.add(img)
        elif group == 1:
            self.NPCGroup.add(img)
        elif group == 2:
            self.PlayerGroup.add(img)
        elif group == 3:
            self.UIGroup.add(img)
        else:
            self.UnRegisterGroup.add(img)
        self.ErrorCase()

    def DrawGroup(self, groupId, win):
        self.workRes = [0, 0]
        if groupId == -1:
            self.UnRegisterGroup.draw(win)
        elif groupId == 0:
            self.StaticGroup.draw(win)
        elif groupId == 1:
            self.NPCGroup.draw(win)
        elif groupId == 2:
            self.PlayerGroup.draw(win)
        elif groupId == 3:
            self.UIGroup.draw(win)
        else:
            self.workRes = [-1, 1]
        self.ErrorCase()

    def ClearGroup(self,groupId):
        self.workRes = [0, 0]
        if groupId == -1:
            self.UnRegisterGroup.empty()
        elif groupId == 0:
            self.StaticGroup.empty()
        elif groupId == 1:
            self.NPCGroup.empty()
        elif groupId == 2:
            self.PlayerGroup.empty()
        elif groupId == 3:
            self.UIGroup.empty()
        else:
            self.workRes = [-1, 3]
        self.ErrorCase()

    def ErrorCase(self):
        if self.workRes == [-1,1]:
            print('Error in DrawGroup(), valible groups: -1 0 1 2 3!')
        if self.workRes == [-1,2]:
            print('Error in Load_img(), scale can`t be <= 0')
        if self.workRes == [-1,3]:
            print('Error in ClearGroup(), valible groups: -1 0 1 2 3!')


IMG = IMG_Worker()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255, 255, 255))
    for i in range(0, 100):
        IMG.Load_img(path='Images\\Circle.png', pos=(random.randint(0,500), random.randint(0,500)), scale=(100,100), group=1)
    IMG.DrawGroup(groupId=1,win=win)
    clock.tick(fps)
    pygame.display.update()