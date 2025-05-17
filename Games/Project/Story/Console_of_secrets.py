from time import sleep
def Program():
    res = ''
    Say('!Controler of correct work!: Этой консоли для корректной обработки файлов необходимо указать путь до папки где содержиться этот файл с окончанием на \\ \nНа пример: C:\\Users\\User\\Desktop\\This_Game\\.',0.01)
    please = input()
    please = input('!Controler of correct work!: Этой консоли для корректной обработки файлов необходимо указать путь до папки где содержиться этот файл с окончанием на \\ \nнапример: C:\\Users\\User\\Desktop\\This_Game\\.')
    s = open(f'{please}Save\Save.cons_of_s','r')
    reader = s.readlines()
    data = Reader(reader)
    open_ = data[0]
    name = data[1]
    lv_p = data[2]
    lv_s = data[3]
    if data[0] == '0' or data[0] == ' ' or data[0] == '':
        Say('[???]: Новенький? Помоги мне, я тут застрял.',0.1)
        Say('[Console]: Назовитесь!',0.001)
        name = input()
        name = input('[???]: Новенький? Помоги мне, я тут застрял.\n[Console]: Назовитесь\t')
        while name != '' or name != ' ':
            Say('[Console]: Повторите!',0.001)
            name = input()
    while name != '' or name != ' ':
        Say('!Controler of correct work!: No_critical_error_1',0.01)
        Say('[{???}:?????????]: Перевожу, Ошибка "кто-то побаловался с файлом сохранения", а именно "именем".',0.1)
        name = input()
    else:
        Say(f'[???]: Привет {data[1]}',0.1)
        if data[1] == ' ' or data[1] == '':
            Say('[???]: Я тебя забыл или,\n{?Удивленние?}[???]:Назовись!\t',0.1)
            name = input()
            name = input('[???]: Я тебя забыл или,\n{?Удивленние?}[Пленик]:Назовись!\t')
    if data[0] == '0' or data[0] == ' ' or data[0] == '':
        open_ = '1'
    else:
        open_ = int(data[0]) + 1
    if data[2] != 'End' or data[2] != 'end':
        res = f'P{data[2]}'
    else:
        res = f'S{data[3]}'
    w = open(f'{please}Save\Save.cons_of_s','w')
    Writer([open_,name,lv_p,lv_s],reader)
    w.close()
    s.close()
    return res

def Reader(reader):
    open_ = reader[0]
    name = reader[1]
    parkur = reader[2]
    shouter = reader[3]
    open_ = Read(open_)
    name = Read(name)
    parkur = Read(parkur)
    shouter = Read(shouter)
    return [open_,name,parkur,shouter]

def Read(string):
    for i in range(0,len(string)):
        buffer = ''
        r = False
        if r:
            buffer += string[i]
        if string[i] == ' ' and string[i-1] == ':':
            r = True
    return buffer

def Writer(data,file):
    Write(file,data)

def Write(file,data):
    buffer = ''
    for i in range(0,len(file)):
        for j in range(0,len(file[i])):
            buffer += file[i][j]
            if file[i][j] == ' ' and file[i][j-1] == ':':
                for b in range(j,len(file[i])):
                    buffer += data[i][b]
        buffer += '\n'

def Err0r():
    pass

def Say(text,sleep_time):
    print()
    for i in text:
        print(i,end='')
        sleep(sleep_time)