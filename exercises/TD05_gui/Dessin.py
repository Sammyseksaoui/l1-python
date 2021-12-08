import tkinter as tk
from tkinter.constants import N, NE

CANVAS_WIDTH, CANVAS_HEIGHT = 1200, 800

root = tk.Tk()
canvas1 = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)  
root.title ("Mon Dessin")
global objects
objects = []
def write_slogan():
    print("bouton appuyé")


def creer_disque () :
    x0 = 300
    x1 = 200
    y = CANVAS_HEIGHT / 2
    y1 = 500
    canvas1.create_oval(x0 - 50 , y - 50 , x1 + 50 , y1+ 50,outline="blue", fill="blue")
    return canvas1.create_oval(x0, y, x1, y1)
def creer_carre () :
    points = [150, 100, 200, 100, 150, 200, 200,
    200]
    mycarre = canvas1.create_polygon(points, outline='red',
    fill='red', width=2)
    return canvas1.create_polygon (points,outline = 'red',fill= 'red',width = 2)

def creer_croix ():
    points = [300, 200, 400, 200, 300, 400, 400,
    400]
    canvas1.create_polygon(points, outline='yellow',
    fill='yellow', width=2)
    canvas1.create_line (150,200,200,400,)
    return

def undo () :
    canvas1.delete (canvas1.create_oval)
    canvas1.delete (canvas1.create_polygon)
    canvas1.delete (canvas1.create_polygon)
    return
    # Début de votre code

canvas1 = tk.Canvas(root, relief = tk.FLAT, background = "black")
canvas1.grid()
button_1 = tk.Button (root,text ="Choisir une couleur",fg="red",command= write_slogan())
button_1.grid ( row = 1 , sticky = N,column = 0)
button_2 = tk.Button (root,text ="Cercle",fg="blue", command= creer_disque ())
button_2.grid (row = 2, sticky = NE,column = 2,)
button_3 = tk.Button (root,text ="Carré",fg="red",command= creer_carre())
button_3.grid (row = 3,sticky = NE, column = 3)
button_4 = tk.Button (root,text ="Croix",fg="yellow",command= creer_croix ())
button_4.grid (row = 4,sticky = NE , column = 4)
button_5 = tk.Button (root,text = "undo")
button_5.grid (row= 2,sticky = N,column= 0)
    # Fin de votre code

root.mainloop()

