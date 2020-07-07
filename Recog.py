"""
author = AVIJIT BANDURI
copyright = Copyright (c) 2020, AVIJIT BANDURI
license = BSD 3-Clause License
version = 1.0
"""

import os
import datetime
import time
import cv2
from csv import writer

def Recog():

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("TrainingImageAndLabel\Recognizer.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)

    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    font = cv2.FONT_HERSHEY_COMPLEX

    while True:
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        filename = "Attendance\Attendance_" + date + ".csv"

        if os.path.exists(filename) == False:
            with open(filename, 'w', newline='') as write_obj:
                csv_writer = writer(write_obj)
                csv_writer.writerow(['Id', 'Name', 'Time'])

        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3, minSize=(int(minW), int(minH)))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 225, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            name = ""

            if (conf < 65):

                with open("EmployeeDetails\EmployeeDetails.csv","r") as info:
                    for inf in info:
                        if str(inf.split(",")[0]) == str(Id):
                            name = inf.split(",")[1]

                cv2.putText(frame, str(name), (x - 50, y - 20), font, 1, (0, 255, 255), 2)

                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                attendance = [Id, name, timeStamp]

                if os.path.exists(filename) == True:
                    with open(filename, "r") as rows:
                        rows.readline()
                        switch = 0

                        for row in rows:
                            if str((row.split(","))[0]) == str(attendance[0]):
                                switch = 1
                                break

                        if switch == 0:
                            with open(filename, 'a', newline='') as write_obj:
                                csv_writer = writer(write_obj)
                                csv_writer.writerow(attendance)

                with open(filename, "r") as rows:
                    rows.readline()
                    for row in rows:
                        if str((row.split(","))[0]) == str(attendance[0]):
                            disp = "Attendance Done"
                            cv2.putText(frame, str(disp), (x - 60, y + h + 35), font, 1, (0, 0, 255), 2)

            else:
                Id = "Unknown"

            if (conf > 70):
                cv2.putText(frame, str(Id), (x - 15, y +h + 35), font, 1, (255, 255, 255), 2)

        cv2.imshow('Recognition Window', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()


