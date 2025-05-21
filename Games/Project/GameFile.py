from Parkur.Main import *
import Parkur.Main
from Story.Console_of_secrets import *
import Story.Console_of_secrets
from time import sleep
res = Story.Console_of_secrets.Program()
if res[0] == 'P':
    buffer = ''
    for i in range(1,len(res)):
        buffer += str(res[i])
    Parkur.Main.level = int(buffer)
    Parkur_Time()
elif res[0] == 'S':
    Say('[VirtualKiller]:Зачем ты сюда вернулся?',0.15)
    Say('[VirtualKiller]:Ах да, награда!',0.15)
    Say('[Console of bad]: Объект награждает вас пустым сохранением!',0.000001)
    data = Read()
    Write([f'open:10000',f'name:',f'level_of_parkur:6',f'Time1:1.1.1',f'Time2:2.2.2',f'Time3:3.3.3',f'Time4:4.4.4',f'Time5:5.5.5',f'Deaths:660216925','!Controler of correct work!: !Controler of correct work!: Don`t redact that file!'])
    sleep(5)
    Story.Console_of_secrets.Err0r()
else:
    Say('[:)]:):):):):):):):):):)',0.25)
    input()