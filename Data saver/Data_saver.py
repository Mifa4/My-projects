import datetime
import shutil
from shutil import copyfile, copytree
import os
import time


def Main():
    try:
        i = 0
        print("Path to copy file.")
        pathFile = input()
        print("One once in hour value.")
        timer = int(input())
        if timer < 10:
            timer = 10
        print("\nWork moment: One once in " + str(timer) + ".\n" + "copy file path: " + str(pathFile))
        while True:
            i += 1
            print("interation: " + str(i))
            ProgramConstructor(pathFile)
            time.sleep(timer)
    except:
        print("Error1: Error in inputs values.")
    
def ProgramConstructor(pathFile):
    ExistChecker(pathFile)

def ExistChecker(pathFile):
    if os.path.exists(pathFile):
        Creator(pathFile)
    else:
        print("Error2: doesen`t exists path.")

def Creator(pathFile):
    try:
        file = False
        fileExist = False
        inumeratorFile = 0
        b = -1
        d = -1
        ToFile = ""
        ToFileExist = ""
        fileMassive = list(pathFile)
        while True:
            ToFileExist = ""
            d = -1
            for e in fileMassive:
                    d += 1
                    if e == ".":
                        fileExist = True
                        ToFileExist += "-copy" + str(inumeratorFile) + "."
                    else:
                        ToFileExist += fileMassive[d]
            if fileExist == False:
                break

            if os.path.exists(ToFileExist):
                inumeratorFile += 1
            else:
                for x in fileMassive:
                    b += 1
                    if x == ".":
                        file = True
                        ToFile += "-copy" + str(inumeratorFile) + "."
                    else:
                        ToFile += fileMassive[b]
                break
        if fileExist == False:
            while True:
                if os.path.exists(ToFileExist + "-copy" + str(inumeratorFile)):
                    inumeratorFile += 1
                else:
                    ToFileExist += "-copy" + str(inumeratorFile)
                    break
            copytree(pathFile,ToFileExist)
        else:
            copyfile(pathFile,ToFile)
    except :
        print("Error3: error in the core")
Main()