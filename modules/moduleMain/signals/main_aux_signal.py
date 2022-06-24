from PySide6.QtCore import QObject,Signal

class MainAuxSignal(QObject):
    deleteItemShoppingCar = Signal(object)
    refreshTotal = Signal()