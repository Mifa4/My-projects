import tkinter as g

window = g.Tk()
canvas = g.Canvas(window,bg='#751d09',width=400,height=400)
start = False
def Start(event):
    global start
    if start != True:
        if event.keysym == 's' or event.keysym == 'S':
            start = True
            for i in range(1,8,1):
                canvas.create_line((400,i * 50),(0,i * 50))
                canvas.create_line((i * 50,400),(i * 50,0))
canvas.pack()
window.bind("<KeyPress>",Start)
window.mainloop()