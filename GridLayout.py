from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog,QGridLayout,QGroupBox,QPushButton,QVBoxLayout
import sys

class window_jatek(QDialog):
    def __init__(self):
        super().__init__()

        self.title="Játék"
        self.left=100
        self.top=100
        self.width=600
        self.height=800

        self.InitUi()


    def InitUi(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.GridLayoutCreation()
        vboxLAyout=QVBoxLayout()
        vboxLAyout.addWidget(self.groupBox)
        self.setLayout(vboxLAyout)
        self.show()

    def GridLayoutCreation(self):
        #n=int(input("Kérem a méretet: "))
        self.groupBox=QGroupBox("Amőba játékfelület")
        gridLayout=QGridLayout()
        for i in range(10):
            for j in range(10):
                gridLayout.addWidget(QPushButton(" "),i , j)


        self.groupBox.setLayout(gridLayout)

#main()
App=QtWidgets.QApplication(sys.argv)
window_jatek=window_jatek()
sys.exit(App.exec())