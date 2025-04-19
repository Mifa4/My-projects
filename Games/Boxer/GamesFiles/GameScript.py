from Varibles import *
from Methods import *
from Musics import *
from Texts import *

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

    TextRender()

    MusicPlayer()
    
    PlayerMouve()

    MusicChanging()
    
    SecretCodes()

    Displaying()
    pygame.display.update()
    clock.tick(FPS)