from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from mysql import stockDatabase
import mysql

# Message function
def show_msg():
    messagebox.showinfo("Eror", "Pomocy, zostalem uwieziony")

def callback(eventObject):
    print("Selected")

def sell(self, ownedstock):
        self.createHistoryStock(ownedstock)
        ownedstock.forget()
        self.clearStocks()
        self.wrapperStocks.forget()
        self.wrapperHistory.forget()
        self.__init_left_panel__()
        self.addOwnedStocks()
        self.addHistoryStocks()

class GUITemplate(object):

    def updateVisualData(self):
        self.companyName.configure(text=self.choosebox.get())
        self.companyUpdateDate.configure(text="Last update: " + self.database.getLastDate(self.choosebox.get()))
        self.minPriceValue.configure(text=self.database.getMin(self.choosebox.get()))
        self.maxPriceValue.configure(text=self.database.getMax(self.choosebox.get()))
        self.avgPriceValue.configure(text=self.database.getAvg(self.choosebox.get()))
        self.medianPriceValue.configure(text=self.database.getMedian(self.choosebox.get()))
        self.volume.configure(text=self.database.getVolume(self.choosebox.get()))
        self.dailyVolume.configure(text=self.database.getDailyVolume(self.choosebox.get()))
        self.lowestDailyVolume.configure(text=self.database.getLowestVolume(self.choosebox.get()))
        self.highestDailyVolume.configure(text=self.database.getHighestVolume(self.choosebox.get()))
        self.clearStocks()
        self.wrapperStocks.forget()
        self.wrapperHistory.forget()
        self.__init_left_panel__()
        self.addOwnedStocks()
        self.addHistoryStocks()
        

    def updateData(self):
        self.database.updateLastMonth(self.choosebox.get())
        self.updateVisualData()

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
        self.choices = [' - ', 'NVIDIA', 'Tesla', 'Amazon']
        self.variable = StringVar(self.wrapperCompany)
        self.variable.set(' - ')
        self.choosebox = ttk.Combobox(self.wrapperCompany, values = self.choices)
        self.choosebox.bind("<<ComboboxSelected>>", lambda eventObject : self.updateVisualData())
        self.choosebox.current(0)
        self.heightenator = Label(self.wrapperCompany, bg='lightsteelblue', height=3)
        self.heightenator.pack(side=LEFT)
        self.choosebox.pack(side=LEFT, fill="x", expand="yes", padx=10, pady=0)
        self.updatebutton = Button(self.wrapperCompany, text="UPDATE", fg = "white", font=("Helvetica 18 bold", 15), bg="#5b74a3", command=self.updateData)
        self.updatebutton.pack(side=TOP, fill="x", expand="yes", padx=100, pady=0)

    def __init_right_panel_data_panel__(self):
        self.companyName = Label(self.wrapperData, text="-", font=("Roboto", 50), bg='white')
        self.companyName.pack(anchor=N, fill='x')
        self.companyLast = LabelFrame(self. wrapperData, bg='lightsteelblue', height=1)
        self.companyLast.pack(anchor=N, fill='both')
        self.companyData = LabelFrame(self.wrapperData, bg='lightsteelblue', height=50, borderwidth=0, highlightthickness=0)
        self.companyData.pack(anchor=N, fill='both', expand='yes')
        self.leftCompanyData = LabelFrame(self.companyData, bg='white')
        self.rightCompanyData = LabelFrame(self.companyData, bg='red')
        self.leftCompanyData.pack(side=LEFT, fill='both')
        self.rightCompanyData.pack(fill='both', expand='yes')

        self.companyUpdateDate = Label(self.companyLast, text="-", bg='white', height=2)
        self.companyUpdateDate.pack(side=LEFT, fill='both', expand="yes")
        # self.companyLastChoosebox = Label(self.companyLast, text="-", bg="white")
        # self.companyLastChoosebox.pack(side=LEFT, fill="both", expand="yes")

        self.minPriceText = Label(self.leftCompanyData, anchor = W)
        self.minPriceText.pack(anchor=NW, fill='x')
        Label(self.minPriceText, text='Minimum price:', font=("TkDefaultFont", 14), anchor=W, width=29).pack()
        self.maxPriceText = Label(self.leftCompanyData)
        self.maxPriceText.pack(anchor=NW, fill='x')
        Label(self.maxPriceText, text='Maximum price:', font=("TkDefaultFont", 14), anchor=W, width=29).pack()
        self.avgPriceText = Label(self.leftCompanyData)
        self.avgPriceText.pack(anchor=NW, fill='x')
        Label(self.avgPriceText, text='Average price:', font=("TkDefaultFont", 14), anchor=W, width=29).pack()
        self.medianPriceText = Label(self.leftCompanyData)
        self.medianPriceText.pack(anchor=NW, fill='x')
        Label(self.medianPriceText, text='Median price:', font=("TkDefaultFont", 14), anchor=W, width=29).pack()
        self.volumeText = Label(self.leftCompanyData)
        self.volumeText.pack(anchor=NW, fill='x')
        Label(self.volumeText, text='Volume:', font=("TkDefaultFont", 14), anchor=W, width=29).pack()
        self.dailyVolumeText = Label(self.leftCompanyData)
        self.dailyVolumeText.pack(anchor=NW, fill='x')
        Label(self.dailyVolumeText, text='Average daily volume:', font=("TkDefaultFont", 14), anchor=W, width=29).pack()
        self.lowestDailyVolumeText = Label(self.leftCompanyData)
        self.lowestDailyVolumeText.pack(anchor=NW, fill='x')
        Label(self.lowestDailyVolumeText, text='Lowest daily Volume:', font=("TkDefaultFont", 14), anchor=W, width=29).pack()
        self.highestDailyVolumeText = Label(self.leftCompanyData)
        self.highestDailyVolumeText.pack(anchor=NW, fill='x')
        Label(self.highestDailyVolumeText, text='Highest daily Volume:', font=("TkDefaultFont", 14), anchor=W, width=29).pack()

        self.minPrice = Label(self.rightCompanyData, anchor = W, width=40)
        self.minPrice.pack(anchor=NW, fill='x')
        self.minPriceValue = Label(self.minPrice, text='-', font=("TkDefaultFont", 14))
        self.minPriceValue.pack()
        self.maxPrice = Label(self.rightCompanyData, anchor = W, width=40)
        self.maxPrice.pack(anchor=NW, fill='x')
        self.maxPriceValue = Label(self.maxPrice, text='-', font=("TkDefaultFont", 14))
        self.maxPriceValue.pack()
        self.avgPrice = Label(self.rightCompanyData, anchor = W, width=40)
        self.avgPrice.pack(anchor=NW, fill='x')
        self.avgPriceValue = Label(self.avgPrice, text='-', font=("TkDefaultFont", 14))
        self.avgPriceValue.pack()
        self.medianPrice = Label(self.rightCompanyData, anchor = W, width=40)
        self.medianPrice.pack(anchor=NW, fill='x')
        self.medianPriceValue = Label(self.medianPrice, text='-', font=("TkDefaultFont", 14))
        self.medianPriceValue.pack()
        self.volume = Label(self.rightCompanyData, anchor = W, width=40)
        self.volume.pack(anchor=NW, fill='x')
        self.volume = Label(self.volume, text='-', font=("TkDefaultFont", 14))
        self.volume.pack()
        self.dailyVolume = Label(self.rightCompanyData, anchor = W, width=40)
        self.dailyVolume.pack(anchor=NW, fill='x')
        self.dailyVolume = Label(self.dailyVolume, text='-', font=("TkDefaultFont", 14))
        self.dailyVolume.pack()
        self.lowestDailyVolume = Label(self.rightCompanyData, anchor = W, width=40)
        self.lowestDailyVolume.pack(anchor=NW, fill='x')
        self.lowestDailyVolume = Label(self.lowestDailyVolume, text='-', font=("TkDefaultFont", 14))
        self.lowestDailyVolume.pack()
        self.highestDailyVolume = Label(self.rightCompanyData, anchor = W, width=40)
        self.highestDailyVolume.pack(anchor=NW, fill='x')
        self.highestDailyVolume = Label(self.highestDailyVolume, text='-', font=("TkDefaultFont", 14))
        self.highestDailyVolume.pack()

    def __init_right_panel_add_stock(self):
        self.addStock = Label(self.wrapperAddStock, anchor=W, bg='white', width=40)
        self.addStock.pack(fill='both', expand='yes')

    def __init_left_panel__(self):
        self.wrapperStocks = LabelFrame(self.wrapperLeft, height=335)
        self.wrapperHistory = LabelFrame(self.wrapperLeft, height=335)
        self.wrapperStocks.pack(side=TOP, fill="both", expand="yes")
        self.wrapperHistory.pack(side=BOTTOM, fill="both", expand="yes")
        self.wrapperStocks.configure(bg='lightsteelblue')
        self.wrapperHistory.configure(bg='lightsteelblue')
        self.__init_left_panel_scrollbars()

    def __init_right_panel__(self):
        self.wrapperCompany = LabelFrame(self.wrapperRight, height=125, borderwidth=0, highlightthickness=0)
        self.wrapperData = LabelFrame(self.wrapperRight, height=450)
        self.wrapperAddStock = LabelFrame(self.wrapperRight, borderwidth=0, highlightthickness=0)
        self.wrapperCompany.pack(anchor=N, side=TOP, fill="both", expand="no")
        self.wrapperData.pack(anchor=N, fill="both", expand="yes")
        self.wrapperAddStock.pack(anchor=N, fill="both", expand="yes")
        self.wrapperCompany.configure(bg='lightsteelblue')
        self.wrapperData.configure(bg='lightsteelblue')
        self.wrapperAddStock.configure(bg='lightsteelblue')
        self.__init_right_panel_data_panel__()
        self.__init_right_panel_company_choose__()
        self.__init_right_panel_add_stock()

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
        self.database = stockDatabase()
        self.database.connect()
        self.__init_window__()

    def clearStocks(self):
        for button in self.frameHistory.winfo_children():
            button.destroy()
        for button in self.frameStocks.winfo_children():
            button.destroy()

    def createHistoryStock(sekf, ownedstock):
        pass

    def createOwnedStockLabel(self):
        label = Label(self.frameStocks, bg="#5b74a3", text='Test')
        labelleft = Label(label, bg='white', height=7)
        labelright = Label(label, bg='white', height=7)
        label.pack(side=TOP, fill='x', expand='yes')
        labelleft.pack(side=LEFT)
        labelright.pack(side=LEFT)

        earnings = Label(labelright, bg='green', text='+1.23$', font=('Kokilla', 16))
        roe = Label(labelright, bg='blue', text='+25.6%', width=23, height=1)
        finish = Button(labelright, text="Sell", fg='white', font='Kokilla', command=lambda e: sell(self, label))
        earnings.pack()
        roe.pack()
        finish.pack()

        date = Label(labelleft, bg='red', anchor=W, text='Start date: 2023-01-23', width=23)
        initialvalue = Label(labelleft, anchor=W, bg='yellow', text='Value: 15$')
        volume = Label(labelleft, anchor=W, bg='red', text='Volumes: 15')
        volumeprice = Label(labelleft, anchor=W, bg='blue', text='Price per volume: 1$')
        date.pack(anchor=W)
        initialvalue.pack(anchor=W)
        volume.pack(anchor=W)
        volumeprice.pack(anchor=W)

    def addOwnedStocks(self):
        for i in range(5):
            self.createOwnedStockLabel()

    def addHistoryStocks(self):
        for i in range(5):
            btn = Button(self.frameHistory, text="Test " + str(i) + " ", fg = "white", font = "Kokila", bg="#5b74a3", command=show_msg)
            btn['command'] = show_msg
            btn.pack(side=TOP, fill="x")