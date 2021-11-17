import tkinter as tk
    

def write_slogan():
    print("Trump is great!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
canvas1 = tk.Canvas(root, relief = tk.FLAT, background = "blue")
canvas1.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Trump",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()
