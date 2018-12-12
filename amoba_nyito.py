# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Tomi\.designer\amoba_nyito.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os,sys
from amoba_jatek import Ui_amoba_jatek

class Ui_MainWindow(object):

    def open_jatek_Window(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_amoba_jatek()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 180, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 220, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(360, 190, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 230, 161, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 120, 431, 61))
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 0, 561, 61))
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(220, 300, 301, 61))
        #ide írtam:
        self.btnStart.clicked.connect(self.save_to_file)


        self.btnStart.clicked.connect(self.open_jatek_Window)
        self.btnStart.clicked.connect(self.reload_data)


        font = QtGui.QFont()
        font.setFamily("Narkisim")
        font.setPointSize(16)
        self.btnStart.setFont(font)
        self.btnStart.setObjectName("btnStart")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(550, 140, 71, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "amoba_nyito"))
        self.label.setText(_translate("MainWindow", "1. Játékos neve:"))
        self.label_2.setText(_translate("MainWindow", "2. Játékos neve:"))
        self.label_3.setText(_translate("MainWindow", "Mekkora táblán szeretnétek játszani (N x N)?"))
        self.label_4.setText(_translate("MainWindow", "Amőba beadandó v1.0"))
        self.btnStart.setText(_translate("MainWindow", "Kezdés"))


    def win(self):     #meghatározza ki nyert (azért itt van, mert a másik ablak nincs kész)
        pass

    def save_to_file(self):       #bevitt adatokat kimenti fáljba
        int=['0','1','2','3','4','5','6','7','8','9']
        try:
            outFile=open('kimentes.txt',mode='w',encoding='utf-8')
            jatekos1=self.lineEdit.text()
            for i in int:
                if i in jatekos1:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Warning!")
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("Az 1. játékos neve nem megengedett karaktert tartalmaz!")
                    msg.exec()
                    break

            jatekos2=self.lineEdit_2.text()
            for k in int:
                if k in jatekos2:
                    msg2 = QtWidgets.QMessageBox()
                    msg2.setWindowTitle("Warning!")
                    msg2.setIcon(QtWidgets.QMessageBox.Warning)
                    msg2.setText("Az 2. játékos neve nem megengedett karaktert tartalmaz!")
                    msg2.exec()
                    break

            meret=self.lineEdit_3.text()
            for j in int:
                if j in jatekos2:
                    msg2 = QtWidgets.QMessageBox()
                    msg2.setWindowTitle("Warning!")
                    msg2.setIcon(QtWidgets.QMessageBox.Warning)
                    msg2.setText("A méretnek egy számnak kell lennie!")
                    msg2.exec()

            outFile.write("Az első játékos neve: {0}\n" .format(jatekos1))
            outFile.write("a második játékos neve: {0}\n".format(jatekos2))
            outFile.write("A tábla mérete: {0} \n".format(meret))
            outFile.write("A nyertes: {0} \n" .format(jatekos1))
            outFile.close()
        except Exception as error:
            print(error)

    def reload_data(self):     #fájlból újratölti az adatokat
        try:
            inFile=open('kimentes.txt',mode='r',encoding='utf-8')
            adatok=[]
            for sor in inFile:
                sor=sor.strip()
                adatok.append(sor)
            print(adatok)
            inFile.close()
        except Exception as error:
            print(error)

    def eredmenyek(self):     # az eredmény gombra kattintva fusson le a reload_data, majd az adatok listát írja a widget-be
        jatekos1_pontok=0
        jatekos2_pontok=0
        tmp='nyertes: '
        inFile=open('kimentes.txt',mode='r',encoding='utf-8')
        for sor in inFile:
            if tmp in sor:
                ind=tmp.find()+1
                if sor[ind]=='jatekos1':
                    jatekos1_pontok+=1
                else:
                    jatekos2_pontok+=1



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


