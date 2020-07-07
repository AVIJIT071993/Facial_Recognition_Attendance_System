"""
author = AVIJIT BANDURI
copyright = Copyright (c) 2020, AVIJIT BANDURI
license = BSD 3-Clause License
version = 1.0
"""

from pandastable import Table
import tkinter as Tk
from tkinter.ttk import *
from tkinter import *

def Employee():
    filename = "EmployeeDetails\EmployeeDetails.csv"
    root3 = Tk()
    root3.title("Employee Table")
    frame = Frame(root3)
    frame.pack()
    pt = Table(frame)
    pt.importCSV(filename)
    pt.show()
    root3.mainloop()