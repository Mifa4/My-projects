import time;

#Hello in the code of my project: console tale.
#Привет в коде моего проекта: console tale.

#game varibels.
#игровые переменные.
localization = "en"
#1 - зло 0 - добро
endResulter = [0]
#Main method start first.
#Главный метод стартует последним.

def Main():
    Menu_worker()

#Start menu.
#Запускает меню.
def Menu_worker():
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
            endResulter = [0]
            Game_worker()
            Ender("end",0)
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


#All game.
#Вся игра.
def Game_worker():
    global localization
    #create code:
    #код создания:
        #res = Messeger("start text...",{"Hello,what is start text?":'How are you',"Hello.":'...'})
        #if (res == "How are you?"):
        #   res = Messeger("",{"Good":'It is bad',"bad":'It is good'})
        #else:
        #   res = Messeger("",{"...":'...',"Do you exist.":'No.'})
        #res = Messeger("So let`s go",{"ok":'...',"Do you ok.":'No.'})
    if(localization == "en"):
        pass
    else:
        pass

#Help method to create texts.
#Метод помошник по созданию текстов.
def Messager(start_text,answer_results_cartedg):
    res = ""
    print(start_text)
    answers = []
    for i in answer_results_cartedg:
        answers.append(i)
    while True:
        print("Ответы: ",end='')
        for i in answers:
            print(i,end=' ')
        print(".")
        answer = input()
        have = False
        for i in answers:
            print(i)
            if(i == answer):
                have = True
        if (have == True):
            res = answer_results_cartedg[answer]
            print(answer_results_cartedg[answer])
            break
        else:
            print("Попробуй еще.")
    return res

#Save chose variant and give you ending.
#Сохраняет выбраный вариант и дает концовку.
def Ender(method,value):
    if (method == "save" or 0):
        endResulter.append(value)
    elif(method == "end" or 1):
        #start: max end: min
        Sum = 0
        try:
            for i in endResulter:
                Sum += float(i)
        except:
            print("Error whith data!")
        #checking

        # big bad(i >= 1) -> 
        # bad(i < 1 and i >= 0.7) -> 
        # small bad(i < 0.7 and i >= 0.5) -> 
        # bad normal(i < 0.5 and i >= 0.4) -> 
        # normal(i < 0.4 and i >= 0.2) -> 
        # small normal(i < 0.2 and i > 0.1) -> 
        # normal good(i <= 0.1 and i >= 0) -> 
        # good(i <= 0.1 and i >= 0.05) -> 
        # very good(i < 0.05 and i >= 0) ->
        # very very good?(i < 0)

        #!!! results[10] {"big bad","bad","small bad","bad normal","normal","small normal","normal good","good","very good","?? good"}
        #English endings
        result_text_en = ["","","","","","","","","",""]
        #Russian endings
        result_text_ru = ["","","","","","","","","",""]
        if localization == "en":
            EndingChecker(Sum,result_text_en)
        if localization == "рус":
            EndingChecker(Sum,result_text_ru)

def EndingChecker(Sum,results):
    #big bad(i >= 1) - 
    if(Sum >= 1):
        print(results[0])
    # bad(i < 1 and i >= 0.7) - 
    elif(Sum < 1 and Sum >= 0.7):
        print(results[1])
    # small bad(i < 0.7 and i >= 0.5) - 
    elif(Sum < 0.7 and Sum >= 0.5):
        print(results[2])
    # bad normal(i < 0.5 and i >= 0.4) - 
    elif(Sum < 0.5 and Sum >= 0.4):
        print(results[3])
    # normal(i < 0.4 and i >= 0.2) - 
    elif(Sum < 0.4 and Sum >= 0.2):
        print(results[4])
    # small normal(i < 0.2 and i > 0.1) -
    elif(Sum < 0.2 and Sum >= 0.1):
        print(results[5])
    # normal good(i <= 0.1 and i >= 0) -
    elif(Sum < 0.1 and Sum >= 0):
        print(results[6])
    #good(i <= 0.1 and i >= 0.05) -
    elif(Sum < 0.1 and Sum >= 0.05):
        print(results[7])
    # very good(i < 0.05 and i >= 0) -
    elif(Sum < 0.05 and Sum >= 0):
        print(results[8])
    # very very good?(i < 0)
    else:
        print(results[9])
        
            

#author Mifsi
#автор Mifsi

Main()