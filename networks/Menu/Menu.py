#This file created to easy creating "Menu" in console.
#Этот файл создан для простого "создания" Меню в консоле.

import time

localization = "en"

def Menu():
    global localization
    while True:
        if(localization == "en"):
            print("             Console     tail.               \n")
            time.sleep(1.5)
            print("     To play: P                 To settings:S\n")
        elif(localization == "рус"):
            print("             Console     tail.               \n")
            time.sleep(1.5)
            print("     Для игры: И              Для настроек: Н\n")
        do = input()
        if(do == "P" or do == "И"):
            Game()
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

def Game():
    pass