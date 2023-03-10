from tkinter import *
from tkinter import ttk
from mysql import stockDatabase
from nameconverter import companies

def callback(eventObject):
    print("Selected")

class GUITemplate(object):

    def createOwnedStock(self):
        self.database.addOwnedStock(self.choosebox.get(), self.addStockDateEntryString.get(), self.addStockPriceEntryString.get(), self.addStockVolumeEntry.get())
        self.updateVisualData()

    def updateVisualData(self):
        self.companyName.configure(text=self.choosebox.get())
        self.companyUpdateDate.configure(text="Last update: " + self.database.getLastDate(self.choosebox.get()))
        self.todayPriceValue.configure(text=self.database.getLastPrice(self.choosebox.get()))
        if (self.database.getLastPrice(self.choosebox.get()) == 0):
            self.todayPriceValue.configure(text='-')
        self.minPriceValue.configure(text=self.database.getMin(self.choosebox.get()))
        self.maxPriceValue.configure(text=self.database.getMax(self.choosebox.get()))
        self.avgPriceValue.configure(text=self.database.getAvg(self.choosebox.get()))
        self.medianPriceValue.configure(text=self.database.getMedian(self.choosebox.get()))
        self.volume.configure(text=self.database.getVolume(self.choosebox.get()))
        self.dailyVolume.configure(text=self.database.getDailyVolume(self.choosebox.get()))
        self.lowestDailyVolume.configure(text=self.database.getLowestVolume(self.choosebox.get()))
        self.highestDailyVolume.configure(text=self.database.getHighestVolume(self.choosebox.get()))

        self.addStockDateEntryString.set(self.database.getLastDate(self.choosebox.get()))
        self.addStockPriceEntryString.set(self.database.getLastPrice(self.choosebox.get()))

        self.clearStocks()
        self.stocksInfo.forget()
        self.wrapperStocks.forget()
        self.historyInfo.forget()
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
        self.canvasStocks.configure(bg="#828195")
        self.canvasHistory.configure(bg="#828195")
        self.canvasStocks.bind('<Configure>', lambda e: self.canvasStocks.configure(scrollregion = self.canvasStocks.bbox('all')))
        self.canvasHistory.bind('<Configure>', lambda e: self.canvasHistory.configure(scrollregion = self.canvasHistory.bbox('all')))
        self.frameStocks = Frame(self.canvasStocks, bg="#adb9d1")
        self.frameHistory = Frame(self.canvasHistory, bg="#adb9d1")
        self.canvasStocks.create_window((0, 0), window=self.frameStocks, anchor="nw")
        self.canvasHistory.create_window((0, 0), window=self.frameHistory, anchor="nw")

    def __init_right_panel_company_choose__(self):
        self.choices = companies
        self.variable = StringVar(self.wrapperCompany)
        self.variable.set(' - ')
        self.choosebox = ttk.Combobox(self.wrapperCompany, values = self.choices)
        self.choosebox.bind("<<ComboboxSelected>>", lambda eventObject : self.updateVisualData())
        self.choosebox.current(0)
        self.heightenator = Label(self.wrapperCompany, bg='#828195', height=3)
        self.heightenator.pack(side=LEFT)
        self.choosebox.pack(side=LEFT, fill="x", expand="yes", padx=10, pady=0)
        self.updatebutton = Button(self.wrapperCompany, text='Update', font=("default", 15, 'bold'), command=self.updateData)
        self.updatebutton.pack(side=TOP, fill="x", expand="yes", padx=100, pady=0)

    def __init_right_panel_data_panel__(self):
        self.companyName = Label(self.wrapperData, text="-", font=("Roboto", 50), bg='white')
        self.companyName.pack(anchor=N, fill='x')
        self.companyLast = LabelFrame(self. wrapperData, bg='#C7C7D2', height=1)
        self.companyLast.pack(anchor=N, fill='both')
        self.companyData = LabelFrame(self.wrapperData, bg='#C7C7D2', height=50, borderwidth=0, highlightthickness=0)
        self.companyData.pack(anchor=N, fill='both', expand='yes')
        self.leftCompanyData = LabelFrame(self.companyData, bg='#C7C7D2')
        self.rightCompanyData = LabelFrame(self.companyData, bg='#C7C7D2')
        self.leftCompanyData.pack(side=LEFT, fill='both')
        self.rightCompanyData.pack(fill='both', expand='yes')

        self.companyUpdateDate = Label(self.companyLast, text="-", bg='#C7C7D2', height=2)
        self.companyUpdateDate.pack(side=LEFT, fill='both', expand="yes")

        self.todayPriceText = Label(self.leftCompanyData, anchor = W, borderwidth=0, highlightthickness=0)
        self.todayPriceText.pack(anchor=NW, fill='x')
        Label(self.todayPriceText, text='Today price:', font=("TkDefaultFont", 18), anchor=W, width=24, bg='#C7C7D2', fg='black', borderwidth=0, highlightthickness=0).pack()
        self.minPriceText = Label(self.leftCompanyData, borderwidth=0, highlightthickness=0)
        self.minPriceText.pack(anchor=NW, fill='x')
        Label(self.minPriceText, text='Minimum price:', font=("TkDefaultFont", 18), anchor=W, width=24, bg='#C7C7D2', fg='black', borderwidth=0, highlightthickness=0).pack()
        self.maxPriceText = Label(self.leftCompanyData, borderwidth=0, highlightthickness=0)
        self.maxPriceText.pack(anchor=NW, fill='x')
        Label(self.maxPriceText, text='Maximum price:', font=("TkDefaultFont", 18), anchor=W, width=24, bg='#C7C7D2', fg='black', borderwidth=0, highlightthickness=0).pack()
        self.avgPriceText = Label(self.leftCompanyData, borderwidth=0, highlightthickness=0)
        self.avgPriceText.pack(anchor=NW, fill='x')
        Label(self.avgPriceText, text='Average price:', font=("TkDefaultFont", 18), anchor=W, width=24, bg='#C7C7D2', fg='black', borderwidth=0, highlightthickness=0).pack()
        self.medianPriceText = Label(self.leftCompanyData, borderwidth=0, highlightthickness=0)
        self.medianPriceText.pack(anchor=NW, fill='x')
        Label(self.medianPriceText, text='Median price:', font=("TkDefaultFont", 18), anchor=W, width=24, bg='#C7C7D2', fg='black', borderwidth=0, highlightthickness=0).pack()
        self.volumeText = Label(self.leftCompanyData, borderwidth=0, highlightthickness=0)
        self.volumeText.pack(anchor=NW, fill='x')
        Label(self.volumeText, text='Volume:', font=("TkDefaultFont", 18), anchor=W, width=24, bg='#C7C7D2', fg='black', borderwidth=0, highlightthickness=0).pack()
        self.dailyVolumeText = Label(self.leftCompanyData, borderwidth=0, highlightthickness=0)
        self.dailyVolumeText.pack(anchor=NW, fill='x')
        Label(self.dailyVolumeText, text='Average daily volume:', font=("TkDefaultFont", 18), anchor=W, width=24, bg='#C7C7D2', fg='black', borderwidth=0, highlightthickness=0).pack()
        self.lowestDailyVolumeText = Label(self.leftCompanyData, borderwidth=0, highlightthickness=0)
        self.lowestDailyVolumeText.pack(anchor=NW, fill='x')
        Label(self.lowestDailyVolumeText, text='Lowest daily Volume:', font=("TkDefaultFont", 18), anchor=W, width=24, bg='#C7C7D2', fg='black', borderwidth=0, highlightthickness=0).pack()
        self.highestDailyVolumeText = Label(self.leftCompanyData, borderwidth=0, highlightthickness=0)
        self.highestDailyVolumeText.pack(anchor=NW, fill='x')
        Label(self.highestDailyVolumeText, text='Highest daily Volume:', font=("TkDefaultFont", 18), anchor=W, width=24, bg='#C7C7D2', fg='black', borderwidth=0, highlightthickness=0).pack()

        self.todayPrice = Label(self.rightCompanyData, anchor = W, width=40, bg='#C7C7D2')
        self.todayPrice.pack(anchor=NW, fill='x')
        self.todayPriceValue = Label(self.todayPrice, text='-', font=("TkDefaultFont", 14), bg='#C7C7D2', fg='black')
        self.todayPriceValue.pack()
        self.minPrice = Label(self.rightCompanyData, anchor = W, width=40, bg='#C7C7D2')
        self.minPrice.pack(anchor=NW, fill='x')
        self.minPriceValue = Label(self.minPrice, text='-', font=("TkDefaultFont", 14), bg='#C7C7D2', fg='black')
        self.minPriceValue.pack()
        self.maxPrice = Label(self.rightCompanyData, anchor = W, width=40, bg='#C7C7D2')
        self.maxPrice.pack(anchor=NW, fill='x')
        self.maxPriceValue = Label(self.maxPrice, text='-', font=("TkDefaultFont", 14), bg='#C7C7D2', fg='black')
        self.maxPriceValue.pack()
        self.avgPrice = Label(self.rightCompanyData, anchor = W, width=40, bg='#C7C7D2')
        self.avgPrice.pack(anchor=NW, fill='x')
        self.avgPriceValue = Label(self.avgPrice, text='-', font=("TkDefaultFont", 14), bg='#C7C7D2', fg='black')
        self.avgPriceValue.pack()
        self.medianPrice = Label(self.rightCompanyData, anchor = W, width=40, bg='#C7C7D2')
        self.medianPrice.pack(anchor=NW, fill='x')
        self.medianPriceValue = Label(self.medianPrice, text='-', font=("TkDefaultFont", 14), bg='#C7C7D2', fg='black')
        self.medianPriceValue.pack()
        self.volume = Label(self.rightCompanyData, anchor = W, width=40, bg='#C7C7D2')
        self.volume.pack(anchor=NW, fill='x')
        self.volume = Label(self.volume, text='-', font=("TkDefaultFont", 14), bg='#C7C7D2', fg='black')
        self.volume.pack()
        self.dailyVolume = Label(self.rightCompanyData, anchor = W, width=40, bg='#C7C7D2')
        self.dailyVolume.pack(anchor=NW, fill='x')
        self.dailyVolume = Label(self.dailyVolume, text='-', font=("TkDefaultFont", 14), bg='#C7C7D2', fg='black')
        self.dailyVolume.pack()
        self.lowestDailyVolume = Label(self.rightCompanyData, anchor = W, width=40, bg='#C7C7D2')
        self.lowestDailyVolume.pack(anchor=NW, fill='x')
        self.lowestDailyVolume = Label(self.lowestDailyVolume, text='-', font=("TkDefaultFont", 14), bg='#C7C7D2', fg='black')
        self.lowestDailyVolume.pack()
        self.highestDailyVolume = Label(self.rightCompanyData, anchor = W, width=40, bg='#C7C7D2')
        self.highestDailyVolume.pack(anchor=NW, fill='x')
        self.highestDailyVolume = Label(self.highestDailyVolume, text='-', font=("TkDefaultFont", 14), bg='#C7C7D2', fg='black')
        self.highestDailyVolume.pack()

    def __init_right_panel_add_stock(self):
        self.addStock = Label(self.wrapperAddStock, anchor=W, bg='#828195', width=40)
        self.addStock.pack(fill='both', expand='yes')
        self.addStockLeft = Label(self.addStock, anchor=W, bg='#828195')
        self.addStockLeft.pack(side=LEFT, fill='both', expand='yes')
        self.addStockCenter = Label(self.addStock, anchor=W, bg='#828195')
        self.addStockCenter.pack(side=LEFT, fill='both', expand='yes')
        self.addStockRight = Label(self.addStock, anchor=W, bg='#828195')
        self.addStockRight.pack(side=LEFT, fill='both', expand='yes')
        # Add stock left panel
        self.addStockPrice = Label(self.addStockLeft, text='Price', fg='black', font=('Kokilla', 18, 'bold'), bg='#828195')
        self.addStockPrice.pack(anchor=W, expand='yes')
        self.addStockDate = Label(self.addStockLeft, text='Start date', fg='black', font=('Kokilla', 18, 'bold'), bg='#828195')
        self.addStockDate.pack(anchor=W, expand='yes')
        self.addStockVolume = Label(self.addStockLeft, text='Volumes', fg='black', font=('Kokilla', 18, 'bold'), bg='#828195')
        self.addStockVolume.pack(anchor=W, expand='yes')
        # Add stock center panel
        self.addStockPriceEntryString = StringVar()
        self.addStockPriceEntry = Entry(self.addStockCenter, font=('Kokilla', 18), textvariable=self.addStockPriceEntryString, width=15)
        self.addStockPriceEntry.pack(expand='yes')
        self.addStockDateEntryString = StringVar()
        self.addStockDateEntry = Entry(self.addStockCenter, font=('Kokilla', 18), textvariable=self.addStockDateEntryString, width=15)
        self.addStockDateEntry.pack(expand='yes')
        self.addStockVolumeEntry = Entry(self.addStockCenter, font=('Kokilla', 18), width=15)
        self.addStockVolumeEntry.pack(expand='yes')
        # Add stock right panel
        self.buyButton = Button(self.addStockRight, font=('Kokilla', 24, 'bold'), text="Confirm", command=self.createOwnedStock)
        self.buyButton.pack(side=LEFT, expand='yes')

    def __init_left_panel__(self):
        self.stocksInfo = Label(self.wrapperLeft, anchor=N, text="Owned stocks", height=1)
        self.wrapperStocks = LabelFrame(self.wrapperLeft, height=335)
        self.historyInfo = Label(self.wrapperLeft, anchor=N, text="History", height=1)
        self.wrapperHistory = LabelFrame(self.wrapperLeft, height=335)
        self.stocksInfo.pack()
        self.wrapperStocks.pack(side=TOP, fill="both", expand="yes")
        self.historyInfo.pack()
        self.wrapperHistory.pack(side=BOTTOM, fill="both", expand="yes")
        self.wrapperStocks.configure(bg='#828195')
        self.wrapperHistory.configure(bg='#828195')
        self.__init_left_panel_scrollbars()

    def __init_right_panel__(self):
        self.wrapperCompany = LabelFrame(self.wrapperRight, height=125, borderwidth=0, highlightthickness=0)
        self.wrapperData = LabelFrame(self.wrapperRight, height=450)
        self.wrapperAddStock = LabelFrame(self.wrapperRight, borderwidth=0, highlightthickness=0)
        self.wrapperCompany.pack(anchor=N, side=TOP, fill="both", expand="no")
        self.wrapperData.pack(anchor=N, fill="both", expand="yes")
        self.wrapperAddStock.pack(anchor=N, fill="both", expand="yes")
        self.wrapperCompany.configure(bg='#828195')
        self.wrapperData.configure(bg='#828195')
        self.wrapperAddStock.configure(bg='#828195')
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
        self.win.configure(bg="#383B4D")
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

    def sell(self, ownedstock):
        self.createHistoryStock(ownedstock)
        ownedstock.forget()
        ownedstock.destroy()
        self.database.deleteOwnedStock(ownedstock.id)
        self.clearStocks()
        self.stocksInfo.forget()
        self.wrapperStocks.forget()
        self.historyInfo.forget()
        self.wrapperHistory.forget()
        self.__init_left_panel__()
        self.addOwnedStocks()
        self.addHistoryStocks()

    def deleteHistory(self, historystock):
        historystock.forget()
        historystock.destroy()
        self.database.deleteHistoryStock(historystock.id)
        self.clearStocks()
        self.stocksInfo.forget()
        self.wrapperStocks.forget()
        self.historyInfo.forget()
        self.wrapperHistory.forget()
        self.__init_left_panel__()
        self.addOwnedStocks()
        self.addHistoryStocks()    

    def createHistoryStock(sekf, ownedstock):
        pass

    def createOwnedStockLabel(self, data):
        label = Label(self.frameStocks, bg="#828195")
        label.id = data[0]
        label.labelleft = Label(label, bg='#C7C7D2', height=7)
        label.labelright = Label(label, bg='#C7C7D2', height=7)
        label.pack(side=TOP, fill='x', expand='yes')
        label.labelleft.pack(side=LEFT)
        label.labelright.pack(side=LEFT)

        earning = round((self.database.getLastPrice(self.choosebox.get()) - data[3]) * data[4], 2)
        roe = round(earning / (data[3] * data[4]) * 100, 2)
        if earning > 0:
            earning = "+" + "{:.2f}".format(earning)
            roe = "+" + "{:.1f}".format(roe)
        else:
            earning = "{:.2f}".format(earning)
            roe = "{:.1f}".format(roe)
        earning = earning + "$"
        roe = roe + "%"
        label.earnings = Label(label.labelright, bg='#C7C7D2', text=earning, font=('Kokilla', 16))
        label.roe = Label(label.labelright, bg='#C7C7D2', text=roe, width=23, height=1)
        label.finish = Button(label.labelright, text="Sell", font='Kokilla', command=lambda : self.sell(label))
        label.earnings.pack()
        label.roe.pack()
        label.finish.pack()

        label.date = Label(label.labelleft, bg='#C7C7D2', anchor=W, text='Start date: ' + str(data[2]), width=23)
        label.initialvalue = Label(label.labelleft, anchor=W, bg='#C7C7D2', text='Value: ' + "{:.2f}".format(data[3] * data[4]) + '$')
        label.volume = Label(label.labelleft, anchor=W, bg='#C7C7D2', text='Volumes: ' + str(data[4]))
        label.volumeprice = Label(label.labelleft, anchor=W, bg='#C7C7D2', text='Price per volume: ' + "{:.2f}".format(data[3]) + '$')
        label.date.pack(anchor=W)
        label.initialvalue.pack(anchor=W)
        label.volume.pack(anchor=W)
        label.volumeprice.pack(anchor=W)

    def addOwnedStocks(self):
        data = self.database.getOwnedStocks(self.choosebox.get())
        for i in range(0, len(data)):
            self.createOwnedStockLabel(data[i])

    def createHistoryStockLabel(self, data):
        label = Label(self.frameHistory, bg="#828195")
        label.id = data[0]
        label.labelleft = Label(label, bg='#C7C7D2', height=7)
        label.labelright = Label(label, bg='#C7C7D2', height=7)
        label.pack(side=TOP, fill='x', expand='yes')
        label.labelleft.pack(side=LEFT)
        label.labelright.pack(side=LEFT)

        earning = round((data[4] - data[3]) * data[5], 2)
        label.earnings = Label(label.labelright, bg='#C7C7D2', text="{:.2f}".format(earning) + "$", font=('Kokilla', 16), pady=1)
        if earning > 0:
            label.earnings.configure(fg='#005908')
        if earning < 0:
            label.earnings.configure(fg='#7E1600')
        label.earnings.pack()
        label.roe = Label(label.labelright, bg='#C7C7D2', width=23, height=1)
        label.roe.pack()
        label.finish = Button(label.labelright, text="Delete", font='Kokilla', command=lambda : self.deleteHistory(label))
        label.finish.pack()

        label.date = Label(label.labelleft, bg='#C7C7D2', anchor=W, text='Start date: ' + str(data[2]), width=23)
        label.initialprice = Label(label.labelleft, anchor=W, bg='#C7C7D2', text='Buying price: ' + "{:.2f}".format(data[3]) + '$')
        label.sellprice = Label(label.labelleft, anchor=W, bg='#C7C7D2', text='Selling price: ' + "{:.2f}".format(data[4]) + '$')
        label.volume = Label(label.labelleft, anchor=W, bg='#C7C7D2', text='Volumes: ' + str(data[5]))
        label.date.pack(anchor=W)
        label.initialprice.pack(anchor=W)
        label.sellprice.pack(anchor=W)
        label.volume.pack(anchor=W)

    def addHistoryStocks(self):
        data = self.database.getHistoryStocks(self.choosebox.get())
        for i in range(0, len(data)):
            self.createHistoryStockLabel(data[i])