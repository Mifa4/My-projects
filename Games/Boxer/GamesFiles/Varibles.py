#importing
import pygame
import random
from threading import Thread
from time import sleep

pygame.init()
#timer
sec,minutes,hour = 0,0,0
sec1,minutes1,hour1 = 0,0,0
sec2,minutes2,hour2 = 0,0,0
sec3,minutes3,hour3 = 0,0,0
FPS = 60
clock = pygame.time.Clock()

#window size
w,h = 500,500

#Surfaces
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

#images
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

#Fonts
Font1 = pygame.font.Font(r'C:\WINDOWS\FONTS\COMIC.TTF',75)
Font2 = pygame.font.Font(r'C:\WINDOWS\FONTS\ITCBLKAD.TTF',75)

#Count of bioms
nl = 1
b1 = 1
b2 = 1
b3 = 1
b4 = 1

#Keys
keys = pygame.key.get_pressed()

#win
win = pygame.display.set_mode((w,h))
if nl == win:
        nl = 1
        xPos = 1
        yPos = 1