import tkinter
if __name__ == '__main__':
    t = tkinter.Tk()
    canvas = tkinter.Canvas(width=800, height=600, bg='black')  
    canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)                
    k = 1
    j = 1
    for i in range(0,26):
        canvas.create_oval(310 - k,250 - k,310 + k,250 + k, width=1,outline="red")
        k += j
        j += 0.3

    t.mainloop ()