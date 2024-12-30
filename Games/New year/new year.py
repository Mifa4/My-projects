import tkinter
from tkinter import PhotoImage

win = tkinter.Tk()
lable = tkinter.Label(win,text='Let`s play game')
player = None
player_img = tkinter.PhotoImage(file=r".\dedMoroz.png")
canvas = tkinter.Canvas(win,bg='#2f6317',width=1080,height=900)#Canvas window,bg color,width,heights
#Game
def Player():
    global player,player_img
    canvas.delete("all")
    player_pos = (460,225)
    player = canvas.create_image((player_pos[0],player_pos[1]),image=player_img,anchor='nw')
    lable.config(text=f'Find object!\nYour cords: x {canvas.coords(player)[0]},y {canvas.coords(player)[1]}')

def Stoper(player):
    xy = canvas.coords(player)
    if xy[0] <= 0:
        canvas.move(player,5,0)
    if xy[0] >= 840:
        canvas.move(player,-5,0)

    if xy[1] <= 0:
        canvas.move(player,0,5)
    if xy[1] >= 505:
        canvas.move(player,0,-5)

def movement(event):

    Stoper(player)
    lable.config(text=f'Find object!\nYour cords: x {canvas.coords(player)[0]},y {canvas.coords(player)[1]}')
    if event.keysym == 'Up':
        canvas.move(player,0,-5)
    elif event.keysym == 'Down':
        canvas.move(player,0,5)
    elif event.keysym == 'Right':
        canvas.move(player,5,0)
    elif event.keysym == 'Left':
        canvas.move(player,-5,0)
Player()
pos_P = canvas.coords(player)
#while True:
#   player_img = tkinter.PhotoImage(file=r".\dedMoroz.png")
#   player = canvas.create_image((pos_P[0],pos_P[1]),image=player_img,anchor='nw')
#   player_img = tkinter.PhotoImage(file=r".\dedMoroz1.png")
#   player = canvas.create_image((pos_P[0],pos_P[1]), image=player_img, anchor='nw')
#   player_img = tkinter.PhotoImage(file=r".\dedMoroz2.png")
#   player = canvas.create_image((pos_P[0],pos_P[1]), image=player_img, anchor='nw')
#   player_img = tkinter.PhotoImage(file=r".\dedMoroz3.png")
#   player = canvas.create_image((pos_P[0],pos_P[1]), image=player_img, anchor='nw')
lable.pack()
canvas.pack()
win.bind("<KeyPress>",movement)
win.mainloop()
