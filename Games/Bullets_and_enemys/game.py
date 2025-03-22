import pygame
import threading
import time

pygame.init()

width = 500
height = 500
timer1 = 0
timer2 = 0
def Timer():
    global timer1
    while True:
        time.sleep(1)
        timer1 -= 1
def Timer2():
    global timer2
    while True:
        time.sleep(1)
        timer2 -= 1
timer1_thread = threading.Thread(target=Timer,daemon=True)
timer1_thread.start()
timer2_thread = threading.Thread(target=Timer2,daemon=True)
timer2_thread.start()
class Player(pygame.sprite.Sprite):
    def __init__(self,enemy,*group):
        super().__init__(*group)
        self.image = pygame.image.load(r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Bullets_and_enemys\Pictures\Player1.png')
        self.image = pygame.transform.scale(self.image,(150,75))
        self.rect = self.image.get_rect()
        self.helth = 50
        self.enemy = enemy
    
    def update(self):
        self.Mouve()
        if self.helth <= 0:
            all_sprites.remove(self)
    
    def Mouve(self):
        global timer1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.top -= 3
        elif keys[pygame.K_s]:
            self.rect.top += 3
        
        if keys[pygame.K_z]:
            if timer1 <= 0:
                bulet = Bulet(self.enemy,bullets_sprites)
                bulet.rect.bottom = self.rect.bottom
                bulet.rect.centerx = self.rect.centerx
                timer1 = 0.5

class Bulet(pygame.sprite.Sprite):
    def __init__(self,enemy,*group):
        super().__init__(*group)
        self.image = pygame.image.load(r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Bullets_and_enemys\Pictures\Bullet.png')
        self.image = pygame.transform.scale(self.image,(50,20))
        self.rect = self.image.get_rect()
    
    def update(self):
        if self.rect.right < width:
            self.rect.left += 3
        else:
            bullets_sprites.remove(self)

class Player1(pygame.sprite.Sprite):
    def __init__(self,enemy,*group):
        super().__init__(*group)
        self.image = pygame.image.load(r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Bullets_and_enemys\Pictures\Player2.png')
        self.image = pygame.transform.scale(self.image,(150,75))
        self.rect = self.image.get_rect()
        self.rect.right = width
        self.rect.bottom = height
        self.helth = 50
        self.enemy = enemy
    
    def update(self):
        self.Mouve()
        if self.helth <= 0:
            all_sprites.remove(self)
    
    def Mouve(self):
        global timer2
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.top -= 3
        elif keys[pygame.K_DOWN]:
            self.rect.top += 3
        
        if keys[pygame.K_SPACE]:
            if timer2 <= 0:
                bulet = Bulet1(self.enemy,bullets_sprites)
                bulet.rect.bottom = self.rect.bottom
                bulet.rect.centerx = self.rect.centerx
                timer2 = 0.5
class Bulet1(pygame.sprite.Sprite):
    def __init__(self,enemy,*group):
        super().__init__(*group)
        self.image = pygame.image.load(r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Bullets_and_enemys\Pictures\Bullet1.png')
        self.image = pygame.transform.scale(self.image,(50,20))
        self.rect = self.image.get_rect()
    
    def update(self):
        if self.rect.left > 0:
            self.rect.left -= 3
        else:
            bullets_sprites.remove(self)
all_sprites = pygame.sprite.Group()
player = Player(all_sprites)
bullets_sprites = pygame.sprite.Group()
player1 = Player1(all_sprites)

win = pygame.display.set_mode((width,height))
FPS = 60
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255,255,255))
    all_sprites.draw(win)
    all_sprites.update()
    bullets_sprites.draw(win)
    bullets_sprites.update()

    pygame.display.update()
    clock.tick(FPS)