import pygame
import time

class MenuStructurer:
    def __init__(self,playerName,checkpoints,MenuWhaiter):
        self.playerName = playerName
        if type(checkpoints) == type(['','','',0]):
            if len(checkpoints) != 0:
                self.checkpoints = checkpoints
            else:
                self.checkpoints = ['']
        if type(MenuWhaiter) == type(1.4) or type(MenuWhaiter) == type(1):
            self.MenuWhaiter = MenuWhaiter
        else:
            self.MenuWhaiter = 0
        self.save = checkpoints[0]
        self.MenuSaver('read save',None)
        self.exit = False
        self.Play = False
        self.run = 1
        self.MenuSaver('read starts',None)


    def Menu(self):
        if self.save == self.checkpoints[0] + '\n' or self.save == self.checkpoints[0]:
            self.Poster(f'[MS]: Hello {self.playerName}.\n[MS]: Long time no see, let`s continue your adventure.\n[MS]: If you ready right comand "\\P",or "\\Q" if you want to quit.\n[MS]: Do you know what do command "\\S".',self.MenuWhaiter)
            while self.exit == False or self.Play == True:
                self.Poster('[CMD]: Enter command.',self.MenuWhaiter)
                do = input(f'[{self.playerName}]:\t')
                if do == '\\P':
                    self.Poster('[MS]: Let`s have fun!',self.MenuWhaiter)
                    self.Play = True
                elif do == '\\Q':
                    self.MenuSaver('save','Researched')
                    self.Poster('[MS]: WHY I ALONE AGAIN????',self.MenuWhaiter)
                    self.exit = True
                elif do == '\\S':
                    self.Poster('[MS]: This command doesn`t do anything.\n[CMD]: "Settings\\settings.txt" no such file or derictory.',self.MenuWhaiter)
                else:
                    self.Poster('[CMD]: Un registry command.',self.MenuWhaiter)
        elif (self.save == self.checkpoints[1] + '\n' or self.save == self.checkpoints[1]) and int(self.run) < 5:
            self.Poster(f'[MS]: Hello {self.playerName}.\n[MS]: It was so long.\n[MS]: I think i need remember only comands "\\P",or "\\Q".\n[MS]: !%$@!^#%^#!. "\\S".',self.MenuWhaiter)
            while self.exit == False or self.Play == True:
                self.Poster('[CMD]: Enter command.',self.MenuWhaiter)
                do = input(f'[{self.playerName}]:\t')
                if do == '\\P':
                    self.Poster('[MS]: Let`s have fun!',self.MenuWhaiter)
                    self.Play = True
                elif do == '\\Q':
                    self.MenuSaver('save','Researched')
                    self.Poster('[MS]: Goodbye, maybe. I Don`t want be ALON!',self.MenuWhaiter)
                    self.exit = True
                elif do == '\\S':
                    self.Poster('[MS]: ...\n[CMD]: "Settings\\settings.txt" you don`t have permission to open or change this file.',self.MenuWhaiter)
                else:
                    self.Poster('[CMD]: Un registry command.\n[MS]:Let`s be sirious.',self.MenuWhaiter)
        elif (self.save == self.checkpoints[1] + '\n' or self.save == self.checkpoints[1]) and int(self.run) >= 5:
            self.Poster(f'[MS]: Hello {self.playerName},You my best friend.\n[MS]: Continue "\\P",exit "\\Q".\n[MS]: "\\S".',self.MenuWhaiter)
            while self.exit == False or self.Play == True:
                self.Poster('[CMD]: Enter command.',self.MenuWhaiter)
                do = input(f'[{self.playerName}]:\t')
                if do == '\\P':
                    self.Poster('[MS]: :)',self.MenuWhaiter)
                    self.Play = True
                elif do == '\\Q':
                    self.MenuSaver('save','Researched')
                    self.Poster('A   L    O   N',self.MenuWhaiter)
                    self.exit = True
                elif do == '\\S':
                    self.Poster('[MS]: ...my secret...\n[CMD]: "Settings\\settings.txt" you can`t open this file.',self.MenuWhaiter)
                else:
                    self.Poster('[CMD]: Un registry command.\n[MS]: =(',self.MenuWhaiter)

    def Poster(self,text,waiter):
        for i in text:
            print(i,end='')
            time.sleep(waiter)
        print()

    def MenuSaver(self,method,checkpoint):
        if method == 'save' or method == 0:
            fl = ['Researched N3','1']
            with open("Saves\\MenuSave.txt",'r+') as SaveFile:
                fl = SaveFile.readlines()
            with open("Saves\\MenuSave.txt",'w+') as SaveFile:
                pass
            with open("Saves\\MenuSave.txt",'r+') as SaveFile:
                SaveFile.seek(0)
                if len(fl) == 0:
                    fl = ['Researched N3','1']
                for i in self.checkpoints:
                    if checkpoint == i:
                        SaveFile.write(f'{checkpoint}\n{int(fl[1]) + 1}')
        elif method == 'read save' or method == 1:
            with open("Saves\\MenuSave.txt",'r+') as SaveFile:
                SaveFile.seek(0)
                fl = SaveFile.readlines()
                if len(fl) == 0:
                    fl = ['Researched N3','1']
                if fl[0] == '' or fl[0] == f'{self.checkpoints[0]}':
                    self.save = self.checkpoints[0]
                else:
                    self.save = fl[0]
        elif method == 'read starts' or method == 2:
            with open("Saves\\MenuSave.txt",'r+') as SaveFile:
                SaveFile.seek(0)
                fl = SaveFile.readlines()
                if len(fl) == 0:
                    fl = ['Researched N3','1']
                if fl[1] == '' or fl[1] == '1':
                    self.run = 1
                else:
                    self.run = fl[1]

Game = MenuStructurer('Researched №3',['Researched N3','Researched','New user'],0.05)
Game.Menu()
if Game.exit == False:
    pass