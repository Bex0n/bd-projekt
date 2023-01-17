from tkinter import *
from gui import *
from mysql import stockDatabase

app = GUITemplate()
app.addButtons()
app.win.mainloop()

# mydtbs = stockDatabase()
# mydtbs.connect()
# mydtbs.execute('select * from stocks')
# result = mydtbs.fetch()

# (x1, x2, x3, x4, x5, x6, x7) = result[0]

# print(x4)
     


