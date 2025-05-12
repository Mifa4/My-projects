import pygame
from time import sleep
from Classe import *
import Classe

pygame.init()
def Timer():
    global s,m,h
    sleep(1)
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0
        m = 0
        s = 0

