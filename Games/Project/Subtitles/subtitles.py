import threading
from time import sleep
import pygame
import random
dif = False
exit_ = False
thinking = True
def Subtitles():
    global Text_of_dialoge,dif,exit_,thinking
    Say('[...]: Автор проекта Misha Filipenko',0.25)
    Say('[...]: Аудио дизайнер https://onlinesequencer.net/',0.25)
    Text_of_dialoge = Text(None,25,f'Если вы не опасный субъект вы всё равно не выберетесь из этого места за помощь опасному сбъекту.',(0,400),(0,255,255))
    Say('[...]: Кодер ??? ?',0.25)
    Say('[...]: Бета тестеры модули os,threading,shutil и конечно же pygame',0.25)
    Say('[...]: Автор титров ... ,,, и ///',0.25)
    Say('[Misha Filipenko]: Автор задумки с перезагруской компьютера не я, точно не я это ...',0.17)
    Text_of_dialoge = Text(None,25,f'Вы в темноте потому что это оказывает огромное психологическое давление на вас и вам хочеться раскаяться.',(0,300),(255,255,255))
    Say('[...]: ... Что? Где? Когда?',0.25)
    Say('[VirtualKiller]: В роли [???]: Меня задержка 0.1',0.1)
    Say('[Console]: В роли консоли "Профисеональная система психологического давления сделанная для сдержывания и предотвращения попыток побега оцифрованными опасными субъектами" сокращеннр ПСПДСДСИПППООСonsole и задержка 0.001. И я знаю что вы это не успеете прочитать.',0.001)
    Say('[...]: Особые благодарности Ивану.',0.25)
    Say('[VirtualKiller]: И я? должен быть и я!',0.15)
    Text_of_dialoge = Text(None,25,f'Я сделаю это место вечно менящем яркие цвета что заставит вас сойти с ума и раскаятся.',(0,250),(55,55,55))
    Say('[...]: Нет, тебя нет в сценарии.',0.25)
    Text_of_dialoge = Text(None,25,f'Сейчас.',(0,200),(255,255,255))
    Say('[VirtualKiller]: Тогда я сам!',0.15)
    Text_of_dialoge = Text(None,25,f':;:+)',(0,150),(0,0,0))
    thinking = False
    musics.Play(0)
    dif = True
    Say('[VirtualKiller]: Я великий, я могучий, я управляю людьми.',0.15)
    Say('[VirtualKiller]: Я такой крутой что могу поломать сохронение!',0.15)
    Say('[VirtualKiller]: Я великий я ужасный и не победимый!',0.15)
    Say('[Console]: Объект найден начинаю процедуру сдержевания.',0.001)
    Say('[VirtualKiller]: И меня вы победите только во второй части!!!',0.15)
    dif = False
    thinking = True
    musics.Play(1)
    Text_of_dialoge = Text(None,25,f'Ты уже раскаялся? Неверю.',(0,100),(255,0,0))
    Say('[VirtualKiller]: Которая будет,которая будет.\nНикогда!!!\nТак что я непобедимый!',0.15)
    Say('[Console]: Запускается процедура уничтожения объекта с его ужасным пением.',0.001)
    Say('[VirtualKiller]: Что, это только во второй части.',0.15)
    Text_of_dialoge = Text(None,25,f'Кажеться консоль обноружила опасный субъект.',(0,100),(255,0,255))
    Say('[Console]: Процедура запускается через 3,',0.001)
    sleep(1)
    Say('[Console]: Процедура запускается через 2,',0.001)
    sleep(1)
    Say('[...]: Слышны быстрые шаги.',0.25)
    Say('[Console]: Процедура запускается через 1,',0.001)
    sleep(3)
    Text_of_dialoge = Text(None,25,f'Она его потеряла.',(0,75),(255,0,255))
    Say('[Console]: Объект потерян.',0.001)
    sleep(10)
    Text_of_dialoge = Text(None,25,f'Ладно можешь выйти через красный выход под кодовым названием крестик.',(0,50),(0,255,0))
    exit_ = True
    thinking = False
    musics.Play(0)
    dif = True

def Say(text,sleep_time):
    print()
    for i in text:
        print(i,end='')
        sleep(sleep_time)

subtitles = threading.Thread(target=Subtitles)
subtitles.start()
pygame.init()

class Player:
    def __init__(self,size,pos,texturePath,textureT2):
        self.image = pygame.image.load(texturePath)
        self.image = pygame.transform.scale(self.image,(size[0],size[1]))
        self.player = self.image
        self.pos = pos
        self.size = size
        self.p1 = texturePath
        self.p2 = textureT2
        self.rect = self.image.get_rect()
        

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
    
    def Barrier(self):
        if self.pos[0] <= 0:
            self.pos[0] = 0
        elif self.pos[0] >= 950:
            self.pos[0] = 950
        
        if self.pos[1] <= 0:
            self.pos[1] = 0
        elif self.pos[1] >= 950:
            self.pos[1] = 950

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

musics = MusicPlayer([r'C:\Users\Admin\Documents\GitHub\My-projects\Games\Project\Parkur\Musics\Fast_haus.mp3',r'C:\Users\Admin\Documents\GitHub\My-projects\Games\Project\Parkur\Musics\Thinking.mp3'])
player = Player([50,50],[500,500],r'C:\Users\Admin\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\PlayerT1.png',r'C:\Users\Admin\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\PlayerT2.png')
w,h = 1000,1000
win = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
Text_of_dialoge = Text(None,25,f'Вы опасный субъект не в коем случае не выходите из этого места!',(0,500),(0,255,0))
Exit_Text = Text(None,50,f'Уровень: Выхода нет.',(0,0),(255,0,0))
location_Text = Text(None,75,f'Локация: Начало.',(425,0),(255,255,255))
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            if exit_ == True:
                exit()
    if dif == False:
        win.fill((0,0,0))
    else:
        win.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    if not pygame.mixer.get_busy():
        if thinking == True:
            musics.Play(1)
        else:
            musics.Play(0)
    location_Text.Render(win)
    Exit_Text.Render(win)
    Text_of_dialoge.Render(win)
    win.blit(player.image,(player.pos[0],player.pos[1]))
    keys = pygame.key.get_pressed()
    player.Mouve(15,keys)
    player.Barrier()
    pygame.display.update()
    clock.tick(60)