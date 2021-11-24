import tkinter as tk
from tkinter.constants import N, NE

CANVAS_WIDTH, CANVAS_HEIGHT = 1200, 800

root = tk.Tk()
canvas1 = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)  
x0 = 300
x1 = 200
y = CANVAS_HEIGHT / 2
y1 = 500
canvas1.create_line(x0, y, x1, y1)
canvas1.create_oval(x0 - 50 , y - 50 , x1 + 50 , y1+ 50,outline="#fb0", fill="#fb0")
canvas1.create_rectangle(30, 10, 120, 80,
    outline="#fb0", fill="#fb0")