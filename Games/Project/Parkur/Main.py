import pygame
import random
import threading
from Parkur.Methods import *
import Parkur.Methods
from Parkur.Classe import *
import Parkur.Classe
import Story.Console_of_secrets
Player = Object([50,50],[27,327], [27, 327],r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\PlayerT1.png',r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Textures\PlayerT2.png',True,'')
sec,min,hours = 0,0,0
deaths = 0
tr = threading.Thread(target=Timer)
tr.start()
musics = MusicPlayer([r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Musics\Level1.mp3',r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Musics\Level2.mp3',r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Musics\Level3.mp3',r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Musics\Level4.mp3',r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Parkur\Musics\Level5.mp3'])
Play = True
level = 1
data = Read()
if data[8] != '':
    deaths = int(data[8])
def Parkur_Time():
    global Player,sec,min,hours,Play,level
    sec = 0
    min = 0
    hours = 0
    pygame.init()
    w,h = 1000,500
    win = pygame.display.set_mode((w,h))
    FPS = 60
    clock = pygame.time.Clock()
    if level == 1:
        musics.Play(0)
    elif level == 2:
        Parkur.Main.Player.pos = [800,250]
    elif level == 3:
        Parkur.Main.Player.pos = [50,125]
    elif level == 4:
        Parkur.Main.Player.pos = [800,350]
    elif level == 5:
        pass
    while Play:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
        location_Text = Text(None,50,f'Локация:',(500,0),(255,50,50))
        if level == 1:
            win.fill((255,255,255))
            location_Text = Text(None,50,f'Локация: Вход к [???]',(500,0),(255,50,50))
        elif level == 2:
            location_Text = Text(None,50,f'Локация: Хоол',(500,0),(255,50,50))
            win.fill((200,200,200))
        elif level == 3:
            location_Text = Text(None,50,f'Локация: Запретная секция',(500,0),(255,50,50))
            win.fill((100,100,100))
        elif level == 4:
            location_Text = Text(None,50,f'Локация: Падение',(500,0),(255,50,50))
            win.fill((50,50,50))
        elif level == 5:
            location_Text = Text(None,25,f'!Controller of corect work!: Не открывай!!!',(255,0),(255,50,50))
            win.fill((random.randint(0,50),random.randint(0,50),random.randint(0,50)))
        if not pygame.mixer.get_busy():
            if level == 1:
                Parkur.Main.musics.Play(0)
            elif level == 2:
                Parkur.Main.musics.Play(1)
            elif level == 3:
                Parkur.Main.musics.Play(2)
            elif level == 4:
                Parkur.Main.musics.Play(3)
            elif level == 5:
                Parkur.Main.musics.Play(4)
        DeathCount_Text = Text(None,25,f'Смерти: {deaths}',(450,55),(255,255,50))
        level_Text = Text(None,50,f'Уровень: {level}',(0,0),(50,255,50))
        Timer_Text = Text(None,25,f'Время: {sec}:{min}:{hours}',(0,60),(50,255,255))
        keys = pygame.key.get_pressed()
        Player.Mouve(5,keys)
        Player.Update(keys,'',level,None,None,None)
        win.blit(Player.image,(Player.pos[0],Player.pos[1]))
        Load_Level(level,win,Player)
        level_Text.Render(win)
        location_Text.Render(win)
        Timer_Text.Render(win)
        DeathCount_Text.Render(win)
        pygame.display.update()
        clock.tick(FPS)
    exit()