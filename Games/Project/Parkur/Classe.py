import pygame
from Parkur.Methods  import *
import Parkur.Methods
from Story.Console_of_secrets import *
import Story.Console_of_secrets
from time import sleep
import shutil
import random

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
        self.p = False
    
    def Update(self,keys,obj,level,objects,offIndex,thisObj):
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
        elif self.type == 'Button':
            self.Button(obj,offIndex,objects,thisObj)
        elif self.type == 'Teleport':
            self.Teleport(obj)
        elif self.type == 'End':
            self.NextLevel(Parkur.Main.Player,level)
        elif self.type == 'Over':
            self.End(obj)
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
            self.p = True
            obj.pos[1] = selftop - obj.size[1]
        else:
            self.p = False
    
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
        if selfbottom >= top and selfright >= left+10 and selfleft <= right-10 and selftop <= bottom-10:
            Parkur.Main.deaths += 1
            data = Read()
            Write([f'open:{data[0]}',f'name:{data[1]}',f'level_of_parkur:{data[2]}',f'Time1:{data[3]}',f'Time2:{data[4]}',f'Time3:{data[5]}',f'Time4:{data[6]}',f'Time5:{data[7]}',f'Deaths:{Parkur.Main.deaths}','!Controler of correct work!: !Controler of correct work!: Don`t redact that file!'])
            s = random.randint(0,10)
            if s == 0:
                Say('[???]:...',0.1)
            elif s == 1:
                Say('[???]:Это просто!',0.1)
            elif s == 2:
                Say('[???]:Ты полный #####!',0.1)
            elif s == 3:
                Say('[???]:Ты специально?',0.1)
            elif s == 4:
                Say('[???]:Хватит это делать!',0.1)
            elif s == 5:
                Say('[???]:Ещё один ту####!!!',0.1)
            elif s == 6:
                Say('[???]:???',0.1)
            elif s == 7:
                Say('[???]: :((((((((((((((((((((',0.1)
            elif s == 8:
                Say('[???]:wwwaaaaaaaaa',0.1)
            elif s == 9:
                Say('[???]:мое терпение кончаеться!',0.1)
            elif s == 10:
                pass

            obj.pos = obj.start_pos[:]
    
    def Button(self,obj,offObjIndex,objects,thisObj):
        top = obj.pos[1]
        bottom = obj.pos[1] + obj.size[1]
        right = obj.pos[0] + obj.size[0]
        left = obj.pos[0]
        selftop = self.pos[1]
        selfbottom = self.pos[1] + self.size[1]
        selfright = self.pos[0] + self.size[0]
        selfleft = self.pos[0]
        #if bottom <= selftop and right >= selfleft and left <= selfright and top >= selfbottom:
        if selfbottom >= top and selfright >= left+10 and selfleft <= right-10 and selftop <= bottom-10:
            objects.pop(offObjIndex)
            objects.pop(thisObj)
    
    def Teleport(self,obj):
        top = obj.pos[1]
        bottom = obj.pos[1] + obj.size[1]
        right = obj.pos[0] + obj.size[0]
        left = obj.pos[0]
        selftop = self.pos[1]
        selfbottom = self.pos[1] + self.size[1]
        selfright = self.pos[0] + self.size[0]
        selfleft = self.pos[0]
        #if bottom <= selftop and right >= selfleft and left <= selfright and top >= selfbottom:
        if selfbottom >= top and selfright >= left+10 and selfleft <= right-10 and selftop <= bottom-10:
            obj.pos = [50,50]
    
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
            Parkur.Methods.New_Level()
            data = Read()
            if level == 1:
                Write([f'open:{data[0]}',f'name:{data[1]}',f'level_of_parkur:2',f'Time1:{Parkur.Main.sec}.{Parkur.Main.min}.{Parkur.Main.hours}',f'Time2:{data[4]}',f'Time3:{data[5]}',f'Time4:{data[6]}',f'Time5:{data[7]}',f'Deaths:{data[8]}','!Controler of correct work!: !Controler of correct work!: Don`t redact that file!'])
                Say('[???]:Тебе еще надо много пройти.',0.1)
                Parkur.Main.musics.Play(1)
            elif level == 2:
                Write([f'open:{data[0]}',f'name:{data[1]}',f'level_of_parkur:3',f'Time1:{data[3]}',f'Time2:{Parkur.Main.sec}.{Parkur.Main.min}.{Parkur.Main.hours}',f'Time3:{data[5]}',f'Time4:{data[6]}',f'Time5:{data[7]}',f'Deaths:{data[8]}','!Controler of correct work!: !Controler of correct work!: Don`t redact that file!'])
                Say('[???]:2! Мало кто это проходил!',0.1)
                Parkur.Main.musics.Play(2)
            elif level == 3:
                Write([f'open:{data[0]}',f'name:{data[1]}',f'level_of_parkur:4',f'Time1:{data[3]}',f'Time2:{data[4]}',f'Time3:{Parkur.Main.sec}.{Parkur.Main.min}.{Parkur.Main.hours}',f'Time4:{data[6]}',f'Time5:{data[7]}',f'Deaths:{data[8]}','!Controler of correct work!: !Controler of correct work!: Don`t redact that file!'])
                Say('[???]:Ты почти добрался до меня.',0.1)
                Parkur.Main.musics.Play(3)
            elif level == 4:
                Write([f'open:{data[0]}',f'name:{data[1]}',f'level_of_parkur:5',f'Time1:{data[3]}',f'Time2:{data[4]}',f'Time3:{data[5]}',f'Time4:{Parkur.Main.sec}.{Parkur.Main.min}.{Parkur.Main.hours}',f'Time5:{data[7]}',f'Deaths:{data[8]}','!Controler of correct work!: !Controler of correct work!: Don`t redact that file!'])
                Say('[???]:Ещё чуть-чуть.',0.1)
                Say('[???]:Ты почти попал в моё начало!.!',0.1)
                Parkur.Main.musics.Play(4)
            Parkur.Main.sec,Parkur.Main.min,Parkur.Main.hours = 0,0,0
    
    def End(self,obj):
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
            data = Read()
            to = r'C:\Users\Елена\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
            file = r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Subtitles\subtitles.py'
            shutil.copy(file,to)
            Say('[VirtualKiller]:Спасибо!!!!!!!!!!!!!!!!!!!!!!!.',0.15)
            Say('[Console]: Объект выбрался на поверхность!',0.001)
            sleep(2)
            Say('[Console]: Объект был потерян!',0.001)
            Say('![Console]!: Произошла фотальная ошибка. ERR0R',0.7)
            Parkur.Main.Play = False
            Write([f'open:{data[0]}',f'name:{data[1]}',f'level_of_parkur:End',f'Time1:{data[3]}',f'Time2:{data[4]}',f'Time3:{data[5]}',f'Time4:{data[6]}',f'Time5:{Parkur.Main.sec}.{Parkur.Main.min}.{Parkur.Main.hours}','!Controler of correct work!: !Controler of correct work!: Don`t redact that file!'])
            Err0r()

class Text:
    def __init__(self,name,size,text,pos,color):
        self.Font = pygame.font.Font(name,size)
        self.text = text
        self.pos = pos
        self.color = color
    
    def Render(self,win):
        Render = self.Font.render(str(self.text),True,(self.color[0],self.color[1],self.color[2]))
        win.blit(Render,(self.pos[0],self.pos[1]))

class MusicPlayer:
    def __init__(self,musics_path):
        self.musics = []
        for i in musics_path:
            self.musics.append(pygame.mixer.Sound(i))
    
    def Play(self,music_index):
        for i in range(0,len(self.musics)):
            self.musics[i].stop()
        self.musics[music_index].play()