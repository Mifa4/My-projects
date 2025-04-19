from Varibles import *
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
def MusicPlayer():
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
def MusicChanging():
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