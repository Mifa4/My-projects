import pygame
import random
from threading import Thread
from time import sleep

sec,minutes,hour = 0,0,0
sec1,minutes1,hour1 = 0,0,0
sec2,minutes2,hour2 = 0,0,0
sec3,minutes3,hour3 = 0,0,0

pygame.init()
w,h = 500,500

win = pygame.display.set_mode((w,h))

FPS = 60
clock = pygame.time.Clock()

wl1 = w // 2
hl1 = h // 2
l1 = pygame.Surface((wl1,hl1))
l1_rgb = [255,0,255]
l1.fill((l1_rgb[0],l1_rgb[1],l1_rgb[2]))

wl2 = w // 2
hl2 = h //2
l2 = pygame.Surface((wl2,hl2))
l2_rgb = [255,0,0]
l2.fill((l2_rgb[0],l2_rgb[1],l2_rgb[2]))

wl3 = w // 2
hl3 = h //2
l3 = pygame.Surface((wl3,hl3))
l3_rgb = [0,0,255]
l3.fill((l3_rgb[0],l3_rgb[1],l3_rgb[2]))

wl4 = w // 2
hl4 = h //2
l4 = pygame.Surface((wl4,hl4))
l4_rgb = [255,255,0]
l4.fill((l4_rgb[0],l4_rgb[1],l4_rgb[2]))

