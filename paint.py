import tkinter as tk

app = tk.Tk()
app.title("CANVAS")
app.geometry("800x600")
app.config(bg="gray")

cvas = tk.Canvas(app, bg='white', width=800, height=550)
cvas.pack()

X = tk.IntVar(value=0)
Y = tk.IntVar(value=0)
foreColor = '#000000'
backColor = '#FFFFFF'
b = tk.Button(app, text="Done")
b.pack(side="bottom")


def onLeftButtonDown(self):
    X.set(self.x)
    Y.set(self.y)
cvas.bind('<Button-1>', onLeftButtonDown)  

def onLeftButtonMove(event):
    cvas.create_line(X.get(), Y.get(), event.x, event.y, fill=foreColor)
    X.set(event.x)
    Y.set(event.y)
cvas.bind('<B1-Motion>', onLeftButtonMove)  

def onRightButtonDown(self):
    X.set(self.x)
    Y.set(self.y)
cvas.bind('<Button-3>', onRightButtonDown)  

def onRightButtonMove(event):
    cvas.create_line(X.get(), Y.get(), event.x, event.y, width=5, fill=backColor)
    X.set(event.x)
    Y.set(event.y)
cvas.bind('<B3-Motion>', onRightButtonMove)

app.mainloop()