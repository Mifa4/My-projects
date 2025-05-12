from Parkur.Main import *
import Parkur.Main
from Story.Console_of_secrets import *
import Story.Console_of_secrets

res = Story.Console_of_secrets.Program()
if res[0] == 'P':
    buffer = ''
    for i in range(1,len(res)):
        buffer += res[i]
    Parkur.Main.Parkur_Time(buffer)
elif res[1] == 'S':
    Story.Console_of_secrets.Err0r()
else:
    print(':)')
    input()