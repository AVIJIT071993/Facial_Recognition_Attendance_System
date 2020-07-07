"""
author = AVIJIT BANDURI
copyright = Copyright (c) 2020, AVIJIT BANDURI
license = BSD 3-Clause License
version = 1.0
"""

import cv2
import os
from PIL import Image
import numpy as np
from tkinter import messagebox

def Train_model():

    recognizer = cv2.face_LBPHFaceRecognizer.create()
    faces, Id = getImagesAndLabels("EmployeeImages")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageAndLabel\Recognizer.yml")
    messagebox.showinfo("Message", "Successfully Trained. Ready for Recognition!")


def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    Ids = []

    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        Ids.append(Id)

    return faces, Ids