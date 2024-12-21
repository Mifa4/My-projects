import threading
import pyglet
path = input('Где этот проект? пример: C:\\Users\\You\\Documents\\GitHub\\My-projects\\My-projects\\MusicPlayer \n') + '\\musics\\'
pathSave = path
path += input('Имя файла в папке music ((пример: test) автоматичиски добовляет .mp3 к файлу):\t') + '.mp3'
def Player(path):
    song = pyglet.media.load(path)
    song.play()
    pyglet.app.run()
mainPlayerThr = threading.Thread(target=Player,name='Player',args=(path,),daemon=True)
mainPlayerThr.start()

while True:
    do = input()
    if(do == 'close'):
        break
    if(do == 'exit'):
        pyglet.app.exit()
        mainPlayerThr.join()