image = pygame.image.load(r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Music Hitter\Images\UIPtester.png')
box = pygame.image.load(r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Music Hitter\Images\Box.png')
playerW = 50
playerH = 50
image = pygame.transform.scale(image,(playerW,playerH))
box = pygame.transform.scale(box,(playerW,playerH))
xPos = 0
yPos = 0
boxXPos = wl1 // 2
boxYPos = hl1 // 2
nl = 1
Font1 = pygame.font.Font(r'C:\WINDOWS\FONTS\COMIC.TTF',75)
Font2 = pygame.font.Font(r'C:\WINDOWS\FONTS\ITCBLKAD.TTF',75)
b1 = 1
b2 = 1
b3 = 1
b4 = 1
def Timer():
    global sec,minutes,hour, sec1, minutes1, hour1, sec2, sec3, minutes2, minutes3, hour2, hour3
    while True:
        sleep(1)
        if nl == 1:
            sec += 1
            if sec == 60:
                minutes += 1
                sec = 0
            if minutes == 60:
                hour += 1
                minutes = 0
            if hour == 24:
                sec,minutes,hour = 0,0,0
        elif nl == 2:
            sec1 += 1
            if sec1 == 60:
                minutes1 += 1
                sec1 = 0
            if minutes1 == 60:
                hour1 += 1
                minutes1 = 0
            if hour1 == 24:
                sec1,minutes1,hour1 = 0,0,0
        elif nl == 3:
            sec2 += 1
            if sec2 == 60:
                minutes2 += 1
                sec2 = 0
            if minutes2 == 60:
                hour2 += 1
                minutes2 = 0
            if hour2 == 24:
                sec2,minutes2,hour2 = 0,0,0
        else:
            sec3 += 1
            if sec3 == 60:
                minutes3 += 1
                sec3 = 0
            if minutes3 == 60:
                hour3 += 1
                minutes3 = 0
            if hour3== 24:
                sec3,minutes3,hour3 = 0,0,0
time = Thread(target=Timer)
time.start()
EndSound = pygame.mixer.Sound(r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Music Hitter\Musics\End.mp3')
HHorSound = pygame.mixer.Sound(r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Music Hitter\Musics\HHor.mp3')
FunnyYetSound = pygame.mixer.Sound(r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Music Hitter\Musics\FunnyYet.mp3')
PlakySound = pygame.mixer.Sound(r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Music Hitter\Musics\PlakyPlaky.mp3')
QuestionSound = pygame.mixer.Sound(r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Music Hitter\Musics\Flowey.mp3')
BIOSSound = pygame.mixer.Sound(r'C:\Users\nout_student4\Documents\GitHub\My-projects\Games\Music Hitter\Musics\BIOS.mp3')
ep = False
horp = False
funp = False
plak = False
deterp = False 

def Play(mus):
    global ep,horp,funp,deterp,plak
    ep = False
    horp = False
    funp = False
    plak = False
    EndSound.stop()
    HHorSound.stop()
    FunnyYetSound.stop()
    PlakySound.stop()
    BIOSSound.stop()
    if deterp != True:
        if mus == 'ep':
            EndSound.play()
            ep = True
        elif mus == 'horp':
            HHorSound.play()
            horp = True
        elif mus == 'funp':
            FunnyYetSound.play()
            funp = True
        elif mus == 'plak':
            PlakySound.play()
            plak = True
        elif mus == 'deterp':
            QuestionSound.play()
            deterp = True
        else:
            BIOSSound.play()
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    if l1_rgb == l2_rgb and l2_rgb == l3_rgb and l3_rgb == l4_rgb:
        Play('deterp')
    if not pygame.mixer.get_busy():
        if ep == True:
            Play('ep')
        elif horp == True:
            Play('horp')
        elif funp == True:
            Play('funp')
        elif plak == True:
            Play('plak')
        elif deterp == True:
            Play('deterp')
    L1Text = Font1.render(f'Биом{b1}',True,(255 - l1_rgb[0],255 - l1_rgb[1],255 - l1_rgb[2]))
    L2Text = Font1.render(f'Биом{b2}',True,(255 - l2_rgb[0],255 - l2_rgb[1],255 - l2_rgb[2]))
    L3Text = Font1.render(f'Биом{b3}',True,(255 - l3_rgb[0],255 - l3_rgb[1],255 - l3_rgb[2]))
    L4Text = Font1.render(f'Биом{b4}',True,(255 - l4_rgb[0],255 - l4_rgb[1],255 - l4_rgb[2]))
    time_text = f'{hour}:{minutes}:{sec}'
    time_text1 = f'{hour1}:{minutes1}:{sec1}'
    time_text2 = f'{hour2}:{minutes2}:{sec2}'
    time_text3 = f'{hour3}:{minutes3}:{sec3}'
    text_of_time = Font2.render(time_text,True,(255 - l1_rgb[0],255 - l1_rgb[1],255 -l1_rgb[2]))
    text_of_time2 = Font2.render(time_text1,True,(255 - l2_rgb[0],255 - l2_rgb[1],255 -l2_rgb[2]))
    text_of_time3 = Font2.render(time_text2,True,(255 - l3_rgb[0],255 - l3_rgb[1],255 -l3_rgb[2]))
    text_of_time4 = Font2.render(time_text3,True,(255 - l4_rgb[0],255 - l4_rgb[1],255 -l4_rgb[2]))
    l1.blit(L1Text,(wl1 // 2 - L1Text.get_width() // 2,hl1 // 2 - L1Text.get_height() // 2))
    l2.blit(L2Text,(wl2 // 2 - L2Text.get_width() // 2,hl2 // 2 - L2Text.get_height() // 2))
    l3.blit(L3Text,(wl3 // 2 - L3Text.get_width() // 2,hl3 // 2 - L3Text.get_height() // 2))
    l4.blit(L4Text,(wl4 // 2 - L4Text.get_width() // 2,hl4 // 2 - L4Text.get_height() // 2))
    l1.blit(text_of_time,(wl1 // 2 - text_of_time.get_width() // 2,0))
    l2.blit(text_of_time2,(wl2 // 2 - text_of_time2.get_width() // 2,0))
    l3.blit(text_of_time3,(wl3 // 2 - text_of_time3.get_width() // 2,0))
    l4.blit(text_of_time4,(wl4 // 2 - text_of_time4.get_width() // 2,0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        yPos -= 5
        if yPos <= 0:
            if nl == 3:
                nl = 1
                l3_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b3 += 1
                yPos = hl1 - playerH
            elif nl == 2:
                nl = 4
                l2_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b2 += 1
                yPos = hl1 - playerH
            elif nl == 1:
                nl = 3
                l1_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b1 += 1
                yPos = hl1 - playerH
            elif nl == 4:
                nl = 2
                l4_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b4 += 1
                yPos = hl1 - playerH
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        yPos += 5
        if yPos + playerH >= hl1:
            if nl == 4:
                nl = 2
                l4_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b4 += 1
            elif nl == 1:
                nl = 3
                l1_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b1 += 1
            elif nl == 2:
                nl = 4
                l2_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b2 += 1
            elif nl == 3:
                nl = 1
                l3_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b3 += 1
            yPos = 0

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        xPos -= 5
        if xPos <= 0:
            if nl == 2:
                nl = 1
                l2_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b2 += 1
                xPos = wl1 - playerW
            elif nl == 4:
                nl = 3
                l4_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b4 += 1
                xPos = wl1 - playerW
            elif nl == 3:
                nl = 4
                l3_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b3 += 1
                xPos = wl1 - playerW
            elif nl == 1:
                nl = 2
                l1_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b1 += 1
                xPos = wl1 - playerW
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        xPos += 5
        if xPos + playerW >= wl1:
            if nl == 4:
                nl = 3
                l4_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b4 += 1
            elif nl == 2:
                nl = 1
                l2_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b2 += 1
            elif nl == 1:
                nl = 2
                l1_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b1 += 1
            elif nl == 3:
                nl = 4
                l3_rgb = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
                b3 += 1
            xPos = 0
    
    if keys[pygame.K_q] and keys[pygame.K_SPACE]:
        l1_rgb = [255,0,0]
        l2_rgb = [255,0,0]
        l3_rgb = [255,0,0]
        l4_rgb = [255,0,0]
    if keys[pygame.K_b] and keys[pygame.K_f]:
        Play('')

    if nl == win:
        nl = 1
        xPos = 1
        yPos = 1
    
    if nl == 1:
        l1.blit(image,(xPos,yPos))
        l1.blit(box,(boxXPos,boxYPos))
        if not funp:
            Play('funp')
    if nl == 2:
        l2.blit(image,(xPos,yPos))
        l2.blit(box,(boxXPos,boxYPos))
        if not horp:
            Play('horp')
    if nl == 3:
        l3.blit(image,(xPos,yPos))
        l3.blit(box,(boxXPos,boxYPos))
        if not plak:
            Play('plak')
    if nl == 4:
        l4.blit(image,(xPos,yPos))
        l4.blit(box,(boxXPos,boxYPos))
        if not ep:
            Play('ep')
    win.fill((255,255,255))
    win.blit(l1,(0,0))
    win.blit(l2,(w // 2,0))
    win.blit(l3,(0,h // 2))
    win.blit(l4,(w // 2,h // 2))
    l1.fill((l1_rgb[0],l1_rgb[1],l1_rgb[2]))
    l2.fill((l2_rgb[0],l2_rgb[1],l2_rgb[2]))
    l3.fill((l3_rgb[0],l3_rgb[1],l3_rgb[2]))
    l4.fill((l4_rgb[0],l4_rgb[1],l4_rgb[2]))
    pygame.display.update()
    clock.tick(FPS)

    #300 lines