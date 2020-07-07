"""
author = AVIJIT BANDURI
copyright = Copyright (c) 2020, AVIJIT BANDURI
license = BSD 3-Clause License
version = 1.0
"""

import tkinter as Tk
import datetime
import time
from tkinter import *
from pandastable import Table


def attendance():
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    filename = "Attendance\Attendance_" + date + ".csv"
    root2 = Tk()
    root2.title("Attendance Table")
    frame = Frame(root2)
    frame.pack()
    pt = Table(frame)
    pt.importCSV(filename)
    pt.show()
    root2.mainloop()