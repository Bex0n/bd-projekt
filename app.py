from tkinter import *
from tkinter import messagebox
from tkinter import ttk

win = Tk()

wrapper1 = LabelFrame(win)
wrapper2 = LabelFrame(win)

mycanvas = Canvas(wrapper1)
mycanvas.pack(side=LEFT, fill="both", expand="yes")

yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=mycanvas.yview )
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.configure(bg="#adb9d1")

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

myframe = Frame(mycanvas)
mycanvas.create_window((0, 0), window=myframe, anchor="nw")

wrapper1.pack(fill="both", expand="yes", padx=30, pady=15)
wrapper2.pack(fill="both", expand="yes", padx=30, pady=15)
wrapper2.configure(bg='lightsteelblue')

def show_msg():
    messagebox.showinfo("Eror", "Hej, tak Ty")

for i in range(50):
    Button(myframe, text="Przycisk " + str(i) + " ", fg = "white", font = "Kokila", bg="#5b74a3", command=show_msg).pack(side=TOP, fill="x")

win.geometry("800x900")
win.configure(bg="#2d3a51")
win.resizable(False, False)
win.title("Fin4nc3")
win.mainloop()