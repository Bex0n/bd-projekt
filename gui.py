from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from mysql import *

# Message function
def show_msg():
    messagebox.showinfo("Eror", "Pomocy, zostalem uwieziony")

class GUITemplate(object):

    def __init_left_panel_scrollbars(self):
        self.canvasStocks = Canvas(self.wrapperStocks, height=335)
        self.canvasHistory = Canvas(self.wrapperHistory, height=335)
        self.canvasStocks.pack(side=LEFT, fill="both", expand="yes")
        self.canvasHistory.pack(side=LEFT, fill="both", expand="yes")
        self.stocksScrollbar = ttk.Scrollbar(self.wrapperStocks, orient="vertical", command=self.canvasStocks.yview)
        self.historyScrollbar = ttk.Scrollbar(self.wrapperHistory, orient="vertical", command=self.canvasHistory.yview)
        self.stocksScrollbar.pack(side=RIGHT, fill="y")
        self.historyScrollbar.pack(side=RIGHT, fill="y")
        self.canvasStocks.configure(yscrollcommand=self.stocksScrollbar.set)
        self.canvasHistory.configure(yscrollcommand=self.historyScrollbar.set)
        self.canvasStocks.configure(bg="#adb9d1")
        self.canvasHistory.configure(bg="#adb9d1")
        self.canvasStocks.bind('<Configure>', lambda e: self.canvasStocks.configure(scrollregion = self.canvasStocks.bbox('all')))
        self.canvasHistory.bind('<Configure>', lambda e: self.canvasHistory.configure(scrollregion = self.canvasHistory.bbox('all')))
        self.frameStocks = Frame(self.canvasStocks, bg="#adb9d1")
        self.frameHistory = Frame(self.canvasHistory, bg="#adb9d1")
        self.canvasStocks.create_window((0, 0), window=self.frameStocks, anchor="nw")
        self.canvasHistory.create_window((0, 0), window=self.frameHistory, anchor="nw")

    def __init_right_panel_company_choose__(self):
        self.choices = [' - ', 'NVIDIA', 'Tesla', 'SpaceX', 'Amazon']
        self.variable = StringVar(self.wrapperCompany)
        self.variable.set(' - ')
        self.choosebox = ttk.Combobox(self.wrapperCompany, values = self.choices)
        self.choosebox.current(0)
        self.choosebox.pack(side=LEFT, fill="x", expand="yes", padx=10, pady=0)
        self.updatebutton = Button(self.wrapperCompany, text="Update", fg = "white", font = "Kokila", bg="#5b74a3", command=show_msg)
        self.updatebutton.pack(side=TOP, fill="x", expand="yes", padx=100, pady=0)

    def __init_left_panel__(self):
        self.wrapperStocks = LabelFrame(self.wrapperLeft, height=335)
        self.wrapperHistory = LabelFrame(self.wrapperLeft, height=335)
        self.wrapperStocks.pack(side=TOP, fill="both", expand="yes")
        self.wrapperHistory.pack(side=BOTTOM, fill="both", expand="yes")
        self.wrapperStocks.configure(bg='lightsteelblue')
        self.wrapperHistory.configure(bg='lightsteelblue')
        self.__init_left_panel_scrollbars()

    def __init_right_panel__(self):
        self.wrapperCompany = LabelFrame(self.wrapperRight, height=75, borderwidth=0, highlightthickness=0)
        self.wrapperData = LabelFrame(self.wrapperRight, height=450)
        self.wrapperAddStock = LabelFrame(self.wrapperRight, height=250, borderwidth=0, highlightthickness=0)
        self.wrapperCompany.pack(side=TOP, fill="both", expand="yes")
        self.wrapperData.pack(fill="both", expand="yes")
        self.wrapperAddStock.pack(side=BOTTOM, fill="both", expand="yes")
        self.wrapperCompany.configure(bg='lightsteelblue')
        self.wrapperData.configure(bg='lightsteelblue')
        self.wrapperAddStock.configure(bg='lightsteelblue')
        self.__init_right_panel_company_choose__()

    def __init_panels__(self):
        self.wrapperLeft = LabelFrame(self.win, height=770, width=540)
        self.wrapperRight = LabelFrame(self.win, height=770, width=540)
        self.wrapperLeft.pack(side=LEFT, fill="both", expand="no", padx=15, pady=15)
        self.wrapperRight.pack(fill="both", expand="yes", padx=15, pady=15)
        self.wrapperRight.configure(bg="#2d3a51")
        self.__init_left_panel__()
        self.__init_right_panel__()

    def __init_window__(self):
        self.win = Tk()
        self.win.geometry("1200x800")
        self.win.configure(bg="#2d3a51")
        self.win.resizable(False, False)
        self.win.title("Fin4nc3")
        self.__init_panels__()

    def __init__(self):
        self.__init_window__()

    def addButtons(self):
        # Adding buttons
        for i in range(12):
            btn = Button(self.frameStocks, text="Przycisk " + str(i) + " ", fg = "white", font = "Kokila", bg="#5b74a3")
            btn['command'] = (lambda b=btn: b.destroy())
            btn.pack(side=TOP, fill='x')
            Button(self.frameHistory, text="Test " + str(i) + " ", fg = "white", font = "Kokila", bg="#5b74a3", command=show_msg).pack(side=TOP, fill="x")

    def clearHistory(self):
        for button in self.frameHistory.winfo_children():
            button.destroy()
        