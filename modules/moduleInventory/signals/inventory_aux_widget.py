from PySide6.QtCore import QObject,Signal

class InventoryAuxWidget(QObject):
    reloadInventory = Signal()