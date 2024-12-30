import tkinter as g

window = g.Tk()
canvas = g.Canvas(window,bg='#751d09',width=400,height=400)
start = False
Lable = g.Label(window,text='Created by Mifsi\nWith using Vs code->python->Tkinter')
Lable.pack()
canvas.create_line((1.5,0),(1.5,400),fill='#0285e3')
canvas.create_line((400,0),(400,400),fill='#0285e3')
canvas.create_line((0,1.5),(400,1.5),fill='#0285e3')
canvas.create_line((0,400),(400,400),fill='#0285e3')
def Start(event):
    global start
    if start != True:
        if event.keysym == 's' or event.keysym == 'S':
            Lable.config(text='We started.')
            start = True
            for i in range(1,8,1):
                canvas.create_line((400,i * 50),(0,i * 50),fill='#331507')
                canvas.create_line((i * 50,400),(i * 50,0),fill='#331507')
            for b in range(0,3,1):
                for i in range(1,9,2):
                    if b % 2 != 0:
                        canvas.create_oval((50 + (50 * i),0 + (b * 50)),(50 * i,50 + (b * 50)),fill='black')
                    else:
                        canvas.create_oval((0 + (50 * (i - 1)),0 + (b * 50)),(50 * i,50 + (b * 50)),fill='black')
                    if b % 2 != 0:
                        canvas.create_oval((50 + (50 * i),400 - (b * 50)),(50 * i,350 - (b * 50)),fill='white')
                    else:
                        canvas.create_oval((0 + (50 * (i - 1)),400 - (b * 50)),(50 * i,350 - (b * 50)),fill='white')
            canvas.create_line((1.5,0),(1.5,400),fill='#cc02e3')
            canvas.create_line((400,0),(400,400),fill='#cc02e3')
            canvas.create_line((0,1.5),(400,1.5),fill='#cc02e3')
            canvas.create_line((0,400),(400,400),fill='#cc02e3')
    else:
        if event.keysym == 's' or event.keysym == 'S':
            Lable.config(text='We can`t started again.')
        elif event.keysym == 'Q' or event.keysym == 'Q':
            Lable.config(text='Goodbye.')
            window.quit()
            
canvas.pack()
window.bind("<KeyPress>",Start)
window.mainloop()