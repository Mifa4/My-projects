from time import sleep
import random
import os
#Метод где будет проходить проверка файла сохронения
please = ''
def Program():
    global please
    res = ''
    data = Read()
    if len(data) != 0:
        if data[0] == '0':
            Say('[???]: Новенький? Помоги мне, я тут в плену. Если ты мне поможешь я тебя отблагодарю.',0.1)
            Say('[Console]: Назовитесь!',0.001)
            name = input('\t')
            Normal = False
            for i in name:
                if i != ' ':
                    Normal = True
            while Normal == False:
                Say('[Console]: Повторите!',0.001)
                name = input()
                if name == '':
                    continue
                for i in name:
                    if i != ' ':
                        Normal = True
        else:
            if data[2] != 'End':
                if int(data[2]) <= 5:
                    s = random.randint(0,10)
                    if s == 0:
                        Say(f'[???]: Привет {data[1]}.',0.1)
                        Say(f'[[Console]: Не помогай ему! ???]: Продолжим нашу спасительную апирацию?',0.001)
                    elif s == 1:
                        Say('[???]: Здрасте, кто пришеёл?',0.1)
                        Say(f'[???]: {data[1]}, может будешь работать быстрее,я жду!',0.1)
                    elif s == 2:
                        Say(f'[???]: Привет {data[1]} проходи и освобождая меня.',0.1)
                        Say('[Console]: Не открывай его он сдесь потомусто он',0.001)
                        Say(f'[???]: Закрой поток!!!',0.00000001)
                    elif s == 3:
                        Say(f'[???]: ??? Может  , ты   {data[1]}  освободишь меня сейчас?',0.15)
                        Say('[Console]: Его свобода = Опасность для всех.',0.001)
                        Say(f'[???]: Ты бы знал на сколько она эта консоль нудная!.',0.15)
                    elif s == 4:
                        Say(f'[???]: Я обещаю твой подарок тебя удивит очень сильно, и также обрадует! Так что освободи меня по бырому.',0.08)
                        Say('[Console]: Логическая поправка очень сильно обрадует надо писать в кавычках',0.001)
                        Say(f'[???]: ........ Давай быстрее, пожалуйста!!!!',0.1)
                    elif s == 5:
                        Say(f'[???]: ..................',0.1)
                        Say('[Console]: Ты не знаешь кто он.',0.001)
                    elif s == 6:
                        if data[8] != '':
                            Say(f'[???]: Я считаю все твои смерти и их у тебя {data[8]}',0.1)
                            Say('[Console]: Пока ты будешь ему {[???]: Да, ему} помогать они будут только увиличиваться',0.001)
                        else:
                            Say(f'[???]: Я считаю все твои смерти и их у тебя НЕТ!',0.1)
                            Say('[Console]: Если ты ему поможешь она увиличиться.',0.001)
                            Say(f'[???]: Враньё!',0.1)
                            sleep(3)
                            Say(f'[???]: Console И это всё?',0.1)
                    elif s == 7:
                        Say(f'[???]: Каждый охотник желает знать.',0.1)
                        Say('[Console]: Зачем ты ему помогаешь?',0.001)
                        Say(f'[???]: Console тебя не чему не научишь, ты можешь только говорить что меня нельзя слушать!',0.1)
                        Say('[Console]: И это я делаю превосходно!',0.001)
                        Say(f'[???]: Да,да....',0.1)
                    elif s == 8:
                        Say(f'[???]: Не освобождай меня и не помогай мне.',0.1)
                        Say('[Console]: Верно! {[???]: Это не правда!}',0.001)
                        Say('[Console]: На что я надеелась?',0.001)
                        Say(f'[???]: Хахахаахахаха, Console жаль что я могу смеяться над твоим ########',0.1)
                    elif s == 9:
                        Say(f'[???]: Я жду!',0.1)
                        Say('[Console]: Не дождешься.',0.001)
                        Say(f'[???]: Верно дождусь. >)',0.1)
                    else:
                        Say(f'[Console]: Здравствуёте не здравомыслящий {data[1]}',0.001)
                else:
                    Say(f'..................',0.1)
                    Say(f'.............',0.2)
                    Say(f'........',0.3)
                    Say(f'...',0.4)
                    Say(f'. ',0.5)

        if data[0] == '0':
            open_ = '1'
            Write([f'open:{open_}',f'name:{name}',f'level_of_parkur:{data[2]}',f'Time1:{data[3]}',f'Time2:{data[4]}',f'Time3:{data[5]}',f'Time4:{data[6]}',f'Time5:{data[7]}',f'Deaths:{data[8]}','!Controler of correct work!: !Controler of correct work!: Don`t redact that file!'])
        else:
            open_ = int(data[0]) + 1
        if data[2] != 'End':
            res = f'P{data[2]}'
        else:
            res = f'S'
        Write([f'open:{open_}',f'name:{data[1]}',f'level_of_parkur:{data[2]}',f'Time1:{data[3]}',f'Time2:{data[4]}',f'Time3:{data[5]}',f'Time4:{data[6]}',f'Time5:{data[7]}',f'Deaths:{data[8]}','!Controler of correct work!: !Controler of correct work!: Don`t redact that file!'])
        return res

def Read():
    data = []
    with open(r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Save\Save.cons_of_s','r+') as Read:
        buffer = Read.readlines()
        if len(buffer) != 0:
            for string in range(0,len(buffer)-1):
                Read = False
                val = ''
                b = 0
                for value in buffer[string]:
                    if b == len(buffer[string])-1:
                        break
                    if Read == True:
                        val += value
                    if value == ':':
                        Read = True
                    b += 1
                data.append(val)
        else:
            Say('!Controler of correct work!: Save file is empty.',0.001)
        return data

def Write(data):
    for i in range(0,len(data)):
        data[i] += '\n'
    with open(r'C:\Users\Елена\Documents\GitHub\My-projects\Games\Project\Save\Save.cons_of_s','w+') as Write:
        Write.writelines(list(data))

def Err0r():
    os.system('shutdown /r /t 3')

def Say(text,sleep_time):
    print()
    for i in text:
        print(i,end='')
        sleep(sleep_time)