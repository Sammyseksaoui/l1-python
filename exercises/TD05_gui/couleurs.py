import tkinter as tk
from tkinter.constants import N, NE, E 
import random
def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)



CANVAS_WIDTH, CANVAS_HEIGHT = 256, 256

root = tk.Tk()
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT,background = "black") 
canvas.grid()
def draw_pixel (i,j,color) :
    canvas.create_rectangle (i,j,i,j,outline= color,fill= color)
    return
def ecran_aleatoire () :
    
    color_list = ["blue","black","red","yellow","cyan"]
    
    for i in range (0,256) :
        for j in range (0,256) :
            color = random.choice (color_list)
            draw_pixel (i,j,color)
    return 

def degrade_gris ():

    for i in range (0,86) :
        for j in range (0,86) :
            color = "black"
            draw_pixel (i,j,color)
            for i in range (86,128) :
                for j in range (86,128) :
                    color = (25,25,25)
                    draw_pixel (i,j,color)
                    for i in range (128,256) :
                        for j in range (128,256 ) :
                            color = "white"
                            draw_pixel (i,j,color)
    return
                            
def degrade_2D () :
    for i in range (0,86) :
        for j in range (0,86) :
            color = "blue"
            draw_pixel (i,j,color)
            for i in range (86,128) :
                for j in range (86,128) :
                    color = "purple"
                    draw_pixel (i,j,color)
                    for i in range (128,256) :
                        for j in range (128,256 ) :
                            color = "red"
                            draw_pixel (i,j,color)
    return

button_1 = tk.Button (root,text ="Aléatoire",fg="blue",command=ecran_aleatoire)
button_1.grid (row = 1 ,sticky = 'nw', column = 0)
button_2 = tk.Button (root,text ="Dégradé gris",fg="blue")
button_2.grid (row = 2,sticky = 'w', column =1 )
button_3 = tk.Button (root,text ="Dégradé 2D",fg="blue")
button_3.grid (row = 3,sticky = 'w', column = 3)
root.mainloop ()
