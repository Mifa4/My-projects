import pygame

class GameStructurer:
    def __init__(self,playerName,checkpoints):
        self.playerName = playerName
        self.chrckpoints = checkpoints

    def MainSysteam(self):
        pass

    def Menu(self):
        pass

    def Poster(self):
        pass

    def Saver(self,method,checkpoint):
        if method == 'save' or method == 0:
            with open("Save.txt",'w+') as SaveFile:
                SaveFile.write(f'{checkpoint}')