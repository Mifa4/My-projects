import pygame
import random
pygame.init()

width = 500
height = 500
win = pygame.display.set_mode((width,height))

class Player(pygame.sprite.Sprite):
    def __init__(self,Enemy, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\GAMEWORKER\Pictures\IMG.png')
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.health = 100
        self.Enemy = Enemy
    def update(self):
        self.Mouve()
    def Mouve(self):
        global backgroundx,backgroundx2,background_speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.top -= 5
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.top += 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            backgroundx -= background_speed
            backgroundx2 -= background_speed
            self.Enemy.rect.left -= 5

class Enemy(pygame.sprite.Sprite):
            def __init__(self,*group):
                super().__init__(*group)
                self.image = pygame.image.load(r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\GAMEWORKER\Pictures\IMG1.png')
                self.image = pygame.transform.scale(self.image,(100,100))
                self.rect = self.image.get_rect()
                self.rect.right = width
                self.health = 100
            def update(self):
                self.Mouve()
            def Mouve(self):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_KP8] or keys[pygame.K_i]:
                    self.rect.top -= 5
                elif keys[pygame.K_KP5] or keys[pygame.K_k]:
                    self.rect.top += 5
                if keys[pygame.K_KP4] or keys[pygame.K_j]:
                    self.rect.left -= 5
                elif keys[pygame.K_KP6] or keys[pygame.K_l]:
                    self.rect.left += 5

enemySprites = pygame.sprite.Group()
enemy = Enemy(enemySprites)
all_sprites = pygame.sprite.Group()
player = Player(enemy,all_sprites)
fps = 60
clock = pygame.time.Clock()
backGround_image = pygame.image.load(r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\GAMEWORKER\Pictures\FON.png')
backGround_image = pygame.transform.scale(backGround_image,(width,height))
backgroundx = 0
backGround_image2 = pygame.image.load(r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\GAMEWORKER\Pictures\Fon1.png')
backGround_image2 = pygame.transform.scale(backGround_image2,(width,height))
backgroundx2 = width
background_speed = 4
player.rect.top = height / 2 - 50
enemy.rect.top = height / 2 - 50
while True:
    for i in pygame.event.get():
          if i.type == pygame.QUIT:
               exit()
    win.blit(backGround_image,(backgroundx,0))
    win.blit(backGround_image2,(backgroundx2,0))
    if backgroundx2 == 0:
         backgroundx = width
    if backgroundx == 0:
         backgroundx2 = width
    
    all_sprites.draw(win)
    all_sprites.update()
    enemySprites.draw(win)
    enemySprites.update()
    hits = pygame.sprite.spritecollide(player,enemySprites,False)
    if len(hits) > 0:
         hits[0].health -= 10
         hits[0].rect.left = random.randint(0,width - hits[0].rect.width)
         hits[0].rect.top = random.randint(0,height - hits[0].rect.height)
    if enemy.rect.left < player.rect.left:
        enemy.rect.left = width
    elif enemy.rect.left > width:
        enemy.rect.left = player.rect.left
    if enemy.rect.bottom < 0:
        enemy.rect.bottom = height
    elif enemy.rect.bottom > height:
        enemy.rect.bottom = 0
    if player.rect.bottom < 0:
        player.rect.bottom = height
    elif player.rect.bottom > height:
        player.rect.bottom = 0
    pygame.display.update()
    clock.tick(fps)