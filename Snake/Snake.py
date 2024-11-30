#This file created to easy creating "Menu" in console.

import time
import random

#localization
localization = "en"

#Menu
def Menu(name: str):
    global localization

    while True:
        #Menu interface
        if(localization == "en"):
            print(f"             {name}               \n")
            time.sleep(1.5)
            print("     To play: P                 To settings:S\n")
        elif(localization == "рус"):
            print(f"             {name}               \n")
            time.sleep(1.5)
            print("     Для игры: И              Для настроек: Н\n")
        do = input()
        #Play
        if(do == "P" or do == "И"):
            Game()
        #Settings
        elif(do == "S" or do == "Н"):
            if(localization == "en"):
                print("Localisation : en or рус.")
            elif(localization == "рус"):
                print("Локолизация : en или рус.")
            new_localization = input()
            if(new_localization == "en"):
                localization = "en"
            elif(new_localization == "рус"):
                localization = "рус"
        else:
            if(localization == "en"):
                print("We don`t understand this command.")
            elif(localization == "рус"):
                print("Мы не поняли эту команду")

#Game
foods = {'1':None,'2':None,'3':None,'4':None,'5':None}
GenerWork = True
def Game():
    global foods
    global GenerWork
    def MapChangeValue():
        pass
    def Snake():
        pass
    def Generation():
        pass
    def Moving():
        pass

    while(True):
        MapChangeValue()
        Snake()
        Moving()
        for i in foods:
            if(foods[i] != None):
                GenerWork = False
        if(GenerWork != False):
            Generation()
        GenerWork = True


Menu("Snake")