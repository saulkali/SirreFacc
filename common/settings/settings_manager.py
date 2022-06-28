#settings
from common.settings.printer import Printer
from common.settings.socket import Socket
from common.settings.system import System

#helper
from helper import getFile, singleton

#pickle
import pickle

@singleton
class SettingsManager(object):
    socket:Socket = Socket()
    printer:Printer = Printer()
    system:System = System()

    def __init__(self) -> None:
        self.__read_files_pickles()

    def __read_files_pickles(self):
        try:
            socket = open(getFile("socket"),"rb")
            self.socket = pickle.load(socket)
            print("settings socket loaded")
        except:
            print("settings socket not found")
        
        try:
            printer = open(getFile("printer"),"rb")
            self.printer = pickle.load(printer)
            print("settings printer loaded")
        except:
            print("settings printer not found")
        
    def save(self):
        with open(getFile("socket"),"wb") as socket_pickle_in:
            pickle.dump(self.socket,socket_pickle_in)
            print("save socket settings")
        
        with open(getFile("printer"),"wb") as printer_pickle_in:
            pickle.dump(self.printer,printer_pickle_in)
            print("save settings printer")
        
        print("save all settings success")
    