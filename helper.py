from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QImage,QPixmap

import os 
import requests
import threading

def singleton(cls):
    instances = dict()
    def wrap(*args,**kargs):
        if cls in instances:
            return instances[cls]
        new_intance = cls(*args,**kargs)
        instances[cls] = new_intance
        return instances[cls]
    return wrap

def getFile(file):
    dirname = os.path.dirname(__file__)+"/"+file
    print("dirname: ",dirname)
    return dirname


def setImage(labelPhoto:QLabel,url:str):
    try:
        image = QImage()
        image.loadFromData(requests.get(url).content)

        pixmap = QPixmap(image)
        labelPhoto.setPixmap(pixmap)
    except Exception as error:
        print(error)
def loadImage(labelPhoto:QLabel,url:str):
    threadSetImage = threading.Thread(target = setImage,args = (labelPhoto,url))
    threadSetImage.start()