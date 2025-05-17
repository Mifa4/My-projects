import pygame
from Parkur.Methods  import *
import Parkur.Methods

pygame.init()
class Object:
    def __init__(self,size,pos,texturePath,textureT2):
        self.image = pygame.image.load(texturePath)
        self.image = pygame.transform.scale(self.image,(size[0],size[1]))
        self.player = self.image
        self.pos = pos
        self.size = size
        self.p1 = texturePath
        self.p2 = textureT2
    
    def Mouve(self,speed,keys):
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.pos[1] -= speed
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.pos[1] += speed

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.image = pygame.image.load(self.p2)
            self.image = pygame.transform.scale(self.image,(self.size[0],self.size[1]))
            self.pos[0] -= speed
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.image = pygame.image.load(self.p1)
            self.image = pygame.transform.scale(self.image,(self.size[0],self.size[1]))
            self.pos[0] += speed
    
    def Collision():
        pass

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