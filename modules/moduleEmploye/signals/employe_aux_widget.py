from PySide6.QtCore import QObject,Signal

class EmployeAuxWidget(QObject):
    reloadListEmployes = Signal()