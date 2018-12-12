# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Tomi\.designer\amoba_zaro.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from amoba_jatek import Ui_amoba_jatek

class Ui_MainWindow2(object):

    def open_jatek_Window(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_amoba_jatek()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(852, 650)
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        font.setPointSize(20)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 0, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 170, 241, 51))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.open_jatek_Window)

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 400, 771, 192))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 340, 171, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.btn_eredmenyek)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "amoba_zaro"))
        self.label.setText(_translate("MainWindow", "Játék vége!"))
        self.pushButton.setText(_translate("MainWindow", "Új játék"))
        self.pushButton_2.setText(_translate("MainWindow", "Eredmények:"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


    def btn_eredmenyek(self):     # az eredmény gombra kattintva fusson le, majd az adatok listát írja a widget-be
        try:
            inFile=open('kimentes.txt',mode='r',encoding='utf-8')
            adatok=[]
            for sor in inFile:
                sor=sor.strip()
                adatok.append(sor)
            self.listWidget.addItems(adatok)
            self.listWidget.addItem('\n')
            inFile.close()
        except Exception as error:
            print(error)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

