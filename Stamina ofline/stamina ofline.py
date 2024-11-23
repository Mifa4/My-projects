#v 1
import random
import time
from threading import Thread

seconds = 0
def timer():
    global seconds
    while True:
        time.sleep(1)
        seconds += 1

def Main():
    print("Чтоб начать нажмите Enter.")
    input()
    Programm()

def Programm():
    global seconds
    seconds = 0
    errors = 0
    words_sum = 0
    thread = Thread(target=timer, args=())
    thread.start()
    words = ['int','char','bool','True','False','print','try','while','double','long','long','except','random','if','else','elif','else if','%','/','*','-','!=','==','>=','<=','range','[]','python','#','\\n','\\t','\\r','input','sleep','socket','def','import','from','time','random','{key:value}','.py','for','len()','append()','time.sleep()','threading','Thread']
    while True:
        words_sum += 1
        max = len(words)-1
        need_world = words[random.randint(0,max)]
        word = input(f'Введите слово: {need_world}\n')
        if(word == need_world):
            continue
        elif(word == 'Exit'):
            words_sum -= 1
            break
        else:
            errors += 1
    if errors != 0:
        result = (errors / words_sum) * 100
    else:
        result = 0
    print(f'Вы совершаете ошибки в {result}% случиев.')
    word_in_seconds = seconds / words_sum
    print(f"1 слово за {word_in_seconds} секунд.")
    print(f"секунд: {seconds}.")
    input()

Main()

