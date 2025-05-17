import pygame
from Parkur.Methods  import *
import Parkur.Methods

pygame.init()
class Object:
    def __init__(self,size,pos, start,texturePath,textureT2,fall,type):
        self.image = pygame.image.load(texturePath)
        self.image = pygame.transform.scale(self.image,(size[0],size[1]))
        self.player = self.image
        self.pos = pos
        self.size = size
        self.p1 = texturePath
        self.p2 = textureT2
        self.rect = self.image.get_rect()
        self.start_pos = start
        #collision verebles
        self.falling = fall
        self.touch = False
        self.count = 0
        self.type = type
    
    def Update(self,keys,obj,level):
        if self.falling == False:
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.count += self.Jump()
            else:
                self.count = 10 * 10
            if self.count >= 10 * 10:
                self.count = 0
                self.falling = True
        elif self.falling != None:
            self.pos[1] += 5
        if self.type == 'Plat':
            self.Plat(obj)
        elif self.type == 'Obctacle':
            self.Obctacle(obj)
        elif self.type == 'End':
            self.NextLevel(level)
        self.rect = self.image.get_rect()
        

    def Mouve(self,speed,keys):
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if self.touch == True:
                self.falling = False

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.image = pygame.image.load(self.p2)
            self.image = pygame.transform.scale(self.image,(self.size[0],self.size[1]))
            self.pos[0] -= speed
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.image = pygame.image.load(self.p1)
            self.image = pygame.transform.scale(self.image,(self.size[0],self.size[1]))
            self.pos[0] += speed

    def Jump(self):
        min = 5
        self.pos[1] -= min
        return min

    
    def Plat(self,obj):
        top = obj.pos[1]
        bottom = obj.pos[1] + obj.size[1]
        right = obj.pos[0] + obj.size[0]
        left = obj.pos[0]
        selftop = self.pos[1]
        selfbottom = self.pos[1] + self.size[1]
        selfright = self.pos[0] + self.size[0]
        selfleft = self.pos[0]
        #if bottom <= selftop and right >= selfleft and left <= selfright and top >= selfbottom:
        if selfbottom >= top and selfright >= left and selfleft <= right and selftop <= bottom:
            obj.touch = True
            obj.pos[1] = selftop - self.size[1]
        else:
            obj.touch = False
    
    def Obctacle(self,obj):
        top = obj.pos[1]
        bottom = obj.pos[1] + obj.size[1]
        right = obj.pos[0] + obj.size[0]
        left = obj.pos[0]
        selftop = self.pos[1]
        selfbottom = self.pos[1] + self.size[1]
        selfright = self.pos[0] + self.size[0]
        selfleft = self.pos[0]
        #if bottom <= selftop and right >= selfleft and left <= selfright and top >= selfbottom:
        if selfbottom >= top and selfright >= left and selfleft <= right and selftop <= bottom:
            obj.pos = obj.start_pos[:]
    
    def NextLevel(self,obj,level):
        top = obj.pos[1]
        bottom = obj.pos[1] + obj.size[1]
        right = obj.pos[0] + obj.size[0]
        left = obj.pos[0]
        selftop = self.pos[1]
        selfbottom = self.pos[1] + self.size[1]
        selfright = self.pos[0] + self.size[0]
        selfleft = self.pos[0]
        #if bottom <= selftop and right >= selfleft and left <= selfright and top >= selfbottom:
        if selfbottom >= top and selfright >= left and selfleft <= right and selftop <= bottom:
            New_Level(level)

class Text:
    def __init__(self,name,size,text,pos,color):
        self.Font = pygame.font.Font(name,size)
        self.text = text
        self.pos = pos
        self.color = color
    
    def Render(self):
        self.Font.render(self.text,True,(self.color[0],self.color[1],self.color[2]))

class Level:
    def __init__(self,size,color,posOnMainSurface,Surface):
        self.level = pygame.Surface((size[0],size[1]))
        self.level.fill((color[0],color[1],color[2]))
        self.pos = posOnMainSurface
        Surface.blit(self.level,(self.pos[0],self.pos[1]))

class MusicPlayer:
    def __init__(self,musics_path):
        self.musics = []
        for i in musics_path:
            self.musics.append(pygame.mixer.Sound(i))
    
    def Play(self,music_index):
        for i in range(0,len(self.bools)):
            self.musics[i].stop()
        self.musics[music_index].play()