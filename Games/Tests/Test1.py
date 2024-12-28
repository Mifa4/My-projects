import tkinter as vs #vs - Visual structure
#Tkinter — кросс-платформенная событийно-ориентированная графическая библиотека, написанная Стином Лумхольтом и Гвидо ван Россумом. Входит в стандартную библиотеку Python.


#list_nums = [1,2,3,3,2,1]#list
#tuple_nums = (1,2,3,3,2,1)#tuple
#set_nums = {1,2,3,3,2,1}#set
#dict_data = {'first': 1,'second': 2,'third': 3}#dict
#print(list_nums, type(list_nums) + '\n' + tuple_nums,type(tuple_nums) + '\n' + set_nums,type(set_nums) + '\n' + dict_data,type(dict_data))
#Creating win
win = vs.Tk()# win like window
canvas = vs.Canvas(win,bg='#15d18f',width=1080,height=900)#Canvas window,bg color,width,heights
#Game
def oval_movement(event):
    info_about_cords = canvas.coords(oval)
    if event.keysym == 'Up':
        canvas.move(oval,0,-5)
    elif event.keysym == 'Down':
        canvas.move(oval,0,5)
    elif event.keysym == 'Right':
        canvas.move(oval,5,0)
    elif event.keysym == 'Left':
        canvas.move(oval,-5,0)
    label.config(text=f'Inginirium\nMifsi\nVS code\nTKinter\nx: {str(info_about_cords[0])}, y:{str(info_about_cords[1])}')
    iac = canvas.coords(oval)
    if iac[0] < 0 or iac[1] < 0:
        canvas.moveto(oval,445,230)
    elif iac[0] > 1020 or iac[1] > 650:
        canvas.moveto(oval,445,230)
label = vs.Label(win,text='Inginirium\nMifsi\nVS code\nTKinter')
label.pack()
oval = canvas.create_oval((445,230),(500,300),fill='#27ab3b')#(x,y) size,(x,y) pos, color
canvas.create_line((100,5),(100,400),(200,10),(100,400),(300,15),(100,400),(0,0),fill='#831ad9')
#End
canvas.pack()#create canvas
win.bind("<KeyPress>",oval_movement)
win.mainloop()#if this thread close all deamon threads close too.