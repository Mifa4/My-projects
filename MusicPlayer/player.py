import threading
import pyglet
path = input('Where is the project? example: C:\\Users\\You\\Documents\\GitHub\\My-projects\\My-projects\\MusicPlayer \n') + '\\musics\\'

path += input('Имя файла в папке music ((example: test) automaticly add .mp3):\t') + '.mp3'
def Player(path):
    song = pyglet.media.load(path)
    song.play()
mainPlayerThr = threading.Thread(target=Player,name='Player',args=(path,))
mainPlayerThr.start()
pyglet.app.run()