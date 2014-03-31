# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teledit.ui'
#
# Created: Tue Feb 04 20:14:40 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtSql import *
import config
import MySQLdb

IP="192.168.2.200"

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(900, 445)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Icons/Teledit/Icon-76@2x.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color:#AFBCE4"))
        self.centralWidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.LFax = QtGui.QLineEdit(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.LFax.setFont(font)
        self.LFax.setStyleSheet(_fromUtf8("background-color:#FFFFFF"))
        self.LFax.setObjectName(_fromUtf8("LFax"))
        self.gridLayout_3.addWidget(self.LFax, 0, 3, 1, 1)
        self.LInfo = QtGui.QLineEdit(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.LInfo.setFont(font)
        self.LInfo.setStyleSheet(_fromUtf8("background-color:#FFFFFF"))
        self.LInfo.setObjectName(_fromUtf8("LInfo"))
        self.gridLayout_3.addWidget(self.LInfo, 0, 1, 1, 1)
        self.LName = QtGui.QLineEdit(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.LName.setFont(font)
        self.LName.setStyleSheet(_fromUtf8("background-color:#FFFFFF"))
        self.LName.setObjectName(_fromUtf8("LName"))
        self.gridLayout_3.addWidget(self.LName, 0, 0, 1, 1)
        self.LNummer = QtGui.QLineEdit(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.LNummer.setFont(font)
        self.LNummer.setStyleSheet(_fromUtf8("background-color:#FFFFFF"))
        self.LNummer.setObjectName(_fromUtf8("LNummer"))
        self.gridLayout_3.addWidget(self.LNummer, 0, 2, 1, 1)
        self.LAuthor = QtGui.QLineEdit(self.centralWidget)
        self.LAuthor.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.LAuthor.setFont(font)
        self.LAuthor.setStyleSheet(_fromUtf8("background-color:#FFFFFF"))
        self.LAuthor.setObjectName(_fromUtf8("LAuthor"))
        self.gridLayout_3.addWidget(self.LAuthor, 0, 4, 1, 1)
        self.LDatum = QtGui.QLineEdit(self.centralWidget)
        self.LDatum.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.LDatum.setFont(font)
        self.LDatum.setStyleSheet(_fromUtf8("background-color:#FFFFFF"))
        self.LDatum.setObjectName(_fromUtf8("LDatum"))
        self.gridLayout_3.addWidget(self.LDatum, 0, 5, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 3, 2, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.BDel = QtGui.QPushButton(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.BDel.setFont(font)
        self.BDel.setStyleSheet(_fromUtf8("background-color:#EFC58B"))
        self.BDel.setObjectName(_fromUtf8("BDel"))
        self.gridLayout_4.addWidget(self.BDel, 0, 2, 1, 1)
        self.BUpdate = QtGui.QPushButton(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.BUpdate.setFont(font)
        self.BUpdate.setStyleSheet(_fromUtf8("background-color:#EFC58B"))
        self.BUpdate.setObjectName(_fromUtf8("BUpdate"))
        self.gridLayout_4.addWidget(self.BUpdate, 0, 1, 1, 1)
        self.BQuit = QtGui.QPushButton(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.BQuit.setFont(font)
        self.BQuit.setStyleSheet(_fromUtf8("background-color:#EFC58B"))
        self.BQuit.setObjectName(_fromUtf8("BQuit"))
        self.gridLayout_4.addWidget(self.BQuit, 1, 2, 1, 1)
        self.BClear = QtGui.QPushButton(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.BClear.setFont(font)
        self.BClear.setStyleSheet(_fromUtf8("background-color:#EFC58B"))
        self.BClear.setObjectName(_fromUtf8("BClear"))
        self.gridLayout_4.addWidget(self.BClear, 1, 1, 1, 1)
        self.BSuche = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BSuche.sizePolicy().hasHeightForWidth())
        self.BSuche.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.BSuche.setFont(font)
        self.BSuche.setStyleSheet(_fromUtf8("background-color:#EFC58B"))
        self.BSuche.setObjectName(_fromUtf8("BSuche"))
        self.gridLayout_4.addWidget(self.BSuche, 0, 0, 2, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 4, 2, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tableWidget = QtGui.QTableWidget(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(_fromUtf8("background-color:#FFFFFF"))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Info', 'Nummer', 'Fax', 'Author', 'Datum', 'Key'])

        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 900, 18))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setMovable(False)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        def clicked(row, column):
            item = self.tableWidget.item(row, column)
            ID = item.text()
            ID=int(ID)
            global ID
            
            print ID
            print("ID: ", ID)

        def suche():
            search=self.LName.text()
            self.tableWidget.clear()
            self.tableWidget.setHorizontalHeaderLabels(['Name', 'Info', 'Nummer', 'Fax', 'Author', 'Datum', 'Key'])

            conn = MySQLdb.connect(host=IP,
                           user="radistart",
                           passwd="radistart",
                           db="Telefonbuch")
            cursor = conn.cursor()
            val="'%"+str(search)+"%'"
            sql = ("SELECT * FROM Telefonbuch WHERE Name LIKE "+val)
            cursor.execute(sql)
            rows = cursor.fetchall()
            #print rows
            for i in cursor:
                A=0
                #print i[0], i[1], i[2], i[3]
                
                for j in rows:
                    self.tableWidget.setItem(A,0, QtGui.QTableWidgetItem(j[0]))
                    self.tableWidget.setItem(A,1, QtGui.QTableWidgetItem(j[1]))
                    self.tableWidget.setItem(A,2, QtGui.QTableWidgetItem(j[2]))
                    self.tableWidget.setItem(A,3, QtGui.QTableWidgetItem(j[3]))
                    self.tableWidget.setItem(A,4, QtGui.QTableWidgetItem(j[4]))
                    self.tableWidget.setItem(A,5, QtGui.QTableWidgetItem(j[5]))
                    self.tableWidget.setItem(A,6, QtGui.QTableWidgetItem(str(j[6])))


                    A=A+1

            self.tableWidget.resizeColumnsToContents()
            cursor.close()
            conn.close()

        A=0
        
        def insert():
            self.tableWidget.clear()
            self.tableWidget.setHorizontalHeaderLabels(['Name', 'Info', 'Nummer', 'Fax', 'Author', 'Datum', 'Key'])

            Name =self.LName.text()
            Nummer =self.LNummer.text()
            Info =self.LInfo.text()
            Fax =self.LFax.text()
            Author=config.User
            Datum=config.Date2
            conn = MySQLdb.connect(host=IP,
                           user="radistart",
                           passwd="radistart",
                           db="Telefonbuch")
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO Telefonbuch (Name, Info, Nummer, Fax, Author, Datum) values (%s, %s, %s, %s, %s, %s)""", (Name,Info,Nummer,Fax, Author, Datum))
            conn.commit()
            cursor.close()
            conn.close()
            suche()

        def update():
            self.tableWidget.clear()
            self.tableWidget.setHorizontalHeaderLabels(['Name', 'Info', 'Nummer', 'Fax', 'Author', 'Datum', 'Key'])

            Name=str(self.LName.text())
            Info=str(self.LInfo.text())
            Nummer =str(self.LNummer.text())
            Fax =str(self.LFax.text())
            Author=str(config.User)
            Datum=str(config.Date2)
            print (Name, Nummer, Info, Fax, Author, Datum)
            conn = MySQLdb.connect(host=IP,
                           user="radistart",
                           passwd="radistart",
                           db="Telefonbuch")
            cursor = conn.cursor()
            cursor.execute("""
                        UPDATE Telefonbuch
                        SET Name=%s, Nummer=%s, Info=%s, Fax=%s, Author=%s, Datum=%s
                        WHERE Name=%s AND Info=%s
                        """, (Name, Nummer, Info, Fax, Author, Datum, Name, Info))
            conn.commit()
            cursor.close()
            conn.close()

        def delete():
            conn = MySQLdb.connect(host=IP,
                           user="radistart",
                           passwd="radistart",
                           db="Telefonbuch")
            cursor = conn.cursor()
            cursor.execute("""
                        Delete FROM Telefonbuch
                        WHERE id=%s
                        """, str(ID))
            conn.commit()
            cursor.close()
            conn.close()
            suche()
            


        self.tableWidget.cellClicked.connect(clicked)
 
        

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.BClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.LName.clear)
        QtCore.QObject.connect(self.BClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.LInfo.clear)
        QtCore.QObject.connect(self.BClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.LNummer.clear)
        QtCore.QObject.connect(self.BClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.LFax.clear)
        QtCore.QObject.connect(self.BDel, QtCore.SIGNAL(_fromUtf8("clicked()")), delete)
        QtCore.QObject.connect(self.BQuit, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.BUpdate, QtCore.SIGNAL(_fromUtf8("clicked()")), update)
        QtCore.QObject.connect(self.BSuche, QtCore.SIGNAL(_fromUtf8("clicked()")), suche)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Editor für das Online-Telefonbuch", None))
        self.LFax.setText(_translate("MainWindow", "Fax", None))
        self.LInfo.setText(_translate("MainWindow", "Info", None))
        self.LName.setText(_translate("MainWindow", "Name", None))
        self.LNummer.setText(_translate("MainWindow", "Nummer", None))
        self.LAuthor.setText(_translate("MainWindow", config.User, None))
        self.LDatum.setText(_translate("MainWindow", config.Date2, None))
        self.BDel.setText(_translate("MainWindow", "Eintrag löschen", None))
        self.BUpdate.setText(_translate("MainWindow", "Eintrag bearbeiten", None))
        self.BQuit.setText(_translate("MainWindow", "Abbrechen", None))
        self.BClear.setText(_translate("MainWindow", "Eingaben löschen", None))
        self.BSuche.setText(_translate("MainWindow", "Eintrag suchen", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

