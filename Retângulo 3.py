from tkinter import Canvas, mainloop, Tk

master = Tk()

w = Canvas(master, width=600, height=600) #1

w.create_rectangle(30, 25, 130, 75, fill="blue")  #2
w.create_rectangle(250, 25, 150, 75, fill= "CYAN")
w.create_rectangle(375, 25, 275, 75, fill = "GREEN")
w.create_rectangle(500, 25, 400, 75, fill = "RED")
w.create_rectangle(30, 100, 130, 150, fill = "GRAY")
w.create_rectangle(150, 100, 250, 150, fill = "MAGENTA")
w.create_rectangle(275, 100, 375, 150, fill = "PINK")
w.create_rectangle(400, 100, 500, 150, fill = "YELLOW")
w.pack()         #3
mainloop()