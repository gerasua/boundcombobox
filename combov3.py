import collections
import sys
from PyQt5 import QtCore, QtWidgets
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import logging
from PyQt5.uic import loadUi

#Logging and console
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(funcName)s:%(message)s')
file_handler = logging.FileHandler('error.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class Ejemplo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.marcas = {"Sin datos": ["Sin datos"]}
        self.initUI()

    def initUI(self):
        loadUi('combo.ui', self)
        self.combo_mar.currentIndexChanged[str].connect(self.llenar_comboBox_modelos)
        self.cargar_marcas()
        self.show()        

    @QtCore.pyqtSlot()    
    def llenar_comboBox_marcas(self):
        self.combo_mar.clear()
        self.combo_mar.addItems(sorted(self.marcas.keys()))

    @QtCore.pyqtSlot(str)    
    def llenar_comboBox_modelos(self,  marca):
        self.combo_mod.clear()
        self.combo_mod.addItems(self.marcas[marca])

    def cargar_marcas(self):
        try:
            dbconfig = read_db_config()
            conn = MySQLConnection(**dbconfig)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM marcas ORDER BY marca DESC")
            reader = cursor.fetchall()
            try:
                data = collections.defaultdict(list)
                for row in reader:
                    data[row[0]].append(row[1])
                self.marcas = dict(data)
                logger.debug("Datos: {}".format(self.marcas))
            except Exception as e:
                logger.exception("Error For: {}".format(e))
        except Error as e:
            logger.exception("Error DB: {}".format(e))
        finally:
            cursor.close()
            conn.close()
        self.llenar_comboBox_marcas()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ejemplo()
    sys.exit(app.exec_()) 