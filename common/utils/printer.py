#pyside 6
from PySide6.QtWidgets import QMessageBox

#escpos
from escpos.printer import File,Usb

#utilies
import os

#common
from common.utils.numeros import numero_to_letras
from common.settings.settings_manager import SettingsManager
from common.values import strings

#helper
from helper import singleton

#entities
from common.entities.sale_entity import SaleEntity

#tabulate
from tabulate import tabulate

CABEZERA = """
REFACCIONES PEQUENO DE S.A.YC.V.
   Felipe angeles 6761122447
 elpequenorefacciones@gmail.com
Cuauhtemoc, Cuencame, Dgo  35850\n\n
"""
@singleton
class PrinterEscPos():
    def __init__(self):
        super().__init__()
        self.DEV = SettingsManager().printer.dev

    def saveNewPortPrinter(self):
        '''metodo para guardar la nueva ruta del DEV'''
        settings = SettingsManager()
        settings.printer.dev = self.DEV
        settings.save()
    
    def scanPortPrinter(self):
        if SettingsManager().system.type == "Linux":
            port = '/dev/usb/lp'
            for n in range(0,30):
                try:
                    DEV = port+str(n)
                    printer = File(port + str(n))
                    printer.text("ok")
                    printer.cut()
                    printer.close()
                    self.DEV = DEV #set path printer main
                    self.saveNewPortPrinter()
                    return
                except ValueError:
                    pass
        elif SettingsManager().system.type == "Windows":    
            try:
                printer = Usb(0x6868,0x0200)
                printer.text("ok")
                printer.cut()
                printer.close()
            except:
                pass
    def openCashDrawing(self):
        match SettingsManager().system.type:
            case strings.system_linux:
                try:
                    print("Open Cash Drawing on linux")
                    os.system(f"echo -en '\033p011' > {self.DEV}")
                except:
                    QMessageBox.warning(None,strings.msg_error,strings.msg_cash_drawing_not_found)
        
            case strings.system_windows:
                try:
                    print("Open Cash Drawing on windows")
                    os.system(f"echo -en '\033p011' > {self.DEV}")
                except:
                    print("Open Cash Drawing on windows")
            case strings.system_mac:
                try:
                    print("Open Cash Drawing on mac")
                    resultCommand = os.system(f"echo -en '\033p011' > {self.DEV}")
                    print("result command:", resultCommand)
                except:
                    QMessageBox.warning(None,strings.msg_error,strings.msg_cash_drawing_not_found)
            case _:
                QMessageBox.warning(None,strings.msg_error,strings.msg_type_system_not_found)

    def printSale(self,saleEntity:SaleEntity):
        try:
            dev = File(self.DEV)
            #img = Image.open("logo.png")
            #resize_img = img.resize((400,200))
            #dev.image(resize_img)
            dev.text(CABEZERA +
                    "Fecha: "+saleEntity.dateTime+ "    \n"+
                    #"Folio: "+str(folio)+"\n"+
                    "Atendio:"+saleEntity.employe.firstName+"\n")
            dev.text("-------------------------------\n")
            #dev.text(tabulate(articulos_v,headers=["Nom","Can","To","iva"],tablefmt='simple'))
            dev.text("\n-------------------------------\n")
            dev.text("                   Total:"+str(saleEntity.getTotal())+"\n")
            dev.text("                   Pago:"+str(saleEntity.payClient)+"\n")
            dev.text("                   Cambio:"+str(saleEntity.changeClient)+"\n")
            dev.text("        Pago En Efectivo \n" )
            dev.text(numero_to_letras(saleEntity.getTotal()) + "\n")

            dev.text(" PARA CUALQUIER ACLARACION Y/O ")
            dev.text(" DEVOLUCION CONSERVE SU TICKET ")
            dev.text("    Despues de 2 dias no se    ")
            dev.text("    aceptan devoluciones ni    ")
            dev.text("         se facturara          ")
            dev.text("    ¡GRACIAS POR SU COMPRA! \n")
            dev.cut()
            dev.close()
        except FileNotFoundError:
            resultPrinterTicket = QMessageBox().warning(None,strings.msg_error,strings.msg_ask_reprinter_ticket_sale,QMessageBox.Yes|QMessageBox.No)
            if resultPrinterTicket == QMessageBox.Yes:
                self.scanPortPrinter()#buscamos el puerto de la impresora
                self.printSale(saleEntity)