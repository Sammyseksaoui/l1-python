import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

    # Début de votre code
x0 = 300
x1 = 300
y = CANVAS_HEIGHT / 2
y1 = 500
canvas.create_line(x0, y, x1, y1)
canvas.create_oval(x0 - 150, y + 150, x0 + 150, y1 - 150)
canvas.create_oval(x0 - 150, y + 150, x0 + 150, y1 - 150)
canvas.create_oval((2*x0) / 2 - 150, y , (2*x0) / 2 + 150, y1 - 150)

    # Fin de votre code

canvas.grid ()
root.mainloop()

