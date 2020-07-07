"""
author = AVIJIT BANDURI
copyright = Copyright (c) 2020, AVIJIT BANDURI
license = BSD 3-Clause License
version = 1.0
"""

import tkinter as Tk
import datetime
from tkinter import messagebox
from tkinter import *
import cv2
import csv
import os
import Train_model


def add_user():
    root1 = Tk()
    root1.title("User Registration")
    Label(root1, text="Employee Name",font =('eras bold itc', 12)).grid(row=0, sticky=W)
    Label(root1, text="Employee ID", font =('eras bold itc', 12)).grid(row=1, sticky=W)
    Label(root1, text="Age", font=('eras bold itc', 12)).grid(row=2, sticky=W)
    Label(root1, text="Department", font=('eras bold itc', 12)).grid(row=3, sticky=W)
    Label(root1, text="Phone Number", font=('eras bold itc', 12)).grid(row=4, sticky=W)
    Fname = Entry(root1)
    Fname.grid(row=0, column=1)

    id = Entry(root1)
    id.grid(row=1, column=1)

    age = Entry(root1)
    age.grid(row=2, column=1)

    dept = Entry(root1)
    dept.grid(row=3, column=1)

    phone = Entry(root1)
    phone.grid(row=4, column=1)

    root1.grid_columnconfigure(1, minsize=150)
    root1.geometry("290x160")

    def getInput():
        global params1
        global params2
        global params3
        global params4
        global params5
        params1 = Fname.get()
        params2 = id.get()
        params3 = age.get()
        params4 = dept.get()
        params5 = phone.get()
        root1.destroy()

    Button(root1, text="Submit", font =('cooper black', 12), command=lambda: [getInput(), capture()]).grid(row=5, sticky=W)
    root1.mainloop()

def capture():
    from csv import writer
    Id=params2
    name=params1
    age=params3
    dept=params4
    phone=params5
    act = 0
    font = cv2.FONT_HERSHEY_COMPLEX

    empfile = "EmployeeDetails\EmployeeDetails.csv"

    if os.path.exists(empfile) == False:
        with open(empfile, 'w', newline='') as write_obj:
            csv_writer = writer(write_obj)
            csv_writer.writerow(['Id', 'Name', 'Age', 'Department','Phone Number', 'Date'])

    with open("EmployeeDetails/EmployeeDetails.csv", "r") as emps:
        for emp in emps:
            if emp.split(",")[0] == Id:
                act = 1
                messagebox.showinfo("Information", "User ID already exit. Enter a unique User ID")
            else:
                continue

    if Id.isnumeric() and act == 0:
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0

        while True:
            ret, frame = cam.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3, minSize=(1, 1))
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                sampleNum = sampleNum+1
                cv2.imwrite("EmployeeImages\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                cv2.putText(frame, str(sampleNum), (x - 50, y - 20), font, 1, (0, 255, 255), 2)
                cv2.imshow('Capturing Images', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                messagebox.showinfo("Message", "User Registered Successfully ")
                break

            elif sampleNum >= 150:
                messagebox.showinfo("Message", "User Registered Successfully ")
                break

        cam.release()
        cv2.destroyAllWindows()

        Date = datetime.datetime.now().strftime('%Y-%m-%d')
        row = [Id, name, age, dept, phone, Date]
        with open('EmployeeDetails\EmployeeDetails.csv', 'a', newline="") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)

        Train_model.Train_model()

    elif act == 1:
        pass

    else:
        messagebox.showerror("Error", "Wrong Input! Enter the correct values.")

