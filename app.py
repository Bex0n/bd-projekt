from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Set up window
win = Tk()
win.geometry("1200x800")
win.configure(bg="#2d3a51")
win.resizable(False, False)
win.title("Fin4nc3")

# Left and right panel
wrapperLeft = LabelFrame(win, height=770, width=540)
wrapperRight = LabelFrame(win, height=770, width=540)
wrapperLeft.pack(side=LEFT, fill="both", expand="no", padx=15, pady=15)
wrapperRight.pack(fill="both", expand="yes", padx=15, pady=15)
wrapperRight.configure(bg="#2d3a51")


# Left panel - upper and lower panel
wrapperStocks = LabelFrame(wrapperLeft, height=335)
wrapperHistory = LabelFrame(wrapperLeft, height=335)
wrapperStocks.pack(side=TOP, fill="both", expand="yes")
wrapperHistory.pack(side=BOTTOM, fill="both", expand="yes")
wrapperStocks.configure(bg='lightsteelblue')
wrapperHistory.configure(bg='lightsteelblue')

# Right panel - upper and lower panel

wrapperCompany = LabelFrame(wrapperRight, height=75, borderwidth=0, highlightthickness=0)
wrapperData = LabelFrame(wrapperRight, height=450)
wrapperAddStock = LabelFrame(wrapperRight, height=250, borderwidth=0, highlightthickness=0)
wrapperCompany.pack(side=TOP, fill="x", expand="yes")
wrapperData.pack(fill="both", expand="yes")
wrapperAddStock.pack(side=BOTTOM, fill="both", expand="yes")
wrapperCompany.configure(bg='lightsteelblue')
wrapperData.configure(bg='lightsteelblue')
wrapperAddStock.configure(bg='lightsteelblue')

# Left panel - stocks and history scrollable lists
canvasStocks = Canvas(wrapperStocks, height=335)
canvasHistory = Canvas(wrapperHistory, height=335)
canvasStocks.pack(side=LEFT, fill="both", expand="yes")
canvasHistory.pack(side=LEFT, fill="both", expand="yes")
stocksScrollbar = ttk.Scrollbar(wrapperStocks, orient="vertical", command=canvasStocks.yview)
historyScrollbar = ttk.Scrollbar(wrapperHistory, orient="vertical", command=canvasHistory.yview)
stocksScrollbar.pack(side=RIGHT, fill="y")
historyScrollbar.pack(side=RIGHT, fill="y")
canvasStocks.configure(yscrollcommand=stocksScrollbar.set)
canvasHistory.configure(yscrollcommand=historyScrollbar.set)
canvasStocks.configure(bg="#adb9d1")
canvasHistory.configure(bg="#adb9d1")
canvasStocks.bind('<Configure>', lambda e: canvasStocks.configure(scrollregion = canvasStocks.bbox('all')))
canvasHistory.bind('<Configure>', lambda e: canvasHistory.configure(scrollregion = canvasHistory.bbox('all')))
frameStocks = Frame(canvasStocks)
frameHistory = Frame(canvasHistory)
canvasStocks.create_window((0, 0), window=frameStocks, anchor="nw")
canvasHistory.create_window((0, 0), window=frameHistory, anchor="nw")

# Right panel - choose company box and update button

choices = [' - ', 'NVIDIA', 'Tesla', 'SpaceX', 'Amazon']
variable = StringVar(wrapperCompany)
variable.set(' - ')
choosebox = ttk.Combobox(wrapperCompany, values = choices)
choosebox.current(0)
choosebox.pack(side=LEFT, fill="both", expand="yes", padx=10, pady=15)
updatebutton = Button(wrapperCompany, text="Update", fg = "white", font = "Kokila", bg="#5b74a3")
updatebutton.pack(side=TOP, fill="both", expand="yes", padx=100, pady=10)

# Adding test buttons
def show_msg():
    messagebox.showinfo("Eror", "Pomocy, zostalem uwieziony")
for i in range(50):
    Button(frameStocks, text="Przycisk " + str(i) + " ", fg = "white", font = "Kokila", bg="#5b74a3", command=show_msg).pack(side=TOP, fill="x")
    Button(frameHistory, text="Test " + str(i) + " ", fg = "white", font = "Kokila", bg="#5b74a3", command=show_msg).pack(side=TOP, fill="x")

# Run program

win.mainloop